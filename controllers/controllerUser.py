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
            return created_User

    def readUser(self) -> None:
        read_User = UserModel.Users(self.params).readUserDB()
        if(read_User):
            return 'OK'
    def updateUser(self) -> None:
        update_User = UserModel.Users(self.params).updateUserBD()
        if(update_User):
            return 'OK'
    def deleteUser(self) -> None:
        delete_User = UserModel.Users(self.params).deleteUserBD()
        if(delete_User):
            return 'OK'
    def loginUser(self)-> None:
        login_User = UserModel.Users(self.params).selectUserForLogin()
        
        if(login_User != []):
            return ['OK',login_User]
        
    
        
        
        



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