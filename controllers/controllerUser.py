import sys
import os
import json
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)
import UserModel



class User():
    
    def __init__(self,params) -> None:
        
       self.params = params
    
    def createUser(self) -> None:
        created_User = UserModel.Users(self.params).createUserDB()
        if(created_User):
            print('User Criado!!!')
            return 'OK'
    def updateUser(self) -> None:
        update_User = UserModel.Users(self.params).updateUserBD()
        if(update_User):
            print("User Alterado!!")
    def deleteUser(self) -> None:
        delete_User = UserModel.Users(self.params).deleteUserBD()
        if(delete_User):
            print("User Deletado!!")
    
        
        
        



# params = {
#     "nome": "leo",
#     "email": "leocarminhoto@gmail.com",
#     "senha": "leozinho",
#     "id": 1
# }
# print(type(params))
# User(params).createUser()
# User(params).updateUser()
# User(params).deleteUser()