import csv

class CategorieService:
    path_db_table_categories = "/home/matheus/estudos/fastAPI_estudo/db/db_table_categories.csv"
    
    fields = ["id", "name"]
    
    @staticmethod
    def get_all_categories() -> list:
        try:
            with open(CategorieService.path_db_table_categories, newline= '' , mode='r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
            
                return list(reader)
            
        except csv.Error as e:
            print(f"Error no arquivo {file} na linha {reader.line_num}: {e}")
        
        
    @staticmethod
    def create_categorie(categorie):
        try:
            with open(CategorieService.path_db_table_categories, newline='', mode='a', encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=CategorieService.fields)
                writer.writerow(categorie)
        except csv.Error as e:
            print(f"Error no arquivo {file} na linha {writer.line_num}: {e}")