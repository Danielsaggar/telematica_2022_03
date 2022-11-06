#importa la libreria de flask
from flask import Flask, render_template, request, flash, session, redirect
from config import config
#creamos una instacia de flask
from flask_mysqldb import MySQL
import sqlite3
import os
from werkzeug.utils import escape
from forms.formularios import Ingresos, Salidas, Usuarios, Proveedores, Celulares, Login, g_usuario, g_prov, UsuariosF, g_usuarioF

#models
from models.ModelUser import ModelUser

#entities
from models.entities.User import Users




app = Flask(__name__)
db=MySQL(app)

@app.route("/", methods=["GET", "POST"])
def home():
    frm = Login()
    if request.method=="POST":    
        user= Users(0, frm.username.data, frm.password.data, 0)   
        print(frm.username.data) 
        logged=ModelUser.login(db, user)
        if logged!=None:  
            if logged.password:   
                if logged.type==3:       
                    return render_template("Home.html", frm=frm)
                else:
                    return render_template("Login.html", frm=frm)
            else:
                flash("Weon ta mal")
            return render_template("Login.html", frm=frm)
        else:
            flash("Weon no existe")
            return render_template("Login.html", frm=frm)
    else:
        return render_template("Login.html", frm=frm)


app.config.from_object(config['development'])
app.run()