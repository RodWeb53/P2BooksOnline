# Programme de scraping  du site http://books.toscrape.com 

## Cette application va permettre de scraper Book To Scrape afin de suivre les prix et les stocks dans le temps.

** Fonctionnalités ** 

- Extraires les données et les enregistrer au format .csv

    -   L'URL de la page web présentant le livre (product_page_url)
    -   Code universel de chaque livre (universal_ product_code (upc))
    -   Le titre du livre (title)
    -   Le prix TTC (price_including_tax)
    -   Le prix HT (price_excluding_tax)
    -   Quantité disponible (number_available)
    -   La description du livre (product_description)
    -   La catégorie du livre (category)
    -   La note du livre (review_rating),
    -   L'URL de l'image du livre (image_url)

- Extraires les images de couverture et les enregistrer

    -   Depuis l'URL de l'image récupération des fichiers et sauvegarde dans un répertoire


## Mise en place du programme

    ** Pré-requis : python 3 doit être installé sur votre machine **

- Télécharger ce code dans ''code'' > ''Download ZIP''
- Décompresser le dossier

### 1. Création de l'environnement virtuel

    Ouvrez le terminal, allez dans le dossier que vous avez téléchargé

    Tapez la commande suivante pour créer l'environnement virtuel

        * * python -m venv env

### 2. Lancement de l'environnement virtuel

    Sous Windows tapez la commande suivante :

        * * env\Scripts\activate.bat

    Sous MAC ou Linux tapez la commande suivante :

        * * source env/bin/activate

### 3. Installation des packages

    Les packages vont permettre le bon fonctionnement du programme

    Tapez la commande suivante pour installer les packages :

        * * pip install -r requirements.txt

    Si vous voulez vérifier que les packages sont bien installés tapez la commande suivante :

        * * pip freeze


## Lancement des programmes

    Pour l'extraction d'un livre taper la commande suivante :

        * * python get_produit.py

    Pour l'extraction d'une catégorie taper la commande suivante :

        * * python get_categorie.py

    Pour l'extraction de toutes les catégories taper la commande suivante :

        * * python main.py    




