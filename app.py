#importa la libreria de flask
from flask import Flask, render_template, request, flash, session, redirect
from config import config
#creamos una instacia de flask
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import os
from werkzeug.utils import escape
from forms.formularios import Register, Arbitrator, Stadium,Login,commentator, Equipos, jugadores

#Importar Json para manejo de querys en JS
import json

#fecha y hora
from datetime import datetime

#models
from models.ModelUser import ModelUser
from models.ModelTable import ModelTable
from models.ModelArbitrator import ModelArbitrator
from models.ModelStadium import ModelStadium
from models.ModelComentarios import ModelComentarios

#entities
from models.entities.User import Users




app = Flask(__name__)
Login_Manager_app=LoginManager(app)
db=MySQL(app)
global Type, comentario 
Type=0
comentario =0

@Login_Manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)


@app.route("/", methods=["GET", "POST"])
def home():    
    global Type
    data=ModelTable.positions(db)            
    return render_template("index.html", table=data, Type=Type)
    

@app.route("/Results", methods=["GET", "POST"])
def results():        
    global Type
    data=ModelTable.positions(db)    
    return render_template("Results.html", table=data, Type=Type)

@app.route("/Register", methods=["GET", "POST"])
def register():    
    frm = Register()
    data=ModelTable.positions(db)        
    if request.method=="POST":    
        user= Users(frm.cellphone.data, frm.username.data, frm.password.data, 0) 
        ModelArbitrator.create(db,user)  
        return redirect ("/logout")
    else:
        return render_template("register.html", frm=frm, table=data, Type=Type) 

@app.route("/live")
def live():
    global Type        
    return render_template("live.html", Type=Type) 
       
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
                return redirect ("/")
            else:
                flash("Weon ta mal")
            return render_template("Login.html", frm=frm, Type=Type)
        else:
            flash("Weon no existe")
            return render_template("Login.html", frm=frm, Type=Type)
    else:
        return render_template("Login.html", frm=frm, Type=Type)

@app.route("/logout")
def logout():
    global Type
    logout_user()
    Type=0
    return redirect ("/Login")
    
@app.route("/Config", methods=["GET", "POST"])
@login_required
def conf():   
    if Type==3:             
        frm_estadio = Stadium()  
        frm_jugador = jugadores()
        frm_equipos= Equipos()
        frm_arbitro = Arbitrator()  
        arbitrator=ModelArbitrator.AllArbitrator(db)   
        stadium=ModelStadium.AllStadium(db)  
        
        if request.method=="POST":   
            if 'crear_arbitro' in request.form: 
                name=frm_arbitro.name.data
                country=frm_arbitro.country.data                
                ModelArbitrator.create(db,name,country) 
                return redirect ("/Config")    
            if 'delete_arbitro' in request.form: 
                id=frm_arbitro.Id.data                           
                ModelArbitrator.delete(db,id) 
                return redirect ("/Config")    
            if 'crear_estadio' in request.form: 
                name=frm_estadio.name.data
                country=frm_estadio.country.data                
                capacidad=frm_estadio.capacidad.data  
                ModelStadium.create(db,name,country,capacidad) 
                return redirect ("/Config")    
            if 'delete_estadio' in request.form: 
                id=frm_estadio.Id.data                           
                ModelStadium.delete(db,id) 
                return redirect ("/Config")             
        return render_template("/admin/Config.html", 
            Arbitrator=arbitrator,Stadium=stadium, frm_arbitro=frm_arbitro, frm_estadio=frm_estadio,frm_equipos=frm_equipos, frm_jugador=frm_jugador)
    else:
        return redirect ("/")

@app.route("/Programming", methods=["GET", "POST"])
@login_required
def progamming():   
    if Type==3:       
        return render_template("/admin/Menu.html")
    else:
        return redirect ("/")
    
@app.route("/Comment", methods=["GET", "POST"])
@login_required
def comment():  
    global comentario 
    if Type==2:       
        now=datetime.now()
        frm=commentator()
        fecha=str(now.date())
        hora=str(now.hour)+":"+str(now.minute)+":"+str(now.second)
        print(fecha+" "+hora)
        if request.method=="POST":   
            if 'create' in request.form: 
                comentario=comentario+1
                comment=frm.comment.data                             
                ModelComentarios.new(db,comentario,comment)   
                print("Holi")              
            if 'delete' in request.form: 
                comentario=0                                        
                ModelComentarios.clean(db) 
        return render_template("/commentator/comment.html",frm=frm)
    else:
        return redirect ("/")

@app.route("/data", methods=["GET"])
def data():        
    data=ModelComentarios.last(db)            
    y = json.dumps(data)      
    return (y)

app.config.from_object(config['development'])
app.run()