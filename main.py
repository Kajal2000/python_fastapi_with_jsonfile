from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

import json 
import os

app = FastAPI()

# Get all data from json file
@app.get("/Api")
def read_root():
        with open("main.json","r") as file:
            read_data = file.read()
            data_lode = json.loads(read_data)
        return (data_lode)

# # Post data into json file
class Item(BaseModel):
    name: str
    description: Optional[str]

@app.post("/items/")
async def create_item(item: Item):
    with open("main.json","r") as file:
        read_data = file.read()
        data_lode = json.loads(read_data)
        id = len(data_lode)
        data = {
            "id": id+1,
            "name" : item.name,
            "description" : item.description
        }
        data_lode.append(data)
        # print(data_lode)
        with open("main.json", "w") as outfile: 
            json.dump(data_lode, outfile) 

#  update your data from json file
@app.put("/items/{id}")
async def create_item(id : int ,item: Item):
    # print(id)
    with open("main.json","r") as file:
        read_data = file.read()
        data_lode = json.loads(read_data)
        index = (data_lode[id-1])
        data_lode.pop(id-1)
        index = {
            "id" :id,
            "name" : item.name,
            "description" : item.description
        }
        data_lode.append(index)
        print(data_lode)
        with open("main.json", "w") as outfile: 
            json.dump(data_lode, outfile) 


# Delete the data from json file
@app.delete("/items/{id}")
async def create_item(id : int ,item: Item):
    with open("main.json","r") as file:
        read_data = file.read()
        data_lode = json.loads(read_data)
        i = 0
        while i <len(data_lode):
            if data_lode[i]["id"] == id:
                data_lode.pop(id-1)
                break
            i = i + 1
        with open("main.json", "w") as outfile: 
            json.dump(data_lode, outfile) 
        