from fastapi import FastAPI, Header, Response, status, Cookie
from typing import Annotated
from dismissal_model import Dissmissal

fake_db_dismissals = []

app = FastAPI()

@app.get("/")
# Head Parameter
def read_root(user_agent: Annotated[str | None, Header()] = None):
    print(f"User Agent: {user_agent}")
    return {"message": "Hello World!"}


# Path Parameter - Exemplo
@app.get("/api/categories/{categories}", status_code=status.HTTP_200_OK)
def read_categories(categories):
    return [{"name_categorie": f"{categories}", "dismissal": 130}]

# Path Parameter - Exemplo 2
@app.get("/api/dismissal/{month}", status_code=status.HTTP_200_OK)
def read_month_dismissals(response:Response,month, ads_id: Annotated[str | None, Cookie()] = None):
    
    month_dismissals = [dismissal for dismissal in fake_db_dismissals if dismissal["month"] == month]
    # Cookie Parameter
    # Setar um Cookie
    response.set_cookie(key="User_Session", value="2uhf8u8uhe8uf8")
    
    # Ler um Cookie
    print(f"Cookie: {ads_id}")
    
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