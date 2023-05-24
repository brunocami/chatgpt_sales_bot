import mysql.connector
from config import Config


def collectTrainData(telefonoCliente):

    db = mysql.connector.connect(
        host = Config.DATABASE.HOST,
        user = Config.DATABASE.USER,
        password = Config.DATABASE.PASSWORD,
        database=Config.DATABASE.DATABASE
    )

    cursor=db.cursor()
    cursor.execute("SELECT mensaje_recibido, mensaje_enviado FROM registro_entrenamiento UNION ALL SELECT mensaje_recibido, mensaje_enviado FROM registro_nuevos WHERE telefono_wa = %s", (telefonoCliente,))
    rows_entrenamiento = cursor.fetchall()

    conversaciones = []

    for row in rows_entrenamiento:
        mensaje_recibido = row[0]
        mensaje_enviado = row[1] 
        
        conversaciones.append({"role": "system", "content": mensaje_enviado})
        conversaciones.append({"role": "user", "content": mensaje_recibido})
        
    cursor.close()
    db.close()
    
    return conversaciones