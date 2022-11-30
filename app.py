#importa la libreria de flask
from flask import Flask, render_template, request, flash, session, redirect
from config import config
#creamos una instacia de flask
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
import os
from werkzeug.utils import escape, secure_filename
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
from models.ModelTeams import ModelTeams
from models.ModelGroups import ModelGroups
from models.ModelPlayer import ModelPlayer
from models.ModelGame import ModelGame

#entities
from models.entities.User import Users




app = Flask(__name__)
Login_Manager_app=LoginManager(app)
db=MySQL(app)
global Type, comentario, Online 
Type=0
comentario =0
Online=0

@Login_Manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)


@app.route("/", methods=["GET", "POST"])
def home():    
    global Type
    TablaA=ModelTable.positionA(db)   
    print(TablaA)         
    TablaB=ModelTable.positionB(db)            
    TablaC=ModelTable.positionC(db)            
    TablaD=ModelTable.positionD(db)              
    TablaE=ModelTable.positionE(db)              
    TablaF=ModelTable.positionF(db)              
    TablaG=ModelTable.positionG(db)              
    TablaH=ModelTable.positionH(db)                  
    return render_template("index.html", tableA=TablaA,tableB=TablaB,
        tableC=TablaC,tableD=TablaD,tableE=TablaE,tableF=TablaF,
        tableG=TablaG,tableH=TablaH, Type=Type)
    

@app.route("/Results", methods=["GET", "POST"])
def results():        
    global Type       
    return render_template("Results.html", Type=Type)

@app.route("/Register", methods=["GET", "POST"])
def register():    
    frm = Register()           
    if request.method=="POST":    
        user= Users(frm.cellphone.data, frm.username.data, frm.password.data, 0) 
        ModelArbitrator.create(db,user)  
        return redirect ("/logout")
    else:
        return render_template("register.html", frm=frm, Type=Type) 

@app.route("/live")
def live():
    global Type,comentario, Online    
    Online=ModelGame.Online(db)    
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
        Nation=ModelPlayer.Nation(db)
        arbitrator=ModelArbitrator.AllArbitrator(db)   
        stadium=ModelStadium.AllStadium(db)
        
        if request.method=="POST":                                                             
            if 'crear_arbitro' in request.form: 
                name=frm_arbitro.name.data
                country=frm_arbitro.country.data                
                ModelArbitrator.create(db,name,country) 
                return redirect ("/Config")               
            if 'crear_estadio' in request.form: 
                name=frm_estadio.name.data
                country=frm_estadio.country.data                
                capacidad=frm_estadio.capacidad.data  
                ModelStadium.create(db,name,country,capacidad) 
                return redirect ("/Config")        
            if 'crear_equipo' in request.form: 
                file = request.files['uploadFile'] 
                basepath= os.path.dirname (__file__)                                                                    
                newname="Temp"+".jpg"
                upload=os.path.join(basepath,'static/resources',newname)
                if(file.filename!=''):
                    file.save(upload)
                    Grupo=frm_equipos.group.data
                    Entrenador=frm_equipos.namen.data
                    Equipo=frm_equipos.nameeq.data
                    Id_Grupo=frm_equipos.numeq.data                    
                    ModelTeams.create(db,Id_Grupo, Equipo, upload, Grupo, Entrenador)                     
                    ModelGroups.create(db,Equipo,Grupo) 
                    return redirect ("/Config")     
            if 'crear_jugador' in request.form: 
                name=frm_jugador.namejug.data
                num=frm_jugador.numjug.data
                apellido=frm_jugador.apejug.data
                country=request.form["Nation"]                                
                ModelPlayer.create(db,name,apellido,country,num) 
                return redirect ("/Config")    
        return render_template("/admin/Config.html", 
            Arbitrator=arbitrator,Stadium=stadium, frm_arbitro=frm_arbitro, 
            frm_estadio=frm_estadio,frm_equipos=frm_equipos, frm_jugador=frm_jugador,
            Type=Type, Nation=Nation)
    else:
        return redirect ("/")

@app.route("/Edit", methods=["GET", "POST"])
@login_required
def edit():   
    if Type==3:             
        frm_estadio = Stadium()  
        frm_jugador = jugadores()
        frm_equipos= Equipos()
        frm_arbitro = Arbitrator()  
        Nation=ModelPlayer.Nation(db)
        arbitrator=ModelArbitrator.AllArbitrator(db)   
        stadium=ModelStadium.AllStadium(db)  
        Players=ModelPlayer.AllPlayer(db)  
        Teams,escudo=ModelTeams.AllTeams(db)
        print(escudo)
        
        if request.method=="POST":                                                             
            if 'editar_arbitro' in request.form: 
                id=frm_arbitro.Id.data     
                name=frm_arbitro.name.data
                country=frm_arbitro.country.data                
                ModelArbitrator.edit(db,id,name,country) 
                return redirect ("/Edit")    
            if 'delete_arbitro' in request.form: 
                id=frm_arbitro.Id.data                           
                ModelArbitrator.delete(db,id) 
                return redirect ("/Edit")     
            if 'editar_estadio' in request.form: 
                id=frm_estadio.Id.data   
                name=frm_estadio.name.data
                country=frm_estadio.country.data                
                capacidad=frm_estadio.capacidad.data  
                ModelStadium.edit(db,id,name,country,capacidad) 
                return redirect ("/Edit")      
            if 'delete_estadio' in request.form: 
                id=frm_estadio.Id.data                           
                ModelStadium.delete(db,id) 
                return redirect ("/Edit")       
            if 'editar_equipo' in request.form: 
                id=request.form["EqEdit"] 
                file = request.files['uploadFile'] 
                basepath= os.path.dirname (__file__)                                                                    
                newname="Temp"+".jpg"
                upload=os.path.join(basepath,'static/resources',newname)
                if(file.filename!=''):
                    file.save(upload)
                    Grupo=frm_equipos.group.data
                    Entrenador=frm_equipos.namen.data
                    Equipo=frm_equipos.nameeq.data
                    Id_Grupo=frm_equipos.numeq.data                    
                    ModelTeams.edit(db,id,Equipo,upload,Id_Grupo, Grupo,Entrenador)                     
                    ModelGroups.edit(db,id,Grupo,Equipo)             
                    return redirect ("/Edit")     
            if 'delete_equipo' in request.form: 
                id=request.form["EqDelete"]                              
                ModelTeams.delete(db,id) 
                return redirect ("/Edit") 
            if 'editar_jugador' in request.form: 
                id=frm_jugador.Id.data
                name=frm_jugador.namejug.data
                num=frm_jugador.numjug.data
                apellido=frm_jugador.apejug.data
                country=request.form["Nation"]                                
                ModelPlayer.edit(db,id,name,apellido,country,num) 
                return redirect ("/Edit")    
            if 'delete_jugador' in request.form: 
                id=frm_jugador.Id.data                          
                ModelPlayer.delete(db,id)
        return render_template("/admin/Edit.html", 
            Arbitrator=arbitrator,Stadium=stadium, frm_arbitro=frm_arbitro, 
            frm_estadio=frm_estadio,frm_equipos=frm_equipos, frm_jugador=frm_jugador,
            Type=Type, Nation=Nation, Players=Players, Teams=Teams, escudo=escudo)
    else:
        return redirect ("/")
   
@app.route("/Programming", methods=["GET", "POST"])
@login_required
def progamming():   
    if Type==3:       
        return render_template("/admin/Menu.html",Type=Type)
    else:
        return redirect ("/")
    
@app.route("/Comment", methods=["GET", "POST"])
@login_required
def comment():  
    global comentario, Type, Online
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
                AmarillaL=frm.AmarillaL.data
                AmarillaV=frm.Amarillav.data
                RojaL=frm.RojaL.data
                RojaV=frm.RojaV.data
                GolesL=frm.GolesL.data
                GolesV=frm.GolesV.data
                EsquinaL=frm.EsquinaL.data
                EsquinaV=frm.EsquinaV.data
                ArcoL=frm.ArcoL.data
                ArcoV=frm.ArcoV.data
                OffsideL=frm.OffsideL.data
                OffsideV=frm.OffsideV.data     
                Online=ModelGame.Online(db)                         
                ModelComentarios.new(db,comentario,comment)   
                ModelComentarios.update(db,Online, AmarillaL, AmarillaV,RojaL, RojaV,GolesL, GolesV, 
                EsquinaL, EsquinaV, ArcoL, ArcoV, OffsideL, OffsideV)  
                print("Holi")              
            if 'delete' in request.form: 
                comentario=0                                        
                ModelComentarios.clean(db) 
        return render_template("/commentator/comment.html",frm=frm,Type=Type)
    else:
        return redirect ("/")

@app.route("/data", methods=["GET"])
def data():        
    global Online
    data=ModelComentarios.last(db)            
    y = json.dumps(data)      
    return (y)


def status_401(error):
    return redirect ("/Login")

app.config.from_object(config['development'])
app.register_error_handler(401,status_401)
app.run()