from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}


# Query Parameter - Exemplo
@app.get("/api/{categories}")
def read_categories(categories):
    return [{"name_categorie": f"{categories}", "dismissal": 130}]

# Query Parameter - Exemplo 2
@app.get("/api/dismissal/{month}")
def read_month_dismissals(month):
    dismissals = [random.randint(50, 450) for _ in range(3)]
    return {"name_month" : f"{month}", "dismissals": dismissals}