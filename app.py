#importa la libreria de flask
from flask import Flask, render_template, request, flash, session, redirect
from config import config
#creamos una instacia de flask
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import os
from werkzeug.utils import escape
from forms.formularios import Register, Arbitrator, Usuarios, Proveedores, Celulares, Login, g_usuario, g_prov, UsuariosF, g_usuarioF

#models
from models.ModelUser import ModelUser
from models.ModelTable import ModelTable
from models.ModelArbitrator import ModelArbitrator

#entities
from models.entities.User import Users




app = Flask(__name__)
Login_Manager_app=LoginManager(app)
db=MySQL(app)
global Type

@Login_Manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)


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
        ModelArbitrator.create(db,user)  
        return redirect ("/Login")
    else:
        return render_template("register.html", frm=frm, table=data) 

    
@app.route("/Login", methods=["GET", "POST"])
def log():
    user= Users(0, "invitado", "invitado", 0)  
    frm = Login()    
    global Type
    if request.method=="POST":    
        if 'entrar' in request.form:
            user= Users(0, frm.username.data, frm.password.data, 0)           
            logged=ModelUser.login(db, user)
        elif 'invitado' in request.form:                     
            logged=ModelUser.login(db, user)
        if logged!=None:  
            if logged.password:   
                login_user(logged)
                Type=(logged.type)
                print(Type)
                return redirect ("/Menu")
            else:
                flash("Weon ta mal")
            return render_template("Login.html", frm=frm)
        else:
            flash("Weon no existe")
            return render_template("Login.html", frm=frm)
    else:
        return render_template("Login.html", frm=frm)

@app.route("/Menu", methods=["GET", "POST"])
@login_required
def menu():   
    global Type
    print("Entre a menu: ",Type)
    if Type==3:       
        return render_template("/admin/Menu.html")
    elif Type==2:
        return render_template("/commentator/Menu.html")
    elif Type==1:
        return render_template("/guest/Menu.html") 
    else:    
        return redirect ("/Login")
    
@app.route("/Config", methods=["GET", "POST"])
@login_required
def conf():   
    if Type==3:     
        frm = Arbitrator()  
        data=ModelArbitrator.AllArbitrator(db)   
        if request.method=="POST":   
            if 'crear' in request.form: 
                name=frm.name.data
                country=frm.country.data                
                ModelArbitrator.create(db,name,country) 
                return redirect ("/Config")               
        return render_template("/admin/Config.html", data=data, frm=frm)
    else:
        return redirect ("/")

@app.route("/Programming", methods=["GET", "POST"])
@login_required
def progamming():   
    if Type==3:       
        return render_template("/admin/Menu.html")
    else:
        return redirect ("/")

app.config.from_object(config['development'])
app.run()