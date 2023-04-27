import requests
from time import sleep
#http://localhost:8000/Registrarse?Username=facil2&Apodo=facilisimo2


def RegistrarUsuario (Nombre,Apodo,Contrasena):
    requests.post(f"http://localhost:8000/registrarse?Username={Nombre}&Apodo={Apodo}&Psswd={Contrasena}")
    return True

def Login (Username,Password):
    requests.post(f"http://localhost:8000/registrarse?Username={Username}&Psswd={Password}")
    return True

def ObtenerMensajes (USN):
    var9 = requests.post(f"http://localhost:8000/get?Username={USN}")
    return var9.json()

def EnviarMensaje (Texto,Nombre,Recibidor):
    var1 = requests.post(f"http://localhost:8000/send?Text={Texto}&SenderUSN={Nombre}&ReceiverUSN={Recibidor}")
    return var1.json()

def AnadirAmigo (Nombre,Recibidor):
    requests.post(f"http://localhost:8000/add?Username={Nombre}&Othername={Recibidor}")
    return True
def Bloquear (Nombre,Recibidor):
    requests.post(f"http://localhost:8000/block?Username={Nombre}&Othername={Recibidor}")
    return True
    
a= input(1-"login", 2-"Register")
if a == 1:
    Name= input("Identifiquese ")
    Contrasena = input("Ingrese contrasena ")
    Logged_In = Login(Name,Contrasena)
if a == 2:
    Name = input("Identifiquese ")
    Apodaca = input ("Identifiquese pero con el nombre tonto que eligio para sobrenombre ")
    Password = input ("Eliga Contrasena")
    if RegistrarUsuario(Name,Apodaca,Password):
        Logged_In = True
    
if Logged_In:
    while True:
        inpot = int(input("Que quiere realizar\n 1=Obtener Mensajes\n2=Enviar Mensaje\n3=Anadir Amigo\n4=Bloquear Persona\n5=Salir\n"))

        if inpot == 2:
            var2= input("A quien quiere enviarle mensaje ")
            var3 = input("Ingrese su mensaje: ")
            var4 = EnviarMensaje(var3,Name,var2)
            print(var4)
        if inpot == 3:
            var5=input("ingrese username de su amigo")
            AnadirAmigo(Name,var5)
        if inpot == 4:
            var6=input("A quien quiere bloquear")
            Bloquear(Name,var6)
        if inpot == 5:
            break
else:
    print("No se ha podido logear in")