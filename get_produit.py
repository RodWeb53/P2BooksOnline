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
        
        """Boucle pour récupérer les commentaires et s'il n'y a pas de commentaire 
        on récupère un champ vide"""
        description = []
        recup_description = soup.find_all('p', class_ ='')
        for decrip in recup_description:
            description.append(decrip)
        
        


        print('poduct_page_url = ' + url + '\n\n' + 'universal_ product_code (upc) = ' + upc + '\n\n' + 'title = ' + titre + '\n\n'
        + 'price_including_tax = ' + prix_ttc + '\n\n' + 'price_excluding_tax = ' + prix_ht + '\n\n' + 'number_available = ' + quantite_disponible
        + '\n\n' + 'product_description = ' + str(description) + '\n\n' + 'category = ' + categorie + '\n\n' + 'review_rating = ' + version
        + '\n\n' + 'image_url = ' + image)

    else:
            print("Les arguments de l'url ne sont pas conforme produit")      
     
if __name__ == "__main__":

     
    """ligne pour lancer la phase 1 du projet suite à la mise en place de la fonction produit """
    lien = 'http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'
    produit(lien)    
    """!!! il reste le transfert vers un fichier csv à faire !!!""" 
else:
    print('sortie du main')
