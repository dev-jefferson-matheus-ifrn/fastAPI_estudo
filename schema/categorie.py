from pydantic import BaseModel

class Categorie(BaseModel):
    id: int
    name: str