#importa la libreria de flask
from flask import Flask, render_template, request, flash, session, redirect
from config import config
#creamos una instacia de flask
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import os
from werkzeug.utils import escape
from forms.formularios import Register, Salidas, Usuarios, Proveedores, Celulares, Login, g_usuario, g_prov, UsuariosF, g_usuarioF

#models
from models.ModelUser import ModelUser
from models.ModelTable import ModelTable

#entities
from models.entities.User import Users




app = Flask(__name__)
Login_Manager_app=LoginManager(app)
db=MySQL(app)

@app.route("/", methods=["GET", "POST"])
def home():    
    data=ModelTable.positions(db)    
    return render_template("index.html", table=data)

@app.route("/Results", methods=["GET", "POST"])
def results():        
    data=ModelTable.positions(db)    
    return render_template("Results.html", table=data)

@app.route("/Register", methods=["GET", "POST"])
def register():    
    frm = Register()
    data=ModelTable.positions(db)        
    if request.method=="POST":    
        user= Users(frm.cellphone.data, frm.username.data, frm.password.data, 0) 
        ModelUser.create(db,user)  
        return redirect ("/Login")
    else:
        return render_template("register.html", frm=frm, table=data) 

    
@app.route("/Login", methods=["GET", "POST"])
def log():
    user= Users(0, "invitado", "invitado", 0)  
    frm = Login()    
    if request.method=="POST":    
        if 'entrar' in request.form:
            user= Users(0, frm.username.data, frm.password.data, 0)           
            logged=ModelUser.login(db, user)
        elif 'invitado' in request.form:                     
            logged=ModelUser.login(db, user)
        if logged!=None:  
            if logged.password:   
                return redirect ("/Menu", menu(logged))
            else:
                flash("Weon ta mal")
            return render_template("Login.html", frm=frm)
        else:
            flash("Weon no existe")
            return render_template("Login.html", frm=frm)
    else:
        return render_template("Login.html", frm=frm)

@app.route("/Menu", methods=["GET", "POST"])
def menu(logged):   
    if logged.type==3:       
        return render_template("/admin/Menu.html", frm=frm)
    elif logged.type==2:
        return render_template("/commentator/Menu.html", frm=frm)
    elif logged.type==1:
        return render_template("/guest/Menu.html", frm=frm) 
    else:    
        return redirect ("/Login")

app.config.from_object(config['development'])
app.run()