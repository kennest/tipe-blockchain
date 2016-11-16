# Pour récupérer une réponse à une requête :
 * A envoie la requête (Id = x ; Question = Requête ; Réponse = Vide) à B
 * B transmet à C si B n'a pas la réponse, et B enregistre que A lui a transmis cette requête
 * ...
 * Ceci remonte jusqu'à un utilisateur Z possédant la réponse
 * Alors Z envoie la réponse (Id = x ; Question = Requête ; Réponse = Information) à Y
 * Qui la remonte à X
 * ...
 * B envoie la réponse à A
