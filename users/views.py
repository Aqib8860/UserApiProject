from starlette.responses import JSONResponse
from .models import User
from starlette_core.paginator import Paginator
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request

async def getUsers(request):

    try:
        user = User()

        if request.method=="POST":
            data = await request.json()

            user.create(
                data["id"],
                data["email"],
                data["first_name"],
                data["last_name"],
                data["company_name"],
                data["city"],
                data["state"],
                data["zip"],
                data["web"],
                data["age"]
            )
            
            return JSONResponse({"message":"User Created","status":True, "status_code":201},status_code=201)
        
        if request.query_params:
            if request.query_params.get("limit"):
                limit =  request.query_params.get("limit")
                data = user.getLimitedData(limit)

            if request.query_params.get("name"):
                name =  request.query_params.get("name")
                data = user.sortNameData(name)

            if request.query_params.get("sort"):
                sort =  request.query_params.get("sort")
                data = user.getSortData(sort)

        
        else:
            data = user.getUsers()

        return JSONResponse({"message":"Success","data":data,"status":True, "status_code":200}, status_code=200)

    except Exception as e:

        return JSONResponse({"message":str(e),"status":False}, status_code=400)


async def getUser(request):
    try:
        if request.method=="GET":
            user = User()
            user_id = request.path_params["user_id"]
            #user_id = request.query_params.get("user_id")

            data = user.get(user_id)
            return JSONResponse({"data": data,"status":True, "status_code":200},status_code=200)
        
        if request.method=="PUT":
            user_id = request.path_params["user_id"]
            data = await request.json()
            
            user = User()
            data = user.update(user_id, data["first_name"], data["last_name"], data["age"])

            return JSONResponse({"message":data, "status":True, "status_code":200},status_code=200)

        if request.method=="DELETE":
            user_id = request.path_params["user_id"]
            
            user = User()
            data = user.delete(user_id)

            return JSONResponse({"message":data, "status":True, "status_code":200},status_code=200)

    except Exception as e:
        return JSONResponse({"message":str(e),"status":False}, status_code=400)


"""async def get(self, request:Request):
        try:
            user = User()
            #limit = request.path_params["limit"]
            limit = request.query_params.get("limit")
            print(limit)
            data = user.getLimitedData(limit)
            
            return JSONResponse({
                "message":"Success",
                "data":data,
                "status":True, "status_code":200}, status_code=200)

        except Exception as e:

            return JSONResponse({"message":str(e),"status":False}, status_code=400)

"""