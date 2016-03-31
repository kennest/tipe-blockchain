""" Module pour le login et l'enregistrement d'utilisateur. """

def login(path):
    """ Permet à l'utilisateur de se connecter. """
    password = input('Mot de passe : ')
    with open(path + '/wallet', 'r') as f:
        f.readline()
        f.readline()
        truepassword = f.readline()
    if truepassword == password:
        return True
    return False


def signin(path):
    """ Permet à l'utilisateur de créer un compte. """
    print("Création d'une wallet")
    choix = 'f'
    while choix != 'y': # L'utilisateur doit confirmer le mot de passe
        password = input('Mot de passe : ')
        print(password)
        choix = input('y/n ')
     # Manque la clef publique et la clef privée
    with open(path + '/wallet', 'w') as f: # Sauvegarde la wallet
        f.write(password)
    return None

def checkuser(path):
    """ Vérifie si l'utilisateur a déjà une wallet. Retourne un booléen. """
    with open(path + '/wallet', 'r') as f:
        file = f.read()
    if file == '':
        return False
    return True
