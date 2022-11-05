#importa la libreria de flask
from flask import Flask, render_template, request, flash, session, redirect
#creamos una instacia de flask
import sqlite3
import os
from werkzeug.utils import escape
#from forms.formularios import Ingresos, Salidas, Usuarios, Proveedores, Celulares, Login, g_usuario, g_prov, UsuariosF, g_usuarioF
import hashlib

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

app.run(debug=True)