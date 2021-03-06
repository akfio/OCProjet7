import argparse
import sys
import time
import pandas as pd



def calculate_and_print_knapsack(max_weight: int, items: [], results_file) -> None:
    """
    Function that resolves the 0-1 knapsack problem and prints the combination of items that gives
    the best profit for weight of selected items less or equal to max_weight
    @param max_weight: int
    @param items: list
    @param results_file: str
    """

    number_of_items = len(items)  # number of items
    min_weight = items[-1][1]  # minimum weight is the last item's price
    knapsacks = [0] * (max_weight + 1)
    matrices = [knapsacks[:]]



    # Loop to generate combinations of actions
    # Starts from i = 1 until number_of_items included it verifies condition :
    #     matrices[0][j] = 0 whatever j
    for i in range(1, number_of_items + 1):

        # current item is actually from occurrence i - 1
        (_, price, profit, _) = items[i - 1]

        # generate knapsacks from current item
        # Starts from j = max_weight until 1 included so that it verifies condition
        #   matrices[i][0] = 0 whatever i
        # and it does not need to implement the else part of condition price <= j
        for j in range(max_weight, 0, -1):
            if price <= j:
                knapsacks[j] = max(knapsacks[j], knapsacks[j - price] + profit)

        # Add a copy of current knapsacks to matrices
        matrices.append(knapsacks[:])
        #print(matrices)

        # Quit the loop when max profit is found
        # i.e. when the line from where the last knapsacks index between
        # min_weight and max_weight do not vary anymore

        if matrices[i][min_weight:] == matrices[i - 1][min_weight:]:
            number_of_items = i
            break

    # maximum profit
    max_profit = knapsacks[max_weight]

    # investment is the minimum weight corresponding to max_profit
    j = min([j for j in range(max_weight + 1) if knapsacks[j] == max_profit])
    invest_min = j / 100


    # Write the results in results_file
    with open(results_file, 'w', encoding='utf-8') as file:
        file.write('Liste des actions\n')
        # Loop to get combination of actions with the max_profit
        # Iterates i from number_of_items until i == 1 or max_profit <= 0
        # Whenever i is the minimum where matrices[i][j] == max_profit :
        #     - write name
        #     - decrease max_profit from profit (value)
        #     - decrease j from price (weight)
        for i in range(number_of_items, 0, -1):
            if max_profit <= 0:
                break
            if max_profit == matrices[i - 1][j]:
                continue
            (name, price, profit, _) = items[i - 1]
            file.write(f'{name}\n')
            max_profit -= profit
            j -= price
        file.write(f'Profit maximal = {knapsacks[max_weight]:.2f} ???\n')
        file.write(f'Somme investie = {invest_min:.2f} ???\n')


if __name__ == '__main__':

    START_TIME = time.time()

    # generate a pandas.DataFrame from file passed in args
    data_frame = pd.read_csv("./data.csv")

    # create a list of records (type tuple) from data_frame adding a column ratio (profit/price)

    records = [(name, int(round(price * 100, 0)), profit, profit / price)
               for (name, price, profit) in data_frame.to_records(index=False)
               if profit > 0 and price > 0]

    # sort records on ratio (profit/price) then price decreasing order
    records.sort(key=lambda x: (x[3], x[1]), reverse=True)
    print(records)

    # path to file results


    # call the function that resolves the 0-1 knapsack problem

    calculate_and_print_knapsack(500, records, None)
    
