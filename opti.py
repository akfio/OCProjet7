import pandas
from operator import itemgetter

actions = []


def get_csv_to_dict(fichier):
    doc = pandas.read_csv(fichier)
    for i in range(len(doc)):
        if doc["price"][i] > 0:
            prix = doc["price"][i]*100
            benef = doc["profit"][i]*100
            actions.append((doc["name"][i], int(prix), int(benef)))

def get_value(somme, benef):
    profit = benef/100
    pourcentage = 1 + profit / 100
    new = somme/100
    capital = new * pourcentage
    ratio = capital - new
    new_ratio = ratio * 100
    return int(new_ratio)


def get_optimized(prix, fichier):
    pri = prix*100
    get_csv_to_dict(fichier)
    nb_actions = len(actions)*100
    tableau = [[0 for w in range(pri + 1)] for w in range(nb_actions + 1)]
    for i in range(1, nb_actions + 1):
        j = int(i / 100)
        for x in range(1, pri + 1):
            if actions[j - 1][1] <= x:
                tableau[i][x] = max(
                    get_value(actions[j - 1][1], actions[j - 1][2]) + tableau[i - 1][x - actions[j - 1][1]],
                    tableau[i - 1][x])
            else:
                tableau[i][x] = tableau[i - 1][x]

    actions_name = []
    total_price = 0
    while prix >= 0 and nb_actions >= 0:
        e = actions[len(actions) - 1]

        if tableau[nb_actions][pri] == tableau[nb_actions - 1][pri - e[1]] + get_value(e[1], e[2]):
            actions_name.append(e[0])
            total_price += e[1]
            pri -= e[1]

        nb_actions -= 1
    return print('Actions achetées: ' + str(actions_name), '|| Profit: ' + str(tableau[-1][-1]/100),
                 '|| Prix: ' + str(total_price/100))


get_optimized(500, "data.csv")