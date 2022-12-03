import requests
from bs4 import BeautifulSoup




"""Phase 3 du projet
Récupérer les données des produits pour toute les catégories"""

url_complet = 'http://books.toscrape.com/catalogue/page-1.html'

categorie = []

page = requests.get(url_complet)
if page.ok:
    soup = BeautifulSoup(page.content, 'html.parser')

    listes_categories = soup.select('a[href]')

   

    for lien_produit in listes_categories:
        categorie_livre = lien_produit['href']
        if 'category/books/' in categorie_livre:
            lien_livre = categorie_livre.split('/',3)
            categorie.append(lien_livre[2])


else:
    print("Les arguments de l'url ne sont pas conforme dans la page principale")
    
print('liste des liens ' + str(categorie) + ' \n\n')




