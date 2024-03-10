from pydantic import BaseModel
class User(BaseModel):
    nombre: str
    apellido: str
    documento: str
    edad: int
    salario: int
    