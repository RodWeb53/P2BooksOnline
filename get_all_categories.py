import requests
from bs4 import BeautifulSoup
import get_categorie
import csv
import os


"""Phase 3 du projet
Récupérer les données des produits pour toute les catégories"""


def categorie_all():

    url_complet = 'http://books.toscrape.com/catalogue/page-1.html'

    categories = []
    page = requests.get(url_complet)

    if page.ok:
        soup = BeautifulSoup(page.content, 'html.parser')
        listes_categories = soup.select('a[href]')

        # Boucle pour récupérer toutes les catégories
        for lien_produit in listes_categories:
            categorie_livre = lien_produit['href']
            if 'category/books/' in categorie_livre:
                lien_livre = categorie_livre.split('/',3)
                categories.append(lien_livre[2])



    else:
        print("Les arguments de l'url ne sont pas conforme dans la page principale")



    return categories

    

if __name__ == "__main__":

    categories = categorie_all()
    """ Création d'une directory data pour mettre les fichiers"""
    path = os. getcwd()
    os.mkdir(f'{path}/data/')



    # Appel de la fonction get_categorie pour récupérer tous les liens de livres par catégorie   
    for liste_categorie in categories:
        # Création d'une directory par catégorie et déplacement dans la directorie
        os.mkdir(f'{path}/data/{liste_categorie}/')
        os.mkdir(f'{path}/data/{liste_categorie}/images/')
        os.chdir(f'{path}/data/{liste_categorie}/')
        information_categorie = get_categorie.categorie_produit(liste_categorie)



else:
    print('sortie du main')
