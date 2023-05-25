import mysql.connector
from config import Config
import openai
import pandas as pd

from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity

# Set up the OpenAI API client
openai.api_key = Config.OPENAI.OPENAI_API_KEY

def collectTrainData(mensaje, telefonoCliente):

    db = mysql.connector.connect(
        host = Config.DATABASE.HOST,
        user = Config.DATABASE.USER,
        database=Config.DATABASE.DATABASE
    )

    cursor=db.cursor()
    cursor.execute("SELECT prompt, completion FROM registro_entrenamiento UNION ALL SELECT prompt, completion FROM registro_nuevos WHERE telefono_wa = %s", (telefonoCliente,))
    rows_entrenamiento = cursor.fetchall()

    # conversaciones = []

    # for row in rows_entrenamiento:
    #     prompt = row[0]
    #     completion = row[1] 
        
    #     conversaciones.append({"role": "user", "content": prompt})
    #     conversaciones.append({"role": "system", "content": completion})

    
    # Crear un DataFrame para almacenar los datos
    conocimiento_df = pd.DataFrame(rows_entrenamiento, columns=['prompt', 'completion'])
    # Aplicar la función de embedding a los datos
    conocimiento_df['Embedding'] = conocimiento_df['prompt'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))

    # Guardar los resultados en un archivo CSV
    # conocimiento_df.to_csv('embeddings.csv')
        
    cursor.close()
    db.close()


    respuesta = buscar(mensaje, conocimiento_df)

    if not respuesta.empty:
        if respuesta.iloc[0]["Similitud"] > 0.8:
            resultado = respuesta.iloc[0]["completion"]
            return resultado
        else:
            return "Lo siento, no entendí que quiso decir. Solo estoy habilitado a responder preguntas acerca de nuestros servicios. ¿Podría usted repetirlo?"
    else:
        return ""  # Devolver una cadena vacía si no se encuentra ninguna respuesta

def buscar(busqueda, datos, n_resultados=2):
    busqueda_embed = get_embedding(busqueda, engine="text-embedding-ada-002")
    datos["Similitud"] = datos['Embedding'].apply(lambda x: cosine_similarity(x, busqueda_embed))
    datos = datos.sort_values("Similitud", ascending=False)
    return datos.iloc[:n_resultados][["completion", "Similitud", "Embedding"]]