#ChatBot inteligente con WhatsApp en Python
from flask import Flask, request
from config import Config
from utils import procesarMensaje
from save_message_db import save_message_in_db

app = Flask(__name__)
app.config.from_object(Config.FLASK)

#CUANDO RECIBAMOS LAS PETICIONES EN ESTA RUTA
@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():
    
    #SI HAY DATOS RECIBIDOS VIA GET
    if request.method == "GET":
        #SI EL TOKEN ES IGUAL AL QUE RECIBIMOS
        if request.args.get('hub.verify_token') == "TokenDeVerificacion":
            #ESCRIBIMOS EN EL NAVEGADOR EL VALOR DEL RETO RECIBIDO DESDE FACEBOOK
            return request.args.get('hub.challenge')
        else:
            #SI NO SON IGUALES RETORNAMOS UN MENSAJE DE ERROR
          return "Error de autentificacion."
    #RECIBIMOS TODOS LOS DATOS ENVIADO VIA JSON
    data=request.get_json()
    if data['entry'][0]['changes'][0]['value']['messages'][0]['type'] == "text":
        #EXTRAEMOS EL NUMERO DE TELEFONO Y EL MANSAJE
        telefonoCliente=data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        #EXTRAEMOS EL TELEFONO DEL CLIENTE
        mensaje=data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        #EXTRAEMOS EL ID DE WHATSAPP DEL ARRAY
        idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
        #EXTRAEMOS EL TIEMPO DE WHATSAPP DEL ARRAY
        timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
        #SI HAY UN MENSAJE
        procesarMensaje(mensaje,idWA,timestamp,telefonoCliente)
    else: 
        messageType=data['entry'][0]['changes'][0]['value']['messages'][0]['type']
        #EXTRAEMOS EL NUMERO DE TELEFONO Y EL MANSAJE
        telefonoCliente=data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        #EXTRAEMOS EL TELEFONO DEL CLIENTE
        mensaje='por favor, enviar mensjaes de texto unicamente'
        #EXTRAEMOS EL ID DE WHATSAPP DEL ARRAY
        idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
        #EXTRAEMOS EL TIEMPO DE WHATSAPP DEL ARRAY
        timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']

        save_message_in_db(mensaje,idWA,timestamp,telefonoCliente,messageType)

#INICIAMOS FLASK
if __name__ == "__main__":
  app.run(debug=True, port=8000)