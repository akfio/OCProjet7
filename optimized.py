import pandas
import time


actions = []

"""
def get_csv_to_dict(fichier):
    doc = pandas.read_csv(fichier)
    for i in range(len(doc)):
        if doc["price"][i] > 0:
            prix = doc["price"][i] * 100
            actions.append((doc["name"][i], int(prix), doc["profit"][i]))


def get_value(somme, benef):
    pourcentage = 1 + benef / 100
    capital = somme / 100 * pourcentage
    ratio = capital - somme / 100
    new_ratio = ratio * 100
    return int(new_ratio)


def get_optimized(prix, fichier):
    new_price = prix * 100
    get_csv_to_dict(fichier)
    nb_actions = len(actions)
    tableau = [[0 for w in range(new_price + 1)] for w in range(nb_actions + 1)]
    for i in range(1, nb_actions + 1):
        for x in range(1, new_price + 1):
            if actions[i - 1][1] <= x:
                tableau[i][x] = max(
                    get_value(actions[i - 1][1], actions[i - 1][2]) + tableau[i - 1][x - actions[i - 1][1]],
                    tableau[i - 1][x])
            else:
                tableau[i][x] = tableau[i - 1][x]

    actions_name = []
    total_price = 0
    while new_price >= 0 and nb_actions >= 0:
        e = actions[nb_actions - 1]
        if tableau[nb_actions][new_price] == tableau[nb_actions - 1][new_price - e[1]] + get_value(e[1], e[2]):
            actions_name.append(e[0])
            total_price += e[1]
            new_price -= e[1]

        nb_actions -= 1
    return print('Actions achetées: ' + str(actions_name), '|| Profit: ' + str(tableau[-1][-1] / 100),
                 '|| Prix: ' + str(total_price / 100))

a = time.time()
get_optimized(500, "data.csv")
b = time.time()

print(b - a)

"""
def get_csv_to_dict(fichier):
    doc = pandas.read_csv(fichier)
    for i in range(len(doc)):
        actions.append((doc["name"][i], doc["price"][i], doc["profit"][i]))


def get_value(somme, benef):
    pourcentage = 1 + benef / 100
    capital = somme * pourcentage
    ratio = capital - somme
    return ratio


def get_optimized(prix, fichier):
    get_csv_to_dict(fichier)
    nb_actions = len(actions)
    tableau = [[0 for w in range(prix + 1)] for w in range(nb_actions + 1)]
    for i in range(1, nb_actions + 1):
        for x in range(1, prix + 1):
            if actions[i - 1][1] <= x:
                tableau[i][x] = max(
                    get_value(actions[i - 1][1], actions[i - 1][2]) + tableau[i - 1][x - actions[i - 1][1]],
                    tableau[i - 1][x])
            else:
                tableau[i][x] = tableau[i - 1][x]

    actions_name = []
    total_price = 0
    while prix >= 0 and nb_actions >= 0:
        e = actions[nb_actions - 1]
        if tableau[nb_actions][prix] == tableau[nb_actions - 1][prix - e[1]] + get_value(e[1], e[2]):
            actions_name.append(e[0])
            total_price += e[1]
            prix -= e[1]

        nb_actions -= 1
    return print('Actions achetées: ' + str(actions_name), '|| Profit: ' + str(tableau[-1][-1]),
                 '|| Prix: ' + str(total_price))


a = time.time()
get_optimized(500, "data.csv")
b = time.time()

print(b - a)


