menu_pizza = {}
all_ingredients = ["Brie", "Emmental", "Compté", "Parmesan", "Tomate", "Ananas", "Oigons", "Oeuf", "Jambon", "Olives"]

class Pizza:

    def __init__(self, name):
        self.name = name

        menu_pizza[name]= {
            "name": name,
            "price": 7,
            "vegan": True,
            "ingredients": []
        }


    def ingredient(self, produit):
        if produit in ["Oeuf", "Jambon"]:
            menu_pizza[self.name]["vegan"] = False

        menu_pizza[self.name]["ingredients"].append(produit)
        menu_pizza[self.name]["price"] = menu_pizza[self.name]["price"] + 1.2


    def menuPizza():
        print(" ")
        print("Menu du restaurant :")

        for pizza in menu_pizza:
            vegan = ""

            if menu_pizza[pizza]["vegan"] == True:
                vegan = " - Végétarien"

            print("Pizza "+ menu_pizza[pizza]["name"]+" : "+str(round(menu_pizza[pizza]["price"], 3))+" €"+vegan)

            arrays = ""
            for ingredients in menu_pizza[pizza]["ingredients"]:
                arrays += ingredients+", "

            print(arrays)
            print(" ")

class Pizza_perso(Pizza):
    def __init__(self, name):
        Pizza.__init__(self, name)


    def list_ingredients():
        print("Liste des ingrédients :")

        for ingredients in all_ingredients:
            print("  - "+ingredients)

        print(" ")


    def calcul_price_pizza(self):
        nb = int(input("   - Vous voulez combien d'ingrédients dans votre pizza ? "))

        calcul = (nb * 1.2) + 7

        print("   - Votre pizza vous coutera "+ str(calcul)+ "€ pour "+ str(nb) + " ingrédient(s)")
        print("   - "+str(nb)+" ingrédients x 1.2 + 7€ de prix de base")

        return nb


    def create_pizza(self):
        i = 1
        
        print("Ingrédients pour la pizza "+ self.name)

        nb = self.calcul_price_pizza()

        while i <= nb:
            produit = input("   - Ajoutez un ingrédient (ou ENTREZ pour terminer) : ")

            if len(produit) > 0:
                Pizza.ingredient(self, str(produit))

                arrays = ""
                for ingredients in menu_pizza[self.name]["ingredients"]:
                    arrays += ingredients+", "
                
                print("   - Vous avez "+ str(len(menu_pizza[self.name]["ingredients"]))+ " ingrédients(s) : "+ arrays)
                print(" ")
            else:
                break
            i += 1

        
Pizza_perso.list_ingredients()

pizza_perso_1 = Pizza_perso("Personnalisée 1")
pizza_perso_1.create_pizza()

pizza_perso_2 = Pizza_perso("Personnalisée 2")
pizza_perso_2.create_pizza()

pizza_4_Fromages = Pizza_perso("4 Fromages")
pizza_4_Fromages.ingredient("Brie")
pizza_4_Fromages.ingredient("Emmental")
pizza_4_Fromages.ingredient("Compté")
pizza_4_Fromages.ingredient("Parmesan")

pizza_Hawai = Pizza_perso("Hawai")
pizza_Hawai.ingredient("Tomate")
pizza_Hawai.ingredient("Ananas")
pizza_Hawai.ingredient("Oigons")

pizza_4_Saisons = Pizza_perso("4 Saisons")
pizza_4_Saisons.ingredient("Oeuf")
pizza_4_Saisons.ingredient("Emmental")
pizza_4_Saisons.ingredient("Tomate")
pizza_4_Saisons.ingredient("Jambon")
pizza_4_Saisons.ingredient("Olives")

pizza_Vegan = Pizza_perso("Végétarien")
pizza_Vegan.ingredient("Oeuf")
pizza_Vegan.ingredient("Emmental")
pizza_Vegan.ingredient("Tomate")
pizza_Vegan.ingredient("Jambon")
pizza_Vegan.ingredient("Olives")

Pizza.menuPizza()

