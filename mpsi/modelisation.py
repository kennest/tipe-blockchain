import hashlib
import time
import random as rd


def nombre_zeros_debut(c,r) :
    """Compte le nombre de zéros consécutifs en première position
    d'un chaîne de caractères."""
    nb = 0
    for i in range (r) :
        if c[i] == '0' :
            nb = nb + 1
    return nb

        
def preuve_travail_nbr_zeros(x, string, K) : 
    """ Peuve de travail basée sur le nombr de zéros consécutifs du hash
    x est le paramètre de difficulté de la preuve
        string est la chaîne de caractères et K et le nombre de boucles totales.
        Retourne reussie si le nombre de zeros convient, le hash trouvé et
        le nombre de boucles exécutées."""
    # a = time.time() #pour des tests
    k = 0 # nombre de tentatives
    l = string # chaîne passée en argument
    h = (hashlib.sha256((l + str(k)).encode('utf8'))).hexdigest()
    reussie = False
    while nombre_zeros_debut(h, x) < x and k <= K:
        k += 1
        h = (hashlib.sha256((l + str(k)).encode('utf8'))).hexdigest()
    if nombre_zeros_debut(h, x) >= x:
        reussie = True
    # b = time.time()
    #print("Temps : " + str(b-a))
    return reussie, h, k

def proof_stake_nbr_zeros(string, K, solde, alpha, beta):
    """ Fonction de proof of stake, prenant en paramètres le solde
    et l'ancienneté de l'utilisateur, et réalisant une PoW en calculant
    la difficulté selon ces paramètres

    alpha et beta sont des coefficients arbitraires
    alpha = 1, beta = 0.5 """
    #a = time.time() #test
    k = 0 
    l = string
    x = int((10**9 / ((time.time() - 1400000000) * alpha * solde))**beta) + 1
    h = (hashlib.sha256((l + str(k)).encode('utf8'))).hexdigest()
    reussie = False
    while nombre_zeros_debut(h, x) < x and k <= K:
        k += 1
        h = (hashlib.sha256((l + str(k)).encode('utf8'))).hexdigest()
    if nombre_zeros_debut(h, x) >= x:
        reussie = True
    #b = time.time()
    return reussie, h, k
    

def initialisation(n):
    """ Initialise la fonction fonctionnement."""
    utilisateurs = []
    for i in range(n):
         # Chaîne de caractère arbitraire représentant
         # une transaction 0, hash du block, nombre d'itérations pour
         # l'obtenir
        blockchain_i = [("42", "0dfcddb0440e967f05bb68ca09a5e2188b8abc36bfb5b95b83b88be59c42c6e7", 5)]
        utilisateurs.append([blockchain_i, 1000, 100, 1466768000])
    return utilisateurs

def initialisation_ter(n):
    """ Initialise la fonction fonctionnement."""
    utilisateurs = []
    blockchain_i = [("42", "0dfcddb0440e967f05bb68ca09a5e2188b8abc36bfb5b95b83b88be59c42c6e7", 5)]
    utilisateurs.append([blockchain_i, 2000, 100, 1466768000])
    for i in range(1,n):
         # Chaîne de caractère arbitraire représentant
         # une transaction 0, hash du block, nombre d'itérations pour
         # l'obtenir
        blockchain_i = [("42", "0dfcddb0440e967f05bb68ca09a5e2188b8abc36bfb5b95b83b88be59c42c6e7", 5)]
        utilisateurs.append([blockchain_i, 1000, 100, 1466768000])
    return utilisateurs


def fonctionnement_pow_zero(n, temps, difficulte):
    """Retourne les utilisateurs au bout de temps boucles."""
    utilisateurs = initialisation(n)
    for t in range(temps):
        for i in range(n): # Pour chaque utilisateur
            K = utilisateurs[i][1] # 'Puissance' de l'utilisateur
            reussie = True
            while reussie == True:
                x = rd.randrange(1000000)
                #print(x)
                (reussie, h, k) = preuve_travail_nbr_zeros(difficulte, \
                                                           str(x), K)
                #print(reussie, h, k)
                if reussie == True:
                    (utilisateurs[i][0]).append((str(x), h, k))
                K = K - k
        for i in range(n): # Autre boucle, pour avoir les résultats de tous
            # les utilisateurs
            liste_a_comparer = [rd.randrange(n) for j in range(10)]
            l = len(utilisateurs[i][0])
            for j in liste_a_comparer:
                p = len(utilisateurs[j][0])
                if l <= p + 2:
                    utilisateurs[i][0] = (utilisateurs[j][0]).copy()                
    return utilisateurs

def sauvegarde_utilisateurs_fichier(utilisateurs, nom):
    """ Sauvegarde la liste utilisateurs dans un fichier."""
    utilisateurs_temp = []
    for i in range(len(utilisateurs)):
        utilisateur_i = utilisateurs[i]
        blockchain_i_temp = []
        for j in range(len(utilisateur_i[0])):
            blockchain_i_temp.append(str(utilisateur_i[0][j]))
        blockchain_i_str = ('\n\t').join(blockchain_i_temp)
        utilisateur_i_str = str(i) + ':' + str(utilisateur_i[1]) + ';' + \
                            str(utilisateur_i[2]) + ';' + \
                            str(utilisateur_i[3]) + '\n\t' + \
                            blockchain_i_str
        utilisateurs_temp.append(utilisateur_i_str)
    texte = '\n\n'.join(utilisateurs_temp)
    with open(nom, 'w') as f:
        f.write(texte)
    return True

def charger_utilisateurs_fichier(nom):
    """ Non fonctionnel. """
    with open(nom, 'r') as f:
        list_str = f.readlines()
    list_blancs = []
    for i in range(len(list_str)):
        if list_str[i] == '\n':
            list_blancs.append(i)
    list_blancs.reverse()
    list_temp = []
    for i in range(1, len(list_blancs)):
        list_temp.append([list_str[j] for j in range(list_blancs[i-1], list_blancs[i])])
    list_temp.reverse()
    utilisateurs = list_temp
    return utilisateurs

def etat_pow_zero(n, temps, difficulte, nom):
    """ Créé un fichier contenant la liste utilisateurs formatées en txt."""
    utilisateurs = fonctionnement_pow_zero(n, temps, difficulte)
    sauvegarde_utilisateurs_fichier(utilisateurs, nom)
    return None

def nbr_branches_diff(utilisateurs):
    """ Regarde le nombre de blockchains différentes présentes dans une liste
    d'utilisateurs."""
    blockchains = [utilisateurs[0][0]]
    for i in range(1,len(utilisateurs)):
        j = 0
        leave = False
        while leave == False and j < len(blockchains):
            if utilisateurs[i][0] == blockchains[j]:
                j -= 1
                leave = True
            j += 1
        if j+1 != len(blockchains):
            blockchains.append(utilisateurs[i][0])
    return len(blockchains), blockchains

def etat_nbr_branches_diff_pow_zero(n, temps, difficulte, nom):
    utilisateurs = fonctionnement_pow_zero(n, temps, difficulte)
    nbr_br = nbr_branches_diff(utilisateurs)
    sauvegarde_utilisateurs_fichier(utilisateurs, nom)
    return nbr_br

def initialisation_bis(n):
    """ Initialise la fonction fonctionnement."""
    utilisateurs = []
    for i in range(n):
        if i%2 == 0:
         # Chaîne de caractère arbitraire représentant
         # une transaction 0, hash du block, nombre d'itérations pour
         # l'obtenir
            blockchain_i = [("42", "0dfcddb0440e967f05bb68ca09a5e2188b8abc36bfb5b95b83b88be59c42c6e7", 5)]
            utilisateurs.append([blockchain_i, 1000, 1, 1466947198])
        else:
            blockchain_i = [("42", "0dfcddb0440e967f05bb68ca09a5e2188b8abc36bfb5b95b83b88be59c42c6e7", 5)]
            utilisateurs.append([blockchain_i, 1000, 100, 1466768000])
    return utilisateurs

def fonctionnement_pos_zero(n, temps):
    """Retourne les utilisateurs au bout de temps boucles."""
    utilisateurs = initialisation_bis(n)
    for t in range(temps):
        for i in range(n): # Pour chaque utilisateur
            K = utilisateurs[i][1] # 'Puissance' de l'utilisateur
            solde = utilisateurs[i][2]
            reussie = True
            while reussie == True:
                x = rd.randrange(1000000)
                #print(x)
                (reussie, h, k) = proof_stake_nbr_zeros(str(x), K, solde, 1, 0.5)
                #print(reussie, h, k)
                if reussie == True:
                    (utilisateurs[i][0]).append((str(x), h, k))
                K = K - k
        for i in range(n): # Autre boucle, pour avoir les résultats de tous
            # les utilisateurs
            liste_a_comparer = [rd.randrange(n) for j in range(10)]
            l = len(utilisateurs[i][0])
            for j in liste_a_comparer:
                p = len(utilisateurs[j][0])
                if l <= p + 2:
                    utilisateurs[i][0] = (utilisateurs[j][0]).copy()                
    return utilisateurs

def etat_pos_zero(n, temps, nom):
    """ Créé un fichier contenant la liste utilisateurs formatées en txt."""
    utilisateurs = fonctionnement_pos_zero(n, temps)
    sauvegarde_utilisateurs_fichier(utilisateurs, nom)
    return None
