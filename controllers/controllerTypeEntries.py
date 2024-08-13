import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models'))
sys.path.append(module_path)
import TypeEntriesModel

class TypeEntriesController:
    
    def __init__(self,params) -> None:
        
        self.params = params

    def createTypeEntries(self)-> str:
        createtype = TypeEntriesModel.TypeEntries(self.params).createTypeEntrie()
        if(createtype == "OK"):
            return "OK"
        
    def selectAllTypeEntries(self)-> str:
        selectAlltypes = TypeEntriesModel.TypeEntries(self.params).createTypeEntrie()
        if(selectAlltypes=="OK"):
            return "OK"