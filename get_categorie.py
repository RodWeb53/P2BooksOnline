import requests
from bs4 import BeautifulSoup
import get_produit
import csv

"""Phase 2 du projet. Récupérer les données des produits pour une catégorie"""

def categorie_produit(categorie):
    # Boucle pour connaitre le nombre de page par catégorie
    nombre_page = 0
    url_categorie = ''
    page_ok = True
    liens_categorie = []

    while page_ok:
        if nombre_page == 0:
            url_categorie = f'http://books.toscrape.com/catalogue/category/books/{categorie}/index.html'
        else:
            url_categorie = f'http://books.toscrape.com/catalogue/category/books/{categorie}/page-{str(nombre_page + 1)}.html'
        
        page = requests.get(url_categorie)
        
        if page.ok:
            nombre_page = nombre_page + 1

            # creation de base_url pour enlever le chemin relatif récupéré
            base_url = 'http://books.toscrape.com/catalogue'
            
            soup = BeautifulSoup(page.content, 'html.parser')
            
            liens_produits = soup.find_all('h3')
            
            
            for lien_produit in liens_produits:
                lien_virtuel = lien_produit.find('a')
                lien_reel = lien_virtuel['href']
                liens_categorie.append(base_url + lien_reel[8:])

        else:
            page_ok = False    

    """récpération des informations de chaque produit"""
    information_par_produit = []

    for produit_categorie in liens_categorie:
        information_produit = get_produit.produit(produit_categorie)
        information_par_produit.append(information_produit)



    """ Export des livres d'une catégorie"""

    en_tete = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax', 'price_excluding_tax',
        'number_available', 'product_description', 'category', 'review_rating', 'image_url']


    with open(f'{information_par_produit[0][7]}.csv', 'w', encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(en_tete)
        for produit in information_par_produit:
            writer.writerow(produit)
        



    return information_par_produit




if __name__ == "__main__":

    """ligne pour lancer la phase 2 du projet soit sur une mono page ou une multi page"""
    categorie_produit('classics_6') # monopage de livres
    # categorie_produit('sequential-art_5') # multi pages de livres


    

else:
    print('sortie du main')
