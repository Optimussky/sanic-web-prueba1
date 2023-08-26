from sanic_ext import render
from sanic import Sanic

from sanic.response import json
from sanic import response
from jinja2 import Environment, FileSystemLoader

import mysql.connector


# Creando una instancia de la App SANIC
app = Sanic(__name__)

# Configurando la conexión a la DB
db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "D354rr0ll0f4t1g4",
	database = "dbfatiga"
	)

# Definir las rutas del CRUD
## Ruta para obtener todos los registros;
"""
@app.route("/usuarios", methods=["GET"])
async def obtener_usuarios(request):
    cursor = db.cursor()
    cursor.execute("SELECT nombre,usuario FROM tbUsuario")
    usuarios = cursor.fetchall()
    #print([usuarios for u in usuarios])

    return json(usuarios)

"""

@app.get("/")
@app.ext.template("index.html")
async def handler(request):
    return {"seq": ["one", "two"]}


@app.route("/usuarios", methods=["GET"])
async def obtener_usuarios(request):
    cursor = db.cursor()
    cursor.execute("SELECT idUsuario,nombre,usuario FROM tbUsuario")
    usuarios = cursor.fetchall()

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("usuarios.html")
    rendered_template = template.render(usuarios=usuarios)

    return response.html(rendered_template)

# Ruta para actualizar un registro existente

if __name__ == '__main__':

	app.run(host = '0.0.0.0',port = 8500)