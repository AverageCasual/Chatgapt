from typing import Union
import uvicorn
from fastapi import FastAPI,status,HTTPException
from models import uSER,mESSAGE


Users = []

app = FastAPI()
@app.post("/login")
def Login(Username,Psswd):
    for item in Users:
        if item.id == Username and Psswd == item.password:
            return True
    return False
@app.post("/register")
def CreateUser (Username,Apodo,Psswd):#Crea un objeto usuario con userID y username
    found = False
    for item in Users:
        if Username == item.id:
            found = True
    if not found:
        User = uSER(Username,Apodo,Psswd)
        Users.append(User)
        return User

@app.get("/get")
def GetMessage (Username):#regresa conversacion dependiendo del UserID
    for item in Users:
        if item.id == Username:
            return item.Conversation


@app.post("/send")
def SendMessage (Text,SenderUSN,ReceiverUSN):
    
    Sender:uSER = None
    Receiver:uSER = None
    for item in Users:#Guarda los objetos sender y receiver en una variable
        if item.id == SenderUSN:
            Sender = item
        if item.id == ReceiverUSN and ReceiverUSN != Sender.id:
            Receiver = item
    if Receiver in Sender.friends:
        if Receiver.id not in Sender.Conversation:
            Sender.Conversation[Receiver.id] = []
            Receiver.Conversation[Sender.id] = []
        Text = mESSAGE (Text,Sender.id,Receiver.id)
        Sender.Conversation [Receiver.id].append (Text)
        Receiver.Conversation [Sender.id].append (Text)
        return Sender.GetMessagesByID(ReceiverUSN), Receiver.GetMessagesByID(SenderUSN)
    return False
            
            
            
            
            
            
            
    # if Receiver.id not in Sender.Conversation:#Si no esta guardada crea una conversacion nueva
    #     Mensajes = []
    #     Text = mESSAGE (Text,Sender.id,Receiver.id)
    #     Mensajes.append (Text)
    #     Sender.Conversation [Receiver.id] = Mensajes
    #     Receiver.Conversation [Sender.id] = Mensajes
    # else:# si si esta guardada actualiza la conversacion
    #     Mensajes = Sender.Conversation [Receiver.id]
    #     Text = mESSAGE (Text,Sender.id,Receiver.id)
    #     Mensajes.append (Text)
    #     Sender.Conversation [Receiver.id] = Mensajes
    #     Receiver.Conversation [Sender.id] = Mensajes
@app.post("/add")
def Add_Friend(Username,Othername):
    for item in Users:#Guarda los objetos sender y receiver en una variable
        if item.id == Username:
            Sender = item
        if item.id == Othername and Othername!= Sender.id:
            Receiver = item

    if Receiver not in Sender.friends and Receiver not in Sender.blocked:
        Sender.friends.append (Receiver)
        Receiver.friends.append (Sender)
@app.post("/block")
def Block_Black_People(Username,Othername):
    for item in Users:#Guarda los objetos sender y receiver en una variable
        if item.id == Username:
            Sender = item
        if item.id == Othername and Othername!= Sender.id:
            Receiver = item

    if Receiver not in Sender.friends and Receiver not in Sender.blocked:
        Sender.blocked.append (Receiver)
        Receiver.blocked.append (Sender)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


#tarea
#hacer que el usuario cree su propia id y que ponga su apodo, tambien tratar de romperlo En el objeto tengas como atributo en sender name y el reciever name