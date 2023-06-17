import openai
import mysql.connector
import pandas as pd

from config import Config
from embedding_product import embedding_message
from embedding_info import embedding_info

# Establecer la clave de la API de OpenAI
openai.api_key = Config.OPENAI.OPENAI_API_KEY

def chatgpt_completion(mensaje, telefonoCliente):
    # Conectar a la base de datos MySQL
    db = mysql.connector.connect(
        host=Config.DATABASE.HOST,
        user=Config.DATABASE.USER,
        database=Config.DATABASE.DATABASE
    )

    cursor2= db.cursor()
    # Obtener los datos combinados de la tabla "lanchas"
    cursor2.execute("SELECT prompt, completion FROM registro_nuevos WHERE telefono_wa = %s ORDER BY id DESC LIMIT 10;", (telefonoCliente,))
    rows_mesagges = cursor2.fetchall()


    # Crear un DataFrame para almacenar los datos
    conversacion_df = pd.DataFrame(rows_mesagges, columns=['prompt', 'completion'])
    # Aplicar la función de embedding a los datos
    cursor2.close()
    db.close()

    # TODO ES SE VA A OTRO ARCHIVO
    palabras_clave_lanchas = ['productos', 'precio', 'disponibilidad', 'categorias', 'lanchas']
    # Convertir el mensaje a minúsculas para una comparación sin distinción de mayúsculas
    mensaje = mensaje.lower()
    palabras_clave_info = ['restaurantes', 'salidas', 'paseos', 'recorrer']


    # Verificar si alguna palabra clave está presente en el mensaje
    if any(palabra in mensaje for palabra in palabras_clave_lanchas):
        return embedding_message(mensaje)
    elif any(palabra in mensaje for palabra in palabras_clave_info):
        return embedding_info(mensaje)
    else:
        message_objects = []
        # Mensajes de introducción para el chat
        message_objects.append({"role": "system", "content": ""})

        for index, row in conversacion_df.iterrows():
            prompt = row['prompt']
            completion = row['completion']

            message_objects.append({"role": "user", "content": prompt})
            message_objects.append({"role": "assistant", "content": completion})

        message_objects.append({"role": "user", "content": mensaje})

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
