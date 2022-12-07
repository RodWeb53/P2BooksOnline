import get_all_categories
import get_categorie
import os



categories = get_all_categories.categorie_all()
    
""" Création d'une directory <<data>> pour y mettre les fichiers"""
path = os. getcwd()
os.mkdir(f'{path}/data/')



# Appel de la fonction get_categorie pour récupérer tous les liens de livres par catégorie   
for liste_categorie in categories:
    # Création d'une directory par catégorie et et d'une sous catégorie images 
    os.mkdir(f'{path}/data/{liste_categorie}/')
    os.mkdir(f'{path}/data/{liste_categorie}/images/')
    os.chdir(f'{path}/data/{liste_categorie}/')
    information_categorie = get_categorie.categorie_produit(liste_categorie)