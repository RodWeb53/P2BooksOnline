import requests
from bs4 import BeautifulSoup
import get_categorie



"""Phase 3 du projet
Récupérer les données des produits pour toute les catégories"""

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
        print('les categories sont  ' + str(categories) + '\n\n')


else:
    print("Les arguments de l'url ne sont pas conforme dans la page principale")

print('liste des liens ' + str(categories) + ' \n\n')

# Appel de la fonction get_categorie pour récupérer tous les liens de livres par catégorie   
categorie = []
nbre_livre = 0
for liste_categorie in categories:
    information_categorie = get_categorie.categorie_produit(liste_categorie)
    categorie.append(information_categorie)
    nbre_livre = nbre_livre + 1
    print("le produit " + str(categorie) + " est recupéré  \n\n")
    print('récupération du livre n°  ' + str(nbre_livre))



