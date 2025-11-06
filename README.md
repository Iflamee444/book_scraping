Projet : BookToScrap Scraper

**Auteurs :** RAVELOSON Marius - GELAC Yoan

**Date :** Octobre 2025  

---

## 🧠 Description  
Ce projet est un **script Python** permettant de **scraper automatiquement les informations des livres** du site [Books to Scrape](https://books.toscrape.com).  
Il permet de sélectionner des **catégories**, de limiter le **nombre de livres** à extraire, et de choisir les **informations spécifiques** à récupérer (prix, stock, note, etc.).  

Le script génère un fichier CSV contenant les données structurées et nettoyées pour une analyse ou un usage ultérieur.  

---

## 🏗️ Structure du projet  
```txt
📂 Projet-Scraping/
│
├── scrape.py # Script principal exécuté via la ligne de commande
├── utils.py # Fonctions utilitaires : nettoyage, conversion, etc.
├── categories.py # Liste ou scraping automatique des catégories
├── requirements.txt # Dépendances Python nécessaires
├── README.md # Documentation du projet
└── data/ # Dossier où les CSV extraits sont enregistrés
```
---

| Paramètre        | Obligatoire | Description                                                                            | Exemple                       |
| ---------------- | ----------- | -------------------------------------------------------------------------------------  | ----------------------------- |
| `--categories`   | ❌           | Liste des catégories à scraper. Si non précisé, toutes les catégories sont utilisées. | `--categories Travel Science` |
| `--delay`     | ❌           | Le délais entre chaque requêtes (par seconde).                                   | `--delay 10`                |
| `--outdir` | ❌           | Change la sortie pour les informations récupérer       | `--outdir output`       |
| `--max_page`     | ❌           | Nombre maximal de pages à parcourir dans chaque catégorie.                            | `--max_page 3`                |
| `--max_book`     | ❌           | Nombre maximal de livre à récupérer.                                                  | `--max_book 5`                |

---

## 💻 Exemple d’exécution  

### Requirement (obligatoire):
```bash
pip install -r requirements.txt
```

### Commande :
```bash
python.exe scrape.py --categories Travel Science --max_book 5 --outdir my_books
```
## 🧾 Licence

Projet open-source à but éducatif. L’auteur décline toute responsabilité quant à l’usage du script sur des sites autres que BooksToScrape.
