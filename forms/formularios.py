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
    country= SelectField("Procedencia", choices=[("1","Alemania"),("2","Argentina"),("3","Belgica"),("4","Brasil"),
        ("5","Francia"),("6","Japon"),("7","Mexico"),("8","Polonia")])            
    crear_arbitro = SubmitField("Introducir nuevo Arbitro")        
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
    delete_estadio = SubmitField("Eliminar Estadio")     
