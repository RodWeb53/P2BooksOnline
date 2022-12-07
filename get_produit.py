import requests
from bs4 import BeautifulSoup
import csv
import os

"""Fonction pour récupérer les données d'un produit et export en csv local"""

def produit(url):
    page = requests.get(url)
    if page.ok:
        soup = BeautifulSoup(page.content, 'html.parser')

        """liste des td (pour récpérer upc[0], price_including_tax [3], price_excluding_tax [2]
        number_available [5], review_raiting [6])"""
        liste_td = soup.find_all('td')

        upc = liste_td[0].text

        titre = soup.find('h1').text
        
        prix_ttc = liste_td[3].text
        
        prix_ht = liste_td[2].text
        
        quantite_disponible = liste_td[5].text

        """Boucle pour récupérer les commentaires et s'il n'y a pas de commentaire 
        on récupère un champ vide"""
        try:
            description = soup.find('p', class_ ='').text
        except AttributeError as e:
            description = ""


        """Récupération de la catégorie"""
        liens_categorie = soup.find_all('a')
        categorie = liens_categorie[3].text

        version = liste_td[6].text

        """Construction du lien pour l'image récupération de la première image du site (image_base)
        récupération des valeurs de src (image_lien) reconstruction du lien de l'image"""
        image_base = soup.find('img')
        image_lien = image_base['src']
        image = 'http://books.toscrape.com' + image_lien[5:]


        """ Téléchargement de l'image et sauvegarde dans un répertoire ou local si lancé depuis le main"""
        nom_image = image.split('/')[-1]
        load_image = requests.get(image)

        path = os. getcwd()
        try:
            os.chdir(f'{path}/images/')
        except:
            os.chdir(f'{path}')


        with open(f'{nom_image}', 'wb') as f:
            f.write(load_image.content)
            os.chdir(f'{path}/')


        resultat = url, upc, titre, prix_ttc, prix_ht, quantite_disponible, description, categorie, version, image

        return resultat

    else:
            print("Les arguments de l'url ne sont pas conforme produit")      




if __name__ == "__main__":

     
    
    lien = 'http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'
    images = 'http://books.toscrape.com/media/cache/99/df/99df494c230127c3d5ff53153d1f23a3.jpg'
    resultat = produit(lien)  

    # Création du fichier csv

    en_tete = ['product_page_url', 'universal_ product_code', 'title', 'price_including_tax', 'price_excluding_tax',
         'number_available', 'product_description', 'category', 'review_rating', 'image_url']

    with open('un_produit.csv', 'w', encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(en_tete)
        writer.writerow(resultat)


else:
    print('sortie du main')
