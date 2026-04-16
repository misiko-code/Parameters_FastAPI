from fastapi import FastAPI
from enum import Enum

#Creating Enum class
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

#Query parameters and string path parameters
fake_item_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Abend, Ich bin eine coole App!"}

#path parameter and query parameter conversion
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None, short: bool = False): #q is an optional query parameter,with default value of None 
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
            )
    return item

#Usage of Enum class
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}     
#Usage of query parameters and string path parameters
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_item_db[skip : skip + limit]

#multiple path parameters & required query parameters
@app.get("/users/{user_id}/items/{item_id}")# the order of declaration doesn't matter, but the path parameters must be declared in the same order as they appear in the path
async def read_user_item(user_id: int, item_id: str, needy: str, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id, "needy": needy}
    if needy:
        item.update({"needy": needy})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
            )
    return item


