from typing import Annotated
from fastapi import APIRouter, Cookie, status, Header
from services.dismissal_service import DismissalService
from schema.dismissal_model import Dissmissal, DissmissalOutput

fake_db_dismissals = []

router = APIRouter(prefix="/api")

@router.get("/", status_code=status.HTTP_200_OK)
def read_root(user_agent: Annotated[str | None, Header()]=None):
    print(f"User_agent: {user_agent}")
    return {"Message": "Hello World"}


# Metodo HTTP GET - Status Code 200
@router.get("/dismissals",status_code=status.HTTP_200_OK, response_model=list[DissmissalOutput])
def get_all_dismissals():
    return DismissalService.get_all_dismissals()

# Metodo HTTP Post - Status Code 201
@router.post("/dismissal", status_code=status.HTTP_201_CREATED)
def create_dismissal(dismissal: Dissmissal):
    DismissalService.create_dissmissal(dismissal.model_dump())

# Metodo HTTP Get - Status Code 200
# Cookie Parameter
# Path Parameter
@router.get("/dismissal/{month}", status_code=status.HTTP_200_OK, response_model=list[DissmissalOutput])
def get_month_dismissals(month, ads_id: Annotated[str | None, Cookie()] = "93y8rh8h2"):
    dissmissals_by_month = DismissalService.get_all_by_month(month)
    print(f"Cookie:{ads_id}")
    return dissmissals_by_month
    

# Metodo HTTP Get - Status Code 200
# Path Parameter
@router.get("/dismissal/{categorie}", status_code=status.HTTP_200_OK)
def get_dismissals_by_categorie(categorie):
    
    dissmissals = [dismissal for dismissal in fake_db_dismissals if dismissal["categorie"] == categorie]
    
    return dissmissals