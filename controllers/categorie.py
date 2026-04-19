from fastapi import APIRouter, status
from schema.categorie import Categorie
from services.categorie_service import CategorieService

router = APIRouter(prefix="/api")


@router.post("/categorie", status_code=status.HTTP_201_CREATED)
def create_categorie(categorie: Categorie):
    CategorieService.create_categorie(categorie.model_dump())
    

@router.get("/categories", status_code=status.HTTP_200_OK)
def get_all_categories():
    return CategorieService.get_all_categories()