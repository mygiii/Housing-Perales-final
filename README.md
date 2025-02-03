<<<<<<< HEAD
# Housing-Perales-final
Celui là est le dernier repertoire que je créer
=======
# Housing API test

**Housing API** est une API développée avec **FastAPI** et **PostgreSQL**, déployée facilement avec **Docker**. Elle permet de gérer des enregistrements de maisons. Ce guide vous explique comment cloner le projet, le lancer avec Docker et tester l'API avec des exemples d'utilisation.

## Table des Matières

1. [Cloner le Projet](#1-cloner-le-projet)
2. [Lancer le Projet avec Docker](#2-lancer-le-projet-avec-docker)
3. [Tester l'API avec cURL](#3-tester-lapi-avec-curl)
4. [Notes Importantes](#4-notes-importantes)
5. [Licence](#5-licence)

## 1. Cloner le Projet

1. **Cloner le dépôt GitHub** :
   ```bash
   git clone https://github.com/votre-utilisateur/housing-firstname-lastname.git
   cd le project
   ```

2. **Vérifier que les fichiers nécessaires sont présents** :  
   Assurez-vous que les fichiers suivants existent dans le projet :
   - `docker-compose.yml`
   - `Dockerfile`
   - `app/` (le dossier contenant le code source)
   - `pyproject.toml` et `poetry.lock`

## 2. Lancer le Projet avec Docker

1. **Construire et lancer les conteneurs** :
   ```bash
   docker-compose up --build
   ```
   
   Cette commande :
   - Construira les images Docker pour le projet
   - Démarrera les services (API et base de données PostgreSQL)

2. **Accéder à l'API** :
   - Une fois les conteneurs démarrés, l'API sera disponible sur [http://localhost:8001](http://localhost:8001)
   - Vous pouvez accéder à la documentation interactive via [http://localhost:8001/docs](http://localhost:8001/docs)

3. **Arrêter les conteneurs** :
   ```bash
   docker-compose down
   ```

## 3. Tester l'API avec cURL (cette partie concerne seulement housing-api et pas le model de prediction)

### 3.1. Récupérer Toutes les Maisons (`GET /houses`)

Pour récupérer la liste des maisons :
```bash
curl -X GET http://localhost:8001/houses
```

Réponse Attendue (Exemple) :
```json
[]
```

### 3.2. Créer une Nouvelle Maison (`POST /houses`)

Pour ajouter une nouvelle maison à l'API :
```bash
curl -X POST http://localhost:8001/houses \
-H "Content-Type: application/json" \
-d '{
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41,
  "total_rooms": 880,
  "total_bedrooms": 129,
  "population": 322,
  "households": 126,
  "median_income": 8.3252,
  "median_house_value": 452600.0,
  "ocean_proximity": "NEAR BAY"
}'
```

Réponse Attendue (Exemple) :
```json
{
  "id": 1,
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41,
  "total_rooms": 880,
  "total_bedrooms": 129,
  "population": 322,
  "households": 126,
  "median_income": 8.3252,
  "median_house_value": 452600.0,
  "ocean_proximity": "NEAR BAY"
}
```

### 3.3. Valider une Erreur (Exemple d'Entrée Invalide)

Envoyez un POST avec des données manquantes :
```bash
curl -X POST http://localhost:8001/houses \
-H "Content-Type: application/json" \
-d '{
  "longitude": -122.23
}'
```

Réponse Attendue :
```json
{
  "detail": [
    {
      "loc": ["body", "latitude"],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": ["body", "housing_median_age"],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": ["body", "total_rooms"],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": ["body", "total_bedrooms"],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": ["body", "population"],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": ["body", "households"],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": ["body", "median_income"],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": ["body", "median_house_value"],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": ["body", "ocean_proximity"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### 3.4. Afficher les Logs Docker

Pour afficher les logs et surveiller le comportement de l'API et de la base de données, utilisez :
```bash
docker-compose logs -f
```

## 4. Notes Importantes

### Port par Défaut
L'API écoute sur le port 8001. Si vous modifiez le port dans le fichier docker-compose.yml, mettez à jour vos requêtes en conséquence.

### Fichier .env (Facultatif)
Si besoin, configurez un fichier .env pour personnaliser les paramètres (base de données, API, etc.).

### Réinitialiser les Conteneurs
Si vous rencontrez des problèmes, réinitialisez les conteneurs et les volumes :
```bash
docker-compose down --volumes
docker-compose up --build
```

### Sécurité
Ne divulguez jamais vos informations sensibles telles que les mots de passe dans votre dépôt GitHub. Assurez-vous que le fichier .env est bien inclus dans .gitignore.

### Mises à Jour des Dépendances
Régulièrement, mettez à jour vos dépendances avec Poetry pour bénéficier des dernières fonctionnalités et correctifs de sécurité :
```bash
poetry update
```

### Optimisation Docker
- Utilisez le cache Docker efficacement en structurant votre Dockerfile de manière à minimiser les rebuilds inutiles
- Évitez de copier tout le répertoire du projet avant d'installer les dépendances, cela permet de profiter du cache Docker pour les dépendances qui ne changent pas souvent

## 5. Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

---

Merci d'avoir utilisé Housing API ! 😊  
N'hésitez pas à ouvrir des issues ou des pull requests si vous avez des suggestions ou des améliorations à proposer.
>>>>>>> 8e17167 (Initial commit)
