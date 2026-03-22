from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Livro(BaseModel):
    titulo: str
    autor: str
    ano: int
    genero: str


livros = []

@app.post("/livros")
def cadastro(livro: Livro):
    livros.append(livro)
    return {"msg": "Livro cadastrado com sucesso"}

@app.get("/livros")
def mostrar():
    if livros:
        return livros
    else:
        return {"msg": "não tem livros"}