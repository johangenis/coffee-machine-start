from data import menu, resources, money

machine_on = True

transaction_done = False

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


while machine_on and not transaction_done:

    def format_data(resources, money):
        """
        Format resources and money into a printable format to produce a
        report on the quantities of: water, milk, coffee and money.
        """

        quarters_amount = (
            money["quarters"]["value"] * money["quarters"]["count"]
        )
        dimes_amount = money["dimes"]["value"] * money["dimes"]["count"]
        nickles_amount = money["nickles"]["value"] * money["nickles"]["count"]
        pennies_amount = money["pennies"]["value"] * money["pennies"]["count"]
        total_amount = (
            quarters_amount + dimes_amount + nickles_amount + pennies_amount
        )

        return f"Water: {water}ml\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${total_amount}"

    # 4 Check resources sufficient?
    def check_resources(user_choice):

        choice = []
        espresso = menu["espresso"]
        latte = menu["latte"]
        cappuccino = menu["cappuccino"]

        if user_choice == "espresso":
            if water < espresso["ingredients"]["water"]:
                return f"Sorry, there is not enough water in the machine to make your espresso."
            elif milk < espresso["ingredients"]["milk"]:
                return f"Sorry, there is not enough milk in the machine to make your espresso."
            elif coffee < espresso["ingredients"]["coffee"]:
                return f"Sorry, there is not enough coffee in the machine to make your espresso."
            water_level = water - espresso["ingredients"]["water"]
            milk_level = milk
            coffee_level = coffee - espresso["ingredients"]["coffee"]
            cost = espresso["cost"]
            choice = [water_level, milk_level, coffee_level, cost]

        elif user_choice == "latte":
            if water < latte["ingredients"]["water"]:
                return f"Sorry, there is not enough water in the machine to make your latte."
            elif milk < latte["ingredients"]["milk"]:
                return f"Sorry, there is not enough milk in the machine to make your latte."
            elif coffee < latte["ingredients"]["coffee"]:
                return f"Sorry, there is not enough coffee in the machine to make your latte."
            water_level = water - latte["ingredients"]["water"]
            milk_level = milk - latte["ingredients"]["milk"]
            coffee_level = coffee - latte["ingredients"]["coffee"]
            cost = latte["cost"]
            choice = [water_level, milk_level, coffee_level, cost]

        elif user_choice == "cappuccino":
            if water < cappuccino["ingredients"]["water"]:
                return f"Sorry, there is not enough coffee in the machine to make your cappuccino."
            elif milk < cappuccino["ingredients"]["milk"]:
                return f"Sorry, there is not enough milk in the machine to make your cappuccino."
            elif coffee < cappuccino["ingredients"]["coffee"]:
                return f"Sorry, there is not enough coffee in the machine to make your cappuccino."
            water_level = water - cappuccino["ingredients"]["water"]
            milk_level = milk - cappuccino["ingredients"]["milk"]
            coffee_level = coffee - cappuccino["ingredients"]["coffee"]
            cost = cappuccino["cost"]
            choice = [water_level, milk_level, coffee_level, cost]

        return choice

    # 1 Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino):"
    ).lower()

    # 2. Turn off the Coffee Machine by entering "off" at the prompt.
    if user_choice == "off":
        print(f"Machine was turned off.")
        machine_on = False
    # 3. Print report.
    elif user_choice == "report":
        print(format_data(resources, money))
    else:
        resources = check_resources(user_choice)
        print(f"{resources}")
        # resources_after_purchase = check_resources(user_choice)
        # water = resources_after_purchase[0]
        # milk = resources_after_purchase[1]
        # coffee = resources_after_purchase[2]
        # cost = resources_after_purchase[3]
        # print(f"Choice when called: {resources_after_purchase}")


# TODO: 5 Process coins.

# TODO: 6 Check transaction successful?

# TODO: 7 Make Coffee.
