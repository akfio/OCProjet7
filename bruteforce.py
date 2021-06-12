from operator import itemgetter
import pandas

actions = []


def get_csv_to_dict(fichier):
    doc = pandas.read_csv(fichier)
    for i in range(len(doc)):
        actions.append((doc["nom"][i], doc["prix"][i], doc["profit"][i]))


def get_value(somme, benef):
    pourcentage = 1 + benef / 100
    capital = somme * pourcentage
    ratio = capital - somme
    return ratio
    # return round(ratio, 2)


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


def get_combinaisons(fichier, prix, nombre_de_combinaisons):
    get_csv_to_dict(fichier)
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
        action = []
        for l in range(n):
            if combi[l] == '1':
                prix_combi += actions[l][1]
                value += get_value(actions[l][1], actions[l][2])
                action.append(actions[l][0])
        if prix_combi <= prix_max:
            combinaisons_valides.append(('Actions achetées: ' + str(action), 'Total investis: ' + str(prix_combi),
                                         'Total profit: ' + str(value)))
    return print(sorted(combinaisons_valides, key=itemgetter(2), reverse=True)[:nombre_de_combinaisons])


get_combinaisons("data.csv", 500, 1)
