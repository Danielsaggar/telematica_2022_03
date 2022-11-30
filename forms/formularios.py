from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length

class Login(FlaskForm):
    username = StringField("Usuario", validators=[
        DataRequired(message="Usuario es obligartorio")])
    password = PasswordField("Contraseña", validators=[
        DataRequired(message="Password es obligatorio")])
    entrar = SubmitField("Entrar")
    invitado = SubmitField("Invitado")

class Register(FlaskForm):
    username = StringField("Usuario", validators=[
        DataRequired(message="Usuario es obligartorio")])
    password = PasswordField("Contraseña", validators=[
        DataRequired(message="Password es obligatorio")])
    cellphone = IntegerField("Celular", validators=[
        DataRequired(message="Celular es obligartorio"),Length(min=10, max=10)])
    crear = SubmitField("Crear")    

class Arbitrator(FlaskForm):
    name = StringField("Nombre", validators=[
        DataRequired(message="Usuario es obligartorio")])    
    Id = IntegerField("Id", validators=[
        DataRequired(message="Id es obligartorio")])
    country= SelectField("Procedencia", choices=[("Alemania"),("Argentina"),("Belgica"),("Brasil"),
        ("Francia"),("Japon"),("Mexico"),("Polonia")])            
    crear_arbitro = SubmitField("Introducir nuevo Arbitro")        
    editar_arbitro = SubmitField("Editar Arbitro")  
    delete_arbitro = SubmitField("Eliminar Arbitro")        

class Stadium(FlaskForm):
    name = StringField("Nombre", validators=[
        DataRequired(message="Usuario es obligartorio")])
    capacidad = IntegerField("Capacidad", validators=[
        DataRequired(message="capacidad es obligartorio")])
    Id = IntegerField("Id", validators=[
        DataRequired(message="Id es obligartorio")])
    country= SelectField("Procedencia", choices=[("Alemania"),("Argentina"),("Belgica"),("Brasil"),
        ("Francia"),("Japon"),("Mexico"),("Polonia")])            
    crear_estadio = SubmitField("Introducir nuevo Estadio")     
    editar_estadio = SubmitField("Editar Estadio")           
    delete_estadio = SubmitField("Eliminar Estadio")     

class commentator(FlaskForm):
    comment = StringField("Comentario: ", validators=[
        DataRequired(message="Usuario es obligartorio")])           
    create = SubmitField("Nuevo comentario: ")        
    delete = SubmitField("Eliminar ")    
    
class Equipos(FlaskForm):
    Id = IntegerField("Id", validators=[
        DataRequired(message="Id es obligartorio")])
    group=SelectField("Grupo", choices=[("A"),("B"),("C"),("D"),("E"),("F"),("G"),("H")])
    numeq=SelectField("Numero de equipo", choices=[("1"),("2"),("3"),("4")])
    nameeq =StringField("Nombre del equipo",validators=[
        DataRequired(message="Nombre del equipo es obligartorio")] )
    namen =StringField("Nombre del entrenador",validators=[
        DataRequired(message="Nombre del equipo es obligartorio")] )
    crear_equipo = SubmitField("Crear nuevo equipo")
    editar_equipo = SubmitField("Editar equipo")
    delete_equipo = SubmitField("Eliminar equipo")

class jugadores(FlaskForm):    
    Id = IntegerField("Id", validators=[
        DataRequired(message="Id es obligartorio")])
    numjug=SelectField("Numero del jugador ", choices=[("1"),("2"),("3"),("4"),("5"),("6"),("7"),("8"),("9"),("10"),("11")])
    namejug =StringField("Nombre del jugador",validators=[
        DataRequired(message="Nombre del jugador es obligartorio")] )
    apejug =StringField("Apellido  del jugador",validators=[
        DataRequired(message="Apellido del jugador es obligartorio")] )
    crear_jugador = SubmitField("Introducir nuevo jugador")    
    editar_jugador = SubmitField("Editar jugador")    
    delete_jugador = SubmitField("Eliminar jugador")    

