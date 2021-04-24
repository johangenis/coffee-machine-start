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

# TODO: 5 Process coins.

# TODO: 6 Check transaction successful?

# TODO: 7 Make Coffee.
