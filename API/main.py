import ssl
from fastapi import FastAPI, HTTPException
import mysql.connector
from API.db import get_db_connection
from API.models import Usuario, Receta, Ingrediente
import uvicorn

# Crear la instancia de FastAPI
app = FastAPI()

# Definir el contexto SSL con el certificado y la clave privada
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile="ssl/cert.pem", keyfile="ssl/key.pem")

# Endpoint de prueba
@app.get("/")
def read_root():
    return {"message": "API de recetas e ingredientes con HTTPS y MariaDB"}

# Obtener un usuario por ID
@app.get("/usuarios/{usuario_id}")
def get_usuario(usuario_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM Usuario WHERE id_usuario = %s", (usuario_id,))
    usuario = cursor.fetchone()
    
    if usuario:
        return usuario
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Obtener una receta por ID
@app.get("/recetas/{receta_id}")
def get_receta(receta_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM Receta WHERE id_receta = %s", (receta_id,))
    receta = cursor.fetchone()
    
    if receta:
        return receta
    else:
        raise HTTPException(status_code=404, detail="Receta no encontrada")

# Obtener un ingrediente por ID
@app.get("/ingredientes/{ingrediente_id}")
def get_ingrediente(ingrediente_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM Ingrediente WHERE id_ingrediente = %s", (ingrediente_id,))
    ingrediente = cursor.fetchone()
    
    if ingrediente:
        return ingrediente
    else:
        raise HTTPException(status_code=404, detail="Ingrediente no encontrado")

# Iniciar el servidor de FastAPI con HTTPS
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_context=ssl_context)
