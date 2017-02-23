import csv as csv

def ecrit_csv(tableau, nom):
    """tableau est de la forme list(list)"""
    with open(nom + ".csv", "w", newline='') as fichier:
        writer = csv.writer(fichier, delimiter=' ', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        for i in tableau:
            listtext = []
            for j in i:
                listtext.append(str(j))
            writer.writerow(listtext)

def lit_csv(fichier):
    """Retourne un tableau à doubles-entrées"""
    with open(fichier + ".csv", 'r', newline='') as fichiercsv:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            print(', '.join(row))
