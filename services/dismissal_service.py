import csv
from services.categorie_service import CategorieService
class DismissalService:
    
    path_db_table_dissmissal = "/home/matheus/estudos/fastAPI_estudo/db/db_table_dismissal.csv"
    
    fields = ["id", "value", "month", "id_categorie"]
    
        
    @staticmethod
    def get_all_dismissals() -> list:
        
        with open(DismissalService.path_db_table_dissmissal, newline= '' , mode='r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            return list(reader)
            
        
        
    @staticmethod
    def create_dissmissal(dismissal):
        cateogies = CategorieService.get_all_categories()
        with open(DismissalService.path_db_table_dissmissal, newline='', mode='a', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=DismissalService.fields)
            
            for categorie in cateogies:
                if str(dismissal["id_categorie"]) == str(categorie["id"]):
                    writer.writerow(dismissal)
                    break