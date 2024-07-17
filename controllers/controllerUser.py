import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)
import UserModel



class User():
    
    def __init__(self,params) -> None:
        
       self.params = params
    
    def createUser(self) -> None:
        
        createdUser = UserModel.Users(self.params).createUserDB()
        if(createdUser):
            print('User Criado!!!')
        
        



params = {
    "nome": "leo2",
    "email": "leocarminhot1aaa11o@gmail.com",
    "senha": "leozinho"
}

User(params).createUser()
