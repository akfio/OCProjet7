import pandas
import time

class Optimized:

    def __init__(self):
        self.actions = []
        self.actions_name = []

    def get_csv_to_dict(self, fichier):
        doc = pandas.read_csv(fichier)
        for i in range(len(doc)):
            if doc["price"][i] > 0:
                prix = doc["price"][i] * 100
                self.actions.append((doc["name"][i], int(prix), doc["profit"][i]))

    def get_value(self, price, profit):
        pourcentage = 1 + profit / 100
        capital = price / 100 * pourcentage
        ratio = capital - price / 100
        new_ratio = ratio * 100
        return int(new_ratio)

    def get_optimized(self, prix, fichier):
        new_price = prix * 100  # le prix est mis à echelle
        self.get_csv_to_dict(fichier)  # ajouter les données dans [actions]
        self.actions.sort(key=lambda x: x[2], reverse=True)  # trier la liste en utiliant le profit
        number_of_actions = len(self.actions)  # nombre total d'actions
        minimal_profit = self.actions[-1][1]  # le prix de l'action avec le plus petit profit obtenable
        sac_a_dos = [0] * (new_price + 1)  # création de la matrice accueillant les données
        tableau = [sac_a_dos[:]]  # copie de ces données

        for i in range(1, number_of_actions + 1):

            # l'action courant est celle présente en i-1
            (_, price, profit) = self.actions[i - 1]

            # création d'un sac à dos avec la combinaison de plusieurs actions
            for j in range(new_price, 0, -1):
                if price <= j:
                    sac_a_dos[j] = max(sac_a_dos[j], sac_a_dos[j - price] + self.get_value(price, profit))

            # ajouter une copie du sac à dos obtenu dans le tableau
            tableau.append(sac_a_dos[:])

            # quitter la boucle lorsque le profit maximal est découvert
            # et ceux lorsque la valeur du tableau est la même pour i et i-1
            # i correspond au nombre d'actions utilisées
            if tableau[i][minimal_profit:] == tableau[i - 1][minimal_profit:]:
                number_of_actions = i
                break

        # le profit maximal est contenu dans la variable max_profit
        max_profit = sac_a_dos[new_price]

        # la somme investit correspond au plus petit prix pour obtenir le profit maximal
        invest = min(
            [j for j in range(new_price + 1) if sac_a_dos[j] == max_profit]
        )
        total_price = invest / 100

        # boucler afin d'obtenir la combinaison correspondant au profit maximum
        # Lorsque la boucle passe sur le i minimum pour obtenir le profit maximum alors:
        #       le nom de l'action est ajouté dans la liste actions_name
        #       le profit de l'action est soustrait à max_profit
        #       le price de l'action est soustrait au prix de la combinaison
        for i in range(number_of_actions, 0, -1):
            if max_profit <= 0:
                break
            if max_profit == tableau[i - 1][invest]:
                continue
            (name, price, profit) = self.actions[i - 1]
            max_profit -= self.get_value(price, profit)
            invest -= price

            self.actions_name.append(name)

        return print('Actions achetées: ' + str(self.actions_name), '|| Profit: ' + str(sac_a_dos[new_price] / 100),
                     '|| Prix: ' + str(total_price))


run = Optimized()
time_1 = time.time()
run.get_optimized(500, "dataset2.csv")
time_2 = time.time()
print(round(time_2 - time_1, 2), "secondes")



