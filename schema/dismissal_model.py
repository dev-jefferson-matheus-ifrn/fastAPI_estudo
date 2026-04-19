from pydantic import BaseModel

class Dissmissal(BaseModel):
    id: int
    value: float
    month: str
    id_categorie: int | None