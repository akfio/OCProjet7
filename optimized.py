from operator import itemgetter
import pandas
import time

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


def get_opti(prix, fichier):
    get_csv_to_dict(fichier)
    tableau = [[0 for w in range(prix)] for w in range(len(actions))]
    for i in range(len(actions)):
        for x in range(prix):
            if actions[i][1] <= x:
                tableau[i][x] = max(get_value(actions[i][1], actions[i][2]) + tableau[i - 1][x - actions[i][1]],
                                    tableau[i - 1][x])
            else:
                tableau[i][x] = tableau[i - 1][x]
    w = prix
    n = len(actions)
    elements_selection = []

    while w > 0 and n > 0:
        e = actions[n - 1]
        print(e)
        if tableau[n][w] == tableau[n - 1][w - e[1]] + get_value(e[1], e[2]):
            elements_selection.append(e)
            w -= e[1]

        n -= 1

    return tableau[-1][-1], elements_selection

print(get_opti(500, "data.csv"))



# Retrouver les éléments en fonction de la somme

