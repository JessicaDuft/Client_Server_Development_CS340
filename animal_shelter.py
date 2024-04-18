from pymongo import MongoClient
from bson.objectid import ObjectId


    
class AnimalShelter (object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30228
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("SUCCESS - accessed database")
        # Complete this create method to implement the C in CRUD
    
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data) # Data should be a dictionary
            print("animal added succesfully")
            return True
        else:
            raise Exception("Nothing to save due to parameter being empty")
            
            
            # Complete this create method to implement the R in CRUD

    def read(self, search=None):
        if search is not None:
            data = self.database.animals.find_one(criteria,{"_id": False})
            for document in data:
                print(document)
            
        else:
            data = self.database.animals.find_one({},{"_id": False})
        
        return data
    
   # Create method to implement the R in CRUD.
    def read_all(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria,{"_id": False})
            
           # for document in data:
              #  print(document)
            
        else:
            data = self.database.animals.find({},{"_id": False})
            
            
        
        return data

    
    
    # Create method to implement the U in CRUD.
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit = 1) != 0:
                update_result = self.database.animals.update_many(initial, {"$set": change})
                result = update_result.raw_result
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to update, because data parameter is empty")

    # Create method to implement the D in CRUD.
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Nothing to delete, because data parameter is empty")