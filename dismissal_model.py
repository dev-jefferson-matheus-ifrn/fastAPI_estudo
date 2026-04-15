from pydantic import BaseModel

class Dissmissal(BaseModel):
    value: float
    month: str