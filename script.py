import requests
from bs4 import BeautifulSoup

"""Phase 1 du projet
récupérer les données d'un produit et export en csv"""

def produit(url):
    page = requests.get(url)
    if page.ok:
        soup = BeautifulSoup(page.content, 'html.parser')

        """liste des td (pour récpérer upc[0], price_including_tax [3], price_excluding_tax [2]
        number_available [5], review_raiting [6])"""
        listetd = soup.find_all('td')

        upc = listetd[0].text
        prix_ttc = listetd[3].text
        prix_ht = listetd[2].text
        version = listetd[6].text
        quantite_disponible = listetd[5].text

        """Récupération de la catégorie"""
        liens_categorie = soup.find_all('a')
        categorie = liens_categorie[3].text

        """Construction du lien pour l'image
        récupération de la première image du site (image_base)
        récupération des valeurs de src (image_lien)
        reconstruction du lien de l'image
        """
        image_base = soup.find('img')
        image_lien = image_base['src']
        image = 'http://books.toscrape.com' + image_lien[5:]


        titre = soup.find('h1').text
        description = soup.find('p', {'class': ''}).text


        # print('poduct_page_url = ' + url + '\n\n' + 'universal_ product_code (upc) = ' + upc + '\n\n' + 'title = ' + titre + '\n\n'
        # + 'price_including_tax = ' + prix_ttc + '\n\n' + 'price_excluding_tax = ' + prix_ht + '\n\n' + 'number_available = ' + quantite_disponible
        # + '\n\n' + 'product_description = ' + description + '\n\n' + 'category = ' + categorie + '\n\n' + 'review_rating = ' + version
        # + '\n\n' + 'image_url = ' + image)

    else:
            print("Les arguments de l'url ne sont pas conforme produit")      
     
"""ligne pour lancer la phase 1 du projet suite à la mise en place de la fonction produit """
# lien = 'http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'
# produit(lien)    
"""!!! il reste le transfert vers un fichier csv à faire !!!""" 



"""Phase 2 du projet
Récupérer les données des produits pour une catégorie"""

def categorie_produit(categorie):
    #Boucle pour connaitre le nombre de page par catégorie
    nombre_page = 0
    page_ok = True

    while page_ok:
        url_categorie = 'http://books.toscrape.com/catalogue/category/books/' + categorie + '/page-' + str(nombre_page + 1) + '.html'
        page = requests.get(url_categorie)
        if page.ok:
            nombre_page = nombre_page + 1
            print(nombre_page)
        else:
            page_ok = False    



    liens_categorie = []

    for i in range(1, nombre_page + 1):
        """url pour le parcours des 4 pages"""
        url_categorie = 'http://books.toscrape.com/catalogue/category/books/' + categorie + '/page-' + str(i) + '.html'
        page = requests.get(url_categorie)
        if page.ok:
            soup = BeautifulSoup(page.content, 'html.parser')

            """Récupération des liens par page et construction de l'adresse url"""
            #creation de base_url pour enlever le chemin relatif récupéré
            base_url = 'http://books.toscrape.com/catalogue'
            liens_produits = soup.find_all('h3')
            for lien_produit in liens_produits:
                lien_virtuel = lien_produit.find('a')
                lien_reel = lien_virtuel['href']
                liens_categorie.append(base_url + lien_reel[8:])
            print('les liens de la page  ' + str(i) + ' sont récupéré \n\n')

        else:
            print("Les arguments de l'url ne sont pas conforme Categorie")


    """récpération des informations de chaque produit"""
    information_par_produit = []

    for produit_categorie in liens_categorie:
        information_produit = produit(produit_categorie)
        information_par_produit.append(information_produit)
        print("le produit " + produit_categorie + " est recupéré  \n\n")




categorie_produit('sequential-art_5')


"""!!! il reste le transfert vers un fichier csv à faire !!!""" 

"""Phase 3 du projet
Récupérer les données des produits pour toute les catégories"""

