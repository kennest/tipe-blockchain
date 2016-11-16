# Pour récupérer une réponse à une requête :
 * A envoie la requête (Id = x ; Question = Requête ; Réponse = Vide) à B
 * B transmet à C si B n'a pas la réponse, et B enregistre que A lui a transmis cette requête
 * ...
 * Ceci remonte jusqu'à un utilisateur Z possédant la réponse
 * Alors Z envoie la réponse (Id = x ; Question = Requête ; Réponse = Information) à Y
 * Qui la remonte à X
 * ...
 * B envoie la réponse à A

# Pour rendre le réseau sûr
C'est-à-dire pour que la réponse reçue par A corresponde bien à la bonne réponse à sa question. Ce peut être pour éviter des problèmes comme le piratage du site de téléchargement de Linux Mint.
 * S'assurer que au moins 50% des voisins de A lui transmettent cette information ?
 * Mais alors, il faut que ces 50% ne reçoivent pas leurs informations des mêmes sources *corrompues* ou *attaquantes*.
