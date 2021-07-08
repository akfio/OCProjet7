import pandas

actions = []


def get_csv_to_dict(fichier):
    doc = pandas.read_csv(fichier)
    for i in range(len(doc)):
        if doc["price"][i] > 0:
            prix = doc["price"][i] * 100
            actions.append((doc["name"][i], int(prix), doc["profit"][i]))


def calculate_and_print_knapsack(max_weight: int, items: [], results_file) -> None:

    get_csv_to_dict("data.csv")
    number_of_items = len(actions)  # number of items
    min_weight = actions[-1][1]
    knapsacks = [0] * (max_weight + 1)
    matrices = [knapsacks[:]]

    for i in range(1, number_of_items + 1):

        (_, price, profit) = items[i - 1]


        for j in range(max_weight, 0, -1):
            if price <= j:
                knapsacks[j] = max(knapsacks[j], knapsacks[j - price] + profit)

        matrices.append(knapsacks[:])

        if matrices[i][min_weight:] == matrices[i - 1][min_weight:]:
            number_of_items = i
            break

    max_profit = knapsacks[max_weight]

    j = min([j for j in range(max_weight + 1) if knapsacks[j] == max_profit])
    invest_min = j / 100

    for i in range(number_of_items, 0, -1):
        if max_profit <= 0:
            break
        if max_profit == matrices[i - 1][j]:
            continue
        (name, price, profit) = items[i - 1]
        file.write(f'{name}\n')
        max_profit -= profit
        j -= price
    file.write(f'Profit maximal = {knapsacks[max_weight]:.2f} €\n')
    file.write(f'Somme investie = {invest_min:.2f} €\n')




calculate_and_print_knapsack(50000, actions, None)