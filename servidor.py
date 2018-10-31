from flask import Flask, request
import mysql.connector
from usuario import Usuario

conexion = mysql.connector.connect(user="kevin",password="12345",database="invernadero")
cursor = conexion.cursor()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

#/login/?usuario=nombre&password=contraseña
@app.route("/login/", methods=['GET'])
def login():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    
    userBD = Usuario(conexion, cursor)
    print(userBD.login(usuario, password))
    
    print(usuario, password)
#    print(request.args)
    return usuario + " " + password

app.run(debug=True)
