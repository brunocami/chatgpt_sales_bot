#ChatBot inteligente con WhatsApp en Python
# import openai
# from config import Config
# from db_utils import collectTrainData

# # Set up the OpenAI API client
# openai.api_key = Config.OPENAI.OPENAI_API_KEY

# def chatgpt_conection(mensaje, telefonoCliente):
    
#     conversaciones = collectTrainData(mensaje, telefonoCliente)
#     # Agregar la pregunta actual a las conversaciones
#     conversaciones.append({"role": "user", "content": mensaje})
#     # Llamar a la API de OpenAI para generar texto con ChatGPT

#     messages = conversaciones

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages,
#         max_tokens=200,
#         n=1,
#         stop=None,
#         temperature=0.5
#     )

#     return response