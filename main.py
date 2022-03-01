from fastapi import FastAPI
import requests


app = FastAPI()

def get_char():
    r = requests.get('https://rickandmortyapi.com/api/character')
    return r.json()

 
@app.get("/trii")
def read_root():

    res = get_char()
    
    return res