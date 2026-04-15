from fastapi import FastAPI, status
import random
from dismissal_model import Dissmissal

fake_db_dismissals = []

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}


# Path Parameter - Exemplo
@app.get("/api/categories/{categories}", status_code=status.HTTP_200_OK)
def read_categories(categories):
    return [{"name_categorie": f"{categories}", "dismissal": 130}]

# Path Parameter - Exemplo 2
@app.get("/api/dismissal/{month}", status_code=status.HTTP_200_OK)
def read_month_dismissals(month):
    month_dismissals = [dismissal for dismissal in fake_db_dismissals if dismissal["month"] == month]
    
    return month_dismissals
   
            
# Metodo HTTP POST/Request Body
@app.post("/api/dismissal", status_code=status.HTTP_201_CREATED)
def create_dismissal(dismissal: Dissmissal):
    fake_db_dismissals.append(dismissal.model_dump())
    return dismissal
    
    
# Metodo HTTP GET
@app.get("/api/dismissals", status_code=status.HTTP_200_OK)
def get_all_dismissals():
    return fake_db_dismissals