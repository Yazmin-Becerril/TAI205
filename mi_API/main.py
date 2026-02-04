#1. importaciones
from fastapi import FastAPI
from typing import Optional # es para manejar endpoints con parametros opcionales
import asyncio # es para manejar funciones asincronas, con tareas de multitareas, pero ahora lo usaremos para simular que estamos haciendo una peticion a una base de datos

#2. inicializacion APP
app= FastAPI(title='Mi primera API',
             description="Vazquez Becerril Estrella Yazmin",
             version="1.0.0" 
        )

#BD ficticia
usuarios_db = [
    {"id" : "1", "Nombre" : "Yazmin", "edad": 20},
    {"id" : "2", "Nombre" : "Gerardo", "edad": 20},
    {"id" : "3", "Nombre" : "Yahir", "edad": 21}
]


#3. endpoints
@app.get("/", tags=['Inicio'])
async def holaMundo():
    return {"mensaje":"Hola Mundo FASTAPI"}

@app.get("/v1/Bienvenidos", tags=['Inicio'])
async def Bienvenidos():
    return {"mensaje":"Bienvenidos"}

@app.get("/v1/promedio", tags=['Calificaciones'])
async def promedio():
    await asyncio.sleep(3) # simulamos que estamos haciendo una peticion a una base de datos y tarda 3 segundos en responder
    return {
        "Calificacion":"7.5",
        "Estatus":"200" #el significado de estatus 200 es que la peticion fue exitosa, porque 200 es el codigo de exito en HTTP
        }

@app.get("/v1/usuario/{id}", tags=['Parametro Obligatorio'])
async def consultaUno(id:int):
    await asyncio.sleep(3)
    return {
            "Resultado": "usuario encontrado",
            "Esatus":"200",  
        }
#este es un endpoint con un parametro opcional
@app.get("/v1/usuarios_op/", tags=['Parametro Opcional'])
async def consultaOp(id: Optional[int] = None):
    await asyncio.sleep(2)
    if id is not None:
        for usuario in usuarios_db:
            if usuario["id"] == id:
                return {
                    "Usuario encontrado": id, "Datos": usuario}
        return {"Mensaje": "Usuario no encontrado"}
    else:
        return {"Aviso": "No se proporciono ningun ID"}
    

    