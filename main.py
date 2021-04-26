from data import menu, resources, money

machine_on = True

while machine_on:

    def format_data(resources, money):
        """
        Format resources and money into a printable format to produce a
        report on the quantities of: water, milk, coffee and money.
        """

        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
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

    def check_resources(user_choice):
        choice = ""
        espresso = menu["espresso"]
        latte = menu["latte"]
        cappuccino = menu["cappuccino"]

        # format_data(resources, money)

        if user_choice == "espresso":
            print(f"You have chosen: {espresso}")
            water_level = resources["water"] - espresso["ingredients"]["water"]
            milk_level = resources["milk"]  # - espresso["ingredients"]["milk"]
            coffee_level = resources["coffee"]
            choice = f"Water Level: {water_level}\nMilk Level: {milk_level}\nCoffee Level: {coffee_level}"

        elif user_choice == "latte":
            print(f"You have chosen: {latte}")
            water_level = water - menu["latte"]["ingredients"]["water"]
            milk_level = milk - menu["latte"]["ingredients"]["milk"]
            coffee_level = coffee - menu["latte"]["ingredients"]["coffee"]
            choice = f"Water Level: {water_level}\nMilk Level: {milk_level}\nCoffee Level: {coffee_level}"

        elif user_choice == "cappuccino":
            print(f"You have chosen: {cappuccino}")
            water_level = water - menu["cappuccino"]["ingredients"]["water"]
            milk_level = milk - menu["cappuccino"]["ingredients"]["milk"]
            coffee_level = coffee - menu["cappuccino"]["ingredients"]["coffee"]
            choice = f"Water Level: {water_level}\nMilk Level: {milk_level}\nCoffee Level: {coffee_level}"

        return choice

    # TODO: 1 Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
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
    # TODO: 4 Check resources sufficient?
    else:
        check_resources(user_choice)


# TODO: 5 Process coins.

# TODO: 6 Check transaction successful?

# TODO: 7 Make Coffee.
