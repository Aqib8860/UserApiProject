from server.settings import clientOpen
from bson.json_util import dumps, loads
import json
from bson import json_util



class User:

    def __init__(self):
        self.client = clientOpen()

    def create(self, id, email, first_name, last_name, company_name, city, state, zipcode, web, age):
        self.client.mydb.truevalue.insert_one({
            "id":id,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "company_name": company_name,
            "city": city,
            "state": state,
            "zip": zipcode,
            "web": web,
            "age": age,

        })
        self.client.close()

    def get(self, user_id):
        #id = int(user_id)
        res = json.loads(json_util.dumps(self.client.mydb.truevalue.find_one({"id":user_id})))
        self.client.close()
        return res


    def update(self, user_id, first_name, last_name, age):
        if self.client.mydb.truevalue.find_one({"id":user_id}):
            self.client.mydb.truevalue.update_one({"id":user_id},{
                "$set":{
                    "first_name":first_name,
                    "last_name":last_name,
                    "age":age,
                }
            })
            return "Update Success"
        else:
            return "No User Found"

        self.client.close()

    def delete(self, user_id):
        if self.client.mydb.truevalue.find_one({"id":user_id}):
            self.client.mydb.truevalue.delete_one({"id":user_id})
            return "Delete Success"
        else:
            return "No User Found"

        self.client.close()

    def getUsers(self):
        res = json.loads(json_util.dumps(self.client.mydb.truevalue.find()))
        self.client.close()
        return res

    def getLimitedData(self,limit):
        limit = int(limit)
        res = json.loads(json_util.dumps(self.client.mydb.truevalue.find().limit(limit)))
        self.client.close()
        return res

    def sortNameData(self, name):
        res = json.loads(json_util.dumps(self.client.mydb.truevalue.find({"first_name": {"$regex":name, "$options":"i"}})))
        return res

    def getSortData(self,sort):
        res = json.loads(json_util.dumps(self.client.mydb.truevalue.find().sort(sort, 1)))
        self.client.close()
        return res

    def close(self):
        self.client.close()
