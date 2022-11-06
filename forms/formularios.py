from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    username = StringField("Usuario", validators=[
        DataRequired(message="Usuario es obligartorio")])
    password = PasswordField("Contraseña", validators=[
        DataRequired(message="Password es obligatorio")])
    entrar = SubmitField("Entrar")

class Ingresos(FlaskForm):
    id_producto = StringField("id producto")
    nombre = StringField("Modelos")
    descripcion = StringField("Descripcion")
    fecha = DateField("Fecha de ingreso")
    stock =IntegerField("cantidad a ingresar")
    min =IntegerField("cantidad mínima en inventario")
    proveedor =SelectField("proveedor", choices=[()])
    agregar_linea_existente = SubmitField("agregar linea existente")
    agregar_nueva_linea = SubmitField("agregar nueva linea")
    
class Salidas(FlaskForm):
    id_producto = StringField("id producto")
    nombre = StringField("nombre")
    fecha = DateField("Fecha de ingreso")
    cantidad =IntegerField("cantidad a ingresar")       
    guardar = SubmitField("guardar")

class Usuarios(FlaskForm):
    #tipo_usuario = StringField("tipo usuario")
    username = StringField("username")
    password = PasswordField("Password")       
    guardar = SubmitField("guardar")
    rol= SelectField("Roles", choices=[("1", "Usuario final"),("2", "Admin"), ("3", "Super admin")])

class UsuariosF(FlaskForm):
    #tipo_usuario = StringField("tipo usuario")
    username = StringField("username")
    password = PasswordField("Password")       
    guardar = SubmitField("guardar")
    rol= SelectField("Roles", choices=[("1", "Usuario final")])

class Proveedores(FlaskForm):
    nit = StringField("nit")
    nombre = StringField("nombre")
    guardar = SubmitField("guardar")
    
class Celulares(FlaskForm):
    id_celulares = StringField("Modelo celular")
    nombre = StringField("nombre")
    stock = StringField("stock")
    Buscar = SubmitField("Buscar")
    min = SubmitField("Debajo del mínimo")

class g_prov(FlaskForm):
    nit= StringField("NIT")
    name = StringField("Nombre")
    edit = SubmitField("Actualizar")
    delete = SubmitField("Eliminar")
    Crear = SubmitField("Crear")

class g_usuario(FlaskForm):
    id= StringField("id")
    name = StringField("Nombre")
    rol= SelectField("Roles", choices=[("1", "Usuario final"),("2", "Admin"), ("3", "Super admin")])
    password = PasswordField("Contraseña")
    delete = SubmitField("ELIMINAR")
    search = SubmitField("BUSCAR")
    edit = SubmitField("ACTUALIZAR")

class g_usuarioF(FlaskForm):
    id= StringField("id")
    name = StringField("Nombre")
    rol= SelectField("Roles", choices=[("1", "Usuario final")])
    password = PasswordField("Contraseña")
    delete = SubmitField("ELIMINAR")
    search = SubmitField("BUSCAR")
    edit = SubmitField("ACTUALIZAR")