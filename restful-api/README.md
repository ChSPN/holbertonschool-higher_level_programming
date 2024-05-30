# Différenciation entre HTTP et HTTPS

## HTTP vs HTTPS

**HTTP** (HyperText Transfer Protocol) et **HTTPS** (HTTP Secure) sont des protocoles utilisés pour la communication entre les clients (comme les navigateurs web) et les serveurs web. La principale différence entre eux réside dans la sécurité.

### HTTP
- **Données non chiffrées** : HTTP ne chiffre pas les données transmises. Cela signifie que les données peuvent être lues par toute personne interceptant la communication (man-in-the-middle).
- **Port standard** : Utilise le port 80 par défaut.
- **Utilisation** : Convient pour les sites web où la sécurité des données n'est pas critique, comme les blogs ou les forums publics.

### HTTPS
- **Données chiffrées** : HTTPS ajoute une couche de chiffrement à l'aide de SSL/TLS (Secure Sockets Layer / Transport Layer Security), ce qui rend les données illisibles pour les eavesdroppers.
- **Port standard** : Utilise le port 443 par défaut.
- **Utilisation** : Nécessaire pour les sites web manipulant des informations sensibles comme les banques, les services de messagerie, et les plateformes de commerce électronique.

# Structure des Requêtes et Réponses HTTP

## Comprendre la structure des requêtes et des réponses HTTP

1. **Visitez un site web simple** et ouvrez les outils de développement de votre navigateur (clic droit -> Inspecter ou Inspect Element).
2. **Allez à l'onglet "Network"** et rechargez la page pour voir les requêtes réseau.
3. **Cliquez sur la première requête** pour explorer les en-têtes.

### Exemple de structure d'une requête HTTP

GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8
Accept-Language: en-US,en;q=0.8
Connection: keep-alive


### Exemple de structure d'une réponse HTTP

HTTP/1.1 200 OK
Date: Mon, 27 May 2023 12:28:53 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 27 May 2023 12:28:53 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 177

<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
```

## Méthodes HTTP Communes
### GET
Description : Récupère des données du serveur.
Utilisation : Affichage de pages web ou récupération de données depuis une API.
Exemple : Récupérer la page d'accueil d'un site web.
### POST
Description : Envoie des données au serveur pour créer ou mettre à jour une ressource.
Utilisation : Soumettre un formulaire ou envoyer des données via une API.
Exemple : Soumettre un formulaire de connexion.
### PUT
Description : Met à jour une ressource existante ou en crée une si elle n'existe pas.
Utilisation : Mettre à jour les informations d'un utilisateur.
Exemple : Modifier les informations de profil d'un utilisateur.
### DELETE
Description : Supprime une ressource spécifiée.
Utilisation : Supprimer un compte utilisateur.
Exemple : Supprimer un article de blog.

## Codes de Statut HTTP Communes
### 200 OK
Description : La requête a réussi.
Scénario : Une page web ou une ressource a été récupérée avec succès.
### 201 Created
Description : La requête a réussi et une nouvelle ressource a été créée.
Scénario : Un nouvel utilisateur a été créé via une API.
### 400 Bad Request
Description : La requête est mal formée ou contient des paramètres invalides.
Scénario : Envoi de données incorrectes dans un formulaire.
### 401 Unauthorized
Description : L'authentification est requise et a échoué ou n'a pas été fournie.
Scénario : Accéder à une page protégée sans être connecté.
### 404 Not Found
Description : La ressource demandée est introuvable.
Scénario : Accéder à une URL inexistante sur le serveur.
