from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from typing import Optional

app = FastAPI() #Crea una instancia de la clase FastAPI 
app.title = "Mi aplicación de películas favoritas con FastAPI"
app.version = "0.0.1"


movies_list = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "overview": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "year": "1994",
        "rating": "9",
    },
    {
        "id": 2,
        "title": "The Godfather",
        "overview": "An organized crime dynasty's aging patriarch transfers control of his clandestine empire to his reluctant son.",
        "year": "1972",
        "rating": "9",
    },
    {
        "id": 3,
        "title": "Inception",
        "overview": "A thief who steals corporate secrets through dream-sharing technology is tasked with planting an idea into the mind of a CEO.",
        "year": "2010",
        "rating": "8.8",
    },
    {
        "id": 4,
        "title": "Interstellar",
        "overview": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "year": "2014",
        "rating": "8.6",
    },
    {
        "id": 5,
        "title": "Blade Runner 2049",
        "overview": "Young Blade Runner K's discovery of a long-buried secret leads him to track down former Blade Runner Rick Deckard.",
        "year": "2017",
        "rating": "8",
    },
    {
        "id": 6,
        "title": "The Matrix",
        "overview": "A computer hacker learns about the true nature of his reality and his role in the war against its controllers.",
        "year": "1999",
        "rating": "8.7",
    },
    {
        "id": 7,
        "title": "Star Wars: Episode IV - A New Hope",
        "overview": "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, and two droids to save the galaxy.",
        "year": "1977",
        "rating": "8.6",
    },
    {
        "id": 8,
        "title": "The Fifth Element",
        "overview": "In the colorful future, a cab driver unwittingly becomes the central figure in the search for a legendary cosmic weapon.",
        "year": "1997",
        "rating": "7.6",
    },
    {
        "id": 9,
        "title": "Arrival",
        "overview": "A linguist works with the military to communicate with alien lifeforms after twelve mysterious spacecraft appear around the world.",
        "year": "2016",
        "rating": "7.9",
    },
    {
        "id": 10,
        "title": "Dune",
        "overview": "A young nobleman becomes embroiled in a battle for control of a desert planet and its valuable resource, spice.",
        "year": "2021",
        "rating": "8.3",
    },
    {
        "id": 11,
        "title": "Ex Machina",
        "overview": "A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence.",
        "year": "2014",
        "rating": "7.7",
    },
    {
        "id": 12,
        "title": "Gravity",
        "overview": "Two astronauts work together to survive after an accident leaves them stranded in space.",
        "year": "2013",
        "rating": "7.7",
    }
]

@app.get('/', tags=["Home"])#Definimos una ruta
def message(): # Definimos una función de la ruta
    return HTMLResponse('<h1>Hello world</h1>') # Devolvemos un string en la respuesta de la ruta

@app.get('/movies', tags=["Movies"]) #Definimos una ruta de la clase FasAPI
def get_movies():
    return movies_list

@app.get('/movies/{id}', tags=["Movies"]) #Definimos una ruta de la clase FasAPI
def get_movie(id: int):
    for item in movies_list:
        if item['id'] == id:
            return item 
        return item
    return []

#Tokenizar

@app.post("/tokenize") # Decorador para indicar que es una ruta de la API
def tokenize(text:str): # Funcion que retorna un mensaje
    return preprocessar(text)

 

def preprocessar(text):
    import json  # Importamos la librería json para trabajar con archivos json
    from nltk.tokenize import word_tokenize
    import nltk
    nltk.download('punkt')
    tokens = word_tokenize(text)
    result = {word: True for word in tokens}
    print(result)
    return JSONResponse(content={"message":result})
                        



#para correr la app: uvicorn main:app --reload
#uvirconr nombreApp:app --reload --port 5000
# http://127.0.0.1:8000/docs
#Commit: Abordamos hasta la sesion 2 Slide 37