
# Projet de requêtage SQL pour un fichier JSON

Ce projet utilise la bibliothèque **PLY** (Python Lex-Yacc) pour construire un analyseur lexical et syntaxique en Python.

## Prérequis

- Python 3.7 ou supérieur
- `git` installé

## Installation

1. **Cloner le dépôt**

```bash
git clone git@github.com:Wallblue/json_sql.git
cd json_sql
```

2. Créer un environnement virtuel

```bash
python -m venv venv
```

3. Activer cet environnement virtuel

- Sur Linux / MacOS :

  ```bash
  source venv/bin/activate
  ```

- Sur Windows :

  ```bash
  venv\Scripts\activate
  ```

## Utiliser le langage

Pour utiliser ce langage de requêtage, utilisez le terminal :

```bash
main.py [Votre requête]
```

Vous pouvez également créer un alias sur le fichier main.py pour l'utiliser plus intuitivement.

Par exemple :

```bash
main.py "SELECT title FROM city = 'Fontainebleau'"
```

Cette commande fonctionnerait pour un fichier qui ressemble à :

```json
[
  {
    "title": "La maison duchesse",
    "city": "Fontainebleau"
  },
  {
    "title": "Le Bourget",
    "city": "Paris"
  }
]
```

Les résultats de la requête sont envoyés dans un fichier `save.json` à la racine du projet.
