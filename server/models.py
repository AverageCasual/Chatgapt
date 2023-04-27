
import time
class uSER ():
    def __init__(self,Username,Apodo,Psswd) -> None:
        self.id = Username
        self.password = Psswd
        self.name = Apodo
        self.friends = []
        self.blocked = []
        self.Conversation = {}#Key = user.id, value lista de mensajes
    def CheckFriendByID(self,Name):
        for item in self.friends:
            if item.name == Name:
                return item.id
    def GetMessagesByID(self,ID):
        if ID in self.Conversation:
            return self.Conversation[ID]
        return False


#class Conversation
#Clase message depende de User
class mESSAGE ():
    def __init__(self,text,sender,receiveration) -> None:#sender y receiver son ids
        self.text = text
        self.time = time.time()
        self.sender = sender
        self.receiver = receiveration