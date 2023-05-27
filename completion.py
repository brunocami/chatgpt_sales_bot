import openai
import mysql.connector
import pandas as pd
from openai.embeddings_utils import get_embedding, cosine_similarity
from config import Config

# Establecer la clave de la API de OpenAI
openai.api_key = Config.OPENAI.OPENAI_API_KEY

def chatgpt_completion(mensaje, telefonoCliente):
    # Conectar a la base de datos MySQL
    db = mysql.connector.connect(
        host=Config.DATABASE.HOST,
        user=Config.DATABASE.USER,
        database=Config.DATABASE.DATABASE
    )

    cursor = db.cursor()
    cursor2= db.cursor()
    # Obtener los datos combinados de la tabla "lanchas"
    cursor.execute("SELECT combined FROM lanchas")
    rows = cursor.fetchall()
    cursor2.execute("SELECT prompt, completion FROM registro_nuevos WHERE telefono_wa = %s", (telefonoCliente,))
    rows_mesagges = cursor2.fetchall()


    # Crear un DataFrame para almacenar los datos
    product_data_df = pd.DataFrame(rows, columns=['combined'])
    conversacion_df = pd.DataFrame(rows_mesagges, columns=['prompt', 'completion'])
    # Aplicar la función de embedding a los datos
    product_data_df['text_embedding'] = product_data_df.combined.apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
    conversacion_df['Embedding'] = conversacion_df['prompt'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))

    cursor.close()
    db.close()

    customer_input = mensaje

    # Obtener el embedding de la pregunta del cliente utilizando OpenAI
    response = openai.Embedding.create(
        input=customer_input,
        model="text-embedding-ada-002"
    )
    embeddings_customer_question = response['data'][0]['embedding']

    # Calcular la similitud coseno entre los embeddings de las lanchas y la pregunta del cliente
    product_data_df['search_similarity'] = product_data_df.text_embedding.apply(lambda x: cosine_similarity(x, embeddings_customer_question))
    product_data_df = product_data_df.sort_values('search_similarity', ascending=False)

    message_objects = []

    # Mensajes de introducción para el chat
    message_objects.append({"role": "system", "content": "Soy un chatbot de ventas de una empresa de alquiler de lanchas. Estoy aquí para ayudarte a elegir la mejor categoría."})

    for index, row in conversacion_df.iterrows():
        prompt = row['prompt']
        completion = row['completion']

        message_objects.append({"role": "user", "content": prompt})
        message_objects.append({"role": "assistant", "content": completion})

    message_objects.append({"role": "user", "content": customer_input})

    products_list = []

    # Crear una lista de respuestas de las lanchas
    for index, row in product_data_df.iterrows():
        brand_dict = {'role': "assistant", "content": f"{row['combined']}"}
        products_list.append(brand_dict)

    message_objects.extend(products_list)

    # Generar una respuesta utilizando el modelo de chat de OpenAI
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_objects,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5
    )

    return completion.choices[0].message['content']