import pandas
import time


actions = []


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

def get_reponse(prix: int):
    get_csv_to_dict("data.csv")
    new_price = prix * 100
    nb_actions = len(actions)
    mini = actions[-1][1]
    sac = [0] * (new_price + 1)
    tableau = [sac[:]]


    for i in range(1, nb_actions + 1):
        (_, price, profit) = actions[i - 1]

        for j in range(prix, 0, -1):
            if price <= j:
                sac[j] = max(sac[j], sac[j - price] + profit)

        tableau.append(sac[:])
        print(sac[:])

"""
        if tableau[i][mini:] == tableau[i - 1][mini:]:
            #print(tableau[i][mini:])
            #print(tableau[i - 1][mini:])
            nb_actions = i

            break

    actions_name = []
    total_price = 0
    while new_price >= 0 and nb_actions >= 0:
        e = actions[nb_actions - 1]
        #print(actions[nb_actions])
        #print(tableau[nb_actions][new_price - e[1]] + get_value(e[1], e[2]))
        #print(tableau[nb_actions - 1][new_price - e[1]] + get_value(e[1], e[2]))
        if tableau[nb_actions][new_price] == tableau[nb_actions - 1][new_price - e[1]] + get_value(e[1], e[2]):
            actions_name.append(e[0])
            total_price += e[1]
            new_price -= e[1]

        nb_actions -= 1
    return print('Actions achetées: ' + str(actions_name), '|| Profit: ' + str(tableau[-1][-1] / 100),
                 '|| Prix: ' + str(total_price / 100))


if __name__ == '__main__':
    START_TIME = time.time()

    # generate a pandas.DataFrame from file passed in args
    data_frame = pandas.read_csv("./data.csv")

    # create a list of records (type tuple) from data_frame adding a column ratio (profit/price)
    records = [(name, int(round(price, 0)), profit, profit / price)
               for (name, price, profit) in data_frame.to_records(index=False)
               if profit > 0 and price > 0]

    # sort records on ratio (profit/price) then price decreasing order
    records.sort(key=lambda x: (x[2], x[1]), reverse=True)
    print(records)
    
    for i in range(nb_actions, 0, -1):
        if max_profit <= 0:
            break
        if max_profit == tableau[i - 1][s]:
            continue
        (_, price, profit) = actions[i - 1]
        max_profit -= profit
        s -= price
    """

get_reponse(500)

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



#get_optimized(500, "data.csv")

"""
def can_partition(num):
  s = sum(num)
  dp = [[-1 for x in range(s+1)] for y in range(len(num))]
  return can_partition_recursive(dp, num, 0, 0, 0)


def can_partition_recursive(dp, num, currentIndex, sum1, sum2):
  # base check
  if currentIndex == len(num):
    return abs(sum1 - sum2)

  # check if we have not already processed similar problem
  if dp[currentIndex][sum1] == -1:
    # recursive call after including the number at the currentIndex in the first set
    diff1 = can_partition_recursive(
      dp, num, currentIndex + 1, sum1 + num[currentIndex], sum2)

    # recursive call after including the number at the currentIndex in the second set
    diff2 = can_partition_recursive(
      dp, num, currentIndex + 1, sum1, sum2 + num[currentIndex])

    dp[currentIndex][sum1] = min(diff1, diff2)

  return dp[currentIndex][sum1]




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

"""
