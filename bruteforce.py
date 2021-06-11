from operator import itemgetter
import time
import pandas


actions = []

def get_csv_to_dict(fichier):
    doc = pandas.read_csv(fichier)
    for i in range(len(doc)):
        actions.append((doc["nom"][i], doc["prix"][i], doc["profit"][i]))


def get_value(somme, pourcentage):
    capital = somme * pourcentage
    ratio = capital - somme
    return ratio
    #return round(ratio, 1)

def get_binaire():
    n = len(actions)
    table_entiers = []
    for i in range(2 ** n):
        entier = i
        table_entiers.append(entier)
    table_binaire = []
    for j in table_entiers:
        binaire = bin(j)[2:]
        table_binaire.append(binaire)
    return table_binaire

def get_combinaisons(prix, nombre_de_combinaisons):
    n = len(actions)
    combinaisons = []
    for k in get_binaire():
        combins = '0' * (n - len(k)) + k
        combinaisons.append(combins)
    prix_max = prix
    combinaisons_valides = []
    for combi in combinaisons:
        prix_combi = 0
        value = 0
        name = 0
        action = []
        for l in range(n):
            name += 1
            if combi[l] == '1':
                prix_combi += actions[l][1]
                value += get_value(actions[l][1], actions[l][2])
                action.append(actions[l][0])
        if prix_combi <= prix_max:
            combinaisons_valides.append(('Actions achetées: ' + str(action), 'Total investis: ' + str(prix_combi),
                                         'Total profit: ' + str(value)))
    return sorted(combinaisons_valides, key=itemgetter(2), reverse=True)[:nombre_de_combinaisons]

def process(fichier):
    get_csv_to_dict(fichier)
    print(get_combinaisons(500, 1))

process("data.csv")

def get_brut():
    get_csv_to_dict("data.csv")
    n = len(actions)
    table_entiers = []
    for i in range(2 ** n):
        entier = i
        table_entiers.append(entier)
    table_binaire = []
    for j in table_entiers:
        binaire = bin(j)[2:]
        table_binaire.append(binaire)
    combinaisons = []
    for k in table_binaire:
        combins = '0' * (n - len(k)) + k
        combinaisons.append(combins)
    prix_max = 500
    combinaisons_valides = []
    for combi in combinaisons:
        prix_combi = 0
        value = 0
        for l in range(n):
            if combi[l] == '1':
                prix_combi += actions[l][1]
                value += get_value(actions[l][1], actions[l][2])
        if prix_combi <= prix_max:
            combinaisons_valides.append((combi, prix_combi, value))
    return sorted(combinaisons_valides, key=itemgetter(2), reverse=True)[0]


a = time.time()
#print(get_combinaisons(500, 1))
b = time.time()
#print(b-a)

"""
actions = [
    (1, 20, 1.05),
    (2, 30, 1.10),
    (3, 50, 1.15),
    (4, 70, 1.20),
    (5, 60, 1.17),
    (6, 80, 1.25),
    (7, 22, 1.07),
    (8, 26, 1.11),
    (9, 48, 1.13),
    (10, 34, 1.27),
    (11, 42, 1.17),
    (12, 110, 1.09),
    (13, 38, 1.23),
    (14, 14, 1.01),
    (15, 18, 1.03),
    (16, 8, 1.08),
    (17, 4, 1.12),
    (18, 10, 1.14),
    (19, 24, 1.21),
    (20, 114, 1.18),
]
"""

