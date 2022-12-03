import requests
from bs4 import BeautifulSoup
import get_produit




"""Phase 2 du projet
Récupérer les données des produits pour une catégorie"""

def categorie_produit(categorie):
    #Boucle pour connaitre le nombre de page par catégorie
    nombre_page = 0
    url_categorie = ''
    
    
    page_ok = True
    liens_categorie = []
    while page_ok:
        if nombre_page == 0:
            url_categorie = 'http://books.toscrape.com/catalogue/category/books/' + categorie + '/index.html'
        else:
            url_categorie = 'http://books.toscrape.com/catalogue/category/books/' + categorie + '/page-' + str(nombre_page + 1) + '.html'
        page = requests.get(url_categorie)
        if page.ok:
            nombre_page = nombre_page + 1
            print(nombre_page)
            print('la catégorie est ' + url_categorie + '\n\n')
            # creation de base_url pour enlever le chemin relatif récupéré
            base_url = 'http://books.toscrape.com/catalogue'
            
            soup = BeautifulSoup(page.content, 'html.parser')
            
            liens_produits = soup.find_all('h3')
            
            
            for lien_produit in liens_produits:
                lien_virtuel = lien_produit.find('a')
                lien_reel = lien_virtuel['href']
                liens_categorie.append(base_url + lien_reel[8:])

              
            # print('les liens de la page ' + str(liens_categorie) + '  sont récupéré \n\n')
            

        
        else:
            page_ok = False    


    """récpération des informations de chaque produit"""
    information_par_produit = []
    nbre_livre = 0
    for produit_categorie in liens_categorie:
        information_produit = get_produit.produit(produit_categorie)
        information_par_produit.append(information_produit)
        nbre_livre = nbre_livre + 1
        print("le produit " + produit_categorie + " est recupéré  \n\n")
        print('récupération du livre n°  ' + str(nbre_livre))


if __name__ == "__main__":

    """ligne pour lancer la phase 2 du projet suite à la mise en place de la fonction categorie_produit """
    # categorie_produit('sequential-art_5')
    categorie_produit('classics_6')



    """!!! il reste le transfert vers un fichier csv à faire !!!""" 

else:
    print('sortie du main')
