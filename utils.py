#CONECTAMOS A LA BASE DE DATOS
from flask import jsonify
import mysql.connector
from config import Config
from db_utils import collectTrainData
import time

from heyoo import WhatsApp
def enviar(telefonoRecibe,respuesta,token,idNumeroTelefono):
  #INICIALIZAMOS ENVIO DE MENSAJES (token de acceso a facebook, id numero de telefono whatsapp business)
  mensajeWa=WhatsApp(token,idNumeroTelefono)
  telefonoRecibe=telefonoRecibe.replace("54911","541115")
  #ENVIAMOS UN MENSAJE DE TEXTO
  mensajeWa.send_message(respuesta,telefonoRecibe)

#SI HAY UN MENSAJE
def procesarMensaje(mensaje,idWA,timestamp,telefonoCliente):

    if mensaje is not None:

        #CONECTAMOS CON LA BASE DE DATOS
        db = mysql.connector.connect(
            host = Config.DATABASE.HOST,
            user = Config.DATABASE.USER,
            database=Config.DATABASE.DATABASE
        )
        cursor = db.cursor()
        cursor.execute("SELECT count(id) AS cantidad FROM registro_nuevos WHERE id_wa='" + idWA + "';")
        # IMPORTAMOS FUNCION PARA CONECTARSE A CHAT GPT
        response = collectTrainData(mensaje, telefonoCliente)

        # ALMACENO LA RESPUESTA DE CHATGPT EN UNA VARIABLE
        # chatgpt_response = response.choices[0].message.content

        cantidad,=cursor.fetchone()
        cantidad=str(cantidad)
        cantidad=int(cantidad)

        print(response)

        # if cantidad==0 :

        #     sql = ("INSERT INTO registro_nuevos"+ 
        #     "(mensaje_recibido,mensaje_enviado,id_wa      ,timestamp_wa   ,telefono_wa) VALUES "+
        #     "('"+mensaje+"'   ,'"+response+"','"+idWA+"' ,'"+timestamp+"','"+telefonoCliente+"');")
        #     cursor.execute(sql)
        #     db.commit()

        #     # CERRAMOS EL CURSOR Y LA CONEXION CON LA BASE DE DATOS
        #     cursor.close()
        #     db.close()

        #     enviar(telefonoCliente,response,Config.WHATSAPP.TOKEN,Config.WHATSAPP.ID_NUMERO_TELEFONO)

        # #RETORNAMOS EL STATUS EN UN JSON
        # return jsonify({"status": "success"}, 200)

procesarMensaje('donde quedan las flores?', '23123123132', 123123, '5491158487444')
