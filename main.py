from fastapi import FastAPI
from controllers.dismissal import router as dismissal_router
from controllers.categorie import router as categories_router
app = FastAPI()

app.include_router(dismissal_router)
app.include_router(categories_router)


    