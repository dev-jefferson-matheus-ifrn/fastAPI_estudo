import csv
from services.categorie_service import CategorieService
class DismissalService:
    
    path_db_table_dissmissal = "/home/matheus/estudos/fastAPI_estudo/db/db_table_dismissal.csv"
    
    fields = ["id", "value", "month", "id_categorie"]
    
        
    @staticmethod
    def get_all_dismissals() -> list:
        all_categories = {str(cat["id"]): cat["name"] for cat in CategorieService.get_all_categories()}
        all_dismissals = []
        with open(DismissalService.path_db_table_dissmissal, newline= '' , mode='r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                categorie_id = row["id_categorie"]
                if categorie_id in all_categories:
                    row["name_categorie"] = all_categories[categorie_id]
                    
                all_dismissals.append(row)
            
            return all_dismissals
            
                
              
    @staticmethod
    def create_dissmissal(dismissal):
        cateogies = CategorieService.get_all_categories()
        with open(DismissalService.path_db_table_dissmissal, newline='', mode='a', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=DismissalService.fields)
            
            for categorie in cateogies:
                if str(dismissal["id_categorie"]) == str(categorie["id"]):
                    writer.writerow(dismissal)
                    break
                
                
    @staticmethod
    def get_all_by_month(month) -> list:
        all_dismissals = DismissalService.get_all_dismissals()
        dissmissals_filtred = []
        
        for dismissal in all_dismissals:
            if dismissal["month"] == month:
                dissmissals_filtred.append(dismissal)
                
        return dissmissals_filtred
    
    @staticmethod
    def get_all_by_categorie(categorie_name) -> list:
        all_dismissals = DismissalService.get_all_dismissals()
        dissmissals_filtred = []
        
        print(all_dismissals)
        for dismissal in all_dismissals:
            if dismissal["name_categorie"] == categorie_name:
                dissmissals_filtred.append(dismissal)
                
        return dissmissals_filtred
        
        
        