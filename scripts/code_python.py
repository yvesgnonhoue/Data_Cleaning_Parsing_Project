#Mon code python
import re
import pandas as pd

Chemin_fichier = "C:/Users/utilisateur/Data_Cleaning_Parsing_Project/data/fichier_desordonne/raw_data_logs.txt"
def importation_fichier():
    # la lecture du fichier en le mettant dans texte
    with open(Chemin_fichier, "r", encoding="utf-8") as f:
        texte = f.read()
    
    #Elle cherche l'ID, le NOM_Prenom, la Date, le Statut et l'Action
    regex_pattern = r"(?:ID|USER):(?P<id>\d+)[ >-]+(?:NAME)?:?(?P<nom>\w+)_(?P<prenom>\w+)[ >-]+\w+:(?P<date>\d{2}\/\d{2}\/\d{4})[ >-]+\w+:(?P<statut>[\w-]+)[ >-]+\w+:(?P<operation>\w+)"
    
    #J'utilise .finditer pour avoir les dictionnaires 
    finditer = re.finditer(regex_pattern, texte)

    # Je créer une liste pour mettre mes distionnaires afin de pouvoir utiliser pandas
    data = [m.groupdict() for m in finditer]

    # Création du DataFrame à travers data
    df = pd.DataFrame(data)

    # Chemin vers le dossier processed
    output_path = "C:/Users/utilisateur/Data_Cleaning_Parsing_Project/data/fichier_ordonne/cleaned_data.csv"

    # export en CSV (index=False évite d'ajouter une colonne de numéros inutile)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

if __name__ == "__main__":
    importation_fichier()
 
