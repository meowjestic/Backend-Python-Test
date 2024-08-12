from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Segitiga(BaseModel):
    angka: int

@app.get('/')
async def root():
    return {"message": "hello world"}

@app.post('/segitiga')
async def make_triangle(data: Segitiga):
    dataAngka = data.angka

    response = ""

    strAngka = str(dataAngka)
    lnAngka = len(strAngka)

    for i in range(lnAngka):
        zero = ""
        z = ""
        for idx,x in enumerate(strAngka):
            if(idx > i):
                break
            zero += "0"
            z = x
        response += z + zero + "<br>"
    
    return response

@app.post('/ganjil')
async def make_odd(data: Segitiga):
    dataAngka = data.angka
    response = ""

    for x in range(dataAngka + 1):
        if(x % 2 != 0):
            response += str(x)
            if(x+1 != dataAngka):
                response += ' ,'

    return response

@app.post('/prima')
async def make_prime(data: Segitiga):
    dataAngka = data.angka
    response = ""

    if(dataAngka < 2):
        return 'none'
    
    for x in range(dataAngka + 1):
        if(isPrime(x)):
            response += str(x)
            if(x+1 != dataAngka):
                response += ' ,'

    return response

def isPrime(num):
    if(num == 1 or num == 0):
        return False
    
    for x in range(2, num):
        if(num % x == 0):
            return False
        
    return True