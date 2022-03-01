from fastapi import FastAPI
from fastapi.responses import FileResponse
import requests
from io import BytesIO
from zipfile import ZipFile
import json
from pydantic import BaseModel
from typing import Optional

class Charac(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    gender: Optional[str] = None
    download: Optional[str] = None


app = FastAPI()

def get_char(query_params):
    r = requests.get('https://rickandmortyapi.com/api/character' + query_params)
    return r.json()


def zip_a_file(file):
    with ZipFile('res.zip', 'w') as zipObj:
        zipObj.write('json_data.json')

 
@app.get("/trii")
def read_root(charac: Charac):

    

    query_params_string = str()

    if charac.name:
        query_params_string = query_params_string + "name=" + charac.name + "&"
    if charac.status:
        query_params_string = query_params_string + "status=" + charac.status + "&"
    if charac.gender:
        query_params_string = query_params_string + "gender=" + charac.gender

    if query_params_string:
        query_params_string = "/?" + query_params_string

    res = get_char(query_params_string)
    

    if charac.download:
        with open('json_data.json', 'w') as outfile:
            json.dump(res, outfile)
        zip_a_file('json_data.json')
        return FileResponse("res.zip")

    
    return res