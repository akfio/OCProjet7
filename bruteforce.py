from operator import itemgetter
import time


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


def get_value(somme, pourcentage):
    capital = somme * pourcentage
    ratio = capital - somme
    return ratio


def get_brut():
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


a= time.time()
get_brut()
b= time.time()
print(b-a)