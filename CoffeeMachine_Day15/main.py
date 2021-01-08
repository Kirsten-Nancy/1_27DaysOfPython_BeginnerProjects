from data import MENU, resources


def display_menu():
    """Display the coffee shop menu"""
    print("Our Coffee Menu:")
    for key, value in MENU.items():
        print(f"{key}: ${value['cost']}")


def print_report(my_resources, profit):
    """Takes the current available resources in the shop and generates a report
    for the user"""
    print("Available resources:")
    my_resources['money'] = profit
    for key, value in my_resources.items():
        print(f"{key}: {value}")


def remaining_resources(available_res, drink):
    """Takes the current available resources and calculates the remaining
    resources available after each drink has been made, returning the remainder as a dictionary."""
    # Ingredients the drink requires
    ingredients = MENU[drink]['ingredients']
    # print(ingredients)

    remainder = {}
    for key in ingredients:
        remainder[key] = available_res[key] - ingredients[key]

    return remainder


def check_available_resources(available_res, drink):
    """Receives current resource values and drink type and checks if
    the resources are sufficient to make the drink ordered by the user.
    Returns True if sufficient, else returns False."""
    ingredients = MENU[drink]['ingredients']

    for key in ingredients:
        # print(key)
        # To check the values
        if ingredients[key] > available_res[key]:
            print(f"Sorry there is not enough {key} to make your drink.")
            return False
    return True


# q-quarters(0.25), d-dimes(0.10), n-nickles(0.05),p-pennies(0.01)
def process_coins(q, d, n, p, drink):
    """Takes the money from the user and deducts the cost of the drink.
    If the money is sufficient it returns the change if needed. Else
    Refunds money back to the customer and returns False."""
    total_money = 0.25 * q + 0.10 * d + 0.05 * n + 0.01 * p
    drink_price = MENU[drink]['cost']
    change = 0.0
    profit = 0.0
    if total_money >= drink_price:
        change = total_money - drink_price
        profit = drink_price
    elif total_money < drink_price:
        print("Sorry, you have entered insufficient money. Money refunded.")
        print()
        return False
    return "{:.2f}".format(change), profit


total_profit = 0
current_resource_values = resources
off = False

while not off:
    display_menu()
    user_input = input("What would you like? ").lower()

    if user_input == 'off':
        break

    if user_input == 'report':
        print_report(current_resource_values, total_profit)
        continue

    if check_available_resources(current_resource_values, user_input):
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))

        # Returns false in case of insufficient money
        result = process_coins(quarters, dimes, nickles, pennies, user_input)

        if result:
            total_profit += result[1]
            # print(f"Profit: {total_profit}")
            print(f"Here's your change: ${result[0]}")
            print(f"Here's your {user_input}, enjoy!")
            print()

            current_resource_values = remaining_resources(current_resource_values, user_input)
        else:
            continue







# Alternative implementations ot the two functions, albeit longer
# def remaining_resources(available_res, drink):
#     """Takes the current available resources and calculates the remaining
#     resources available after each drink has been made, returning the remainder as a dictionary."""
#     # Ingredients the drink requires
#     ingredients = MENU[drink]['ingredients']
#     water = ingredients['water']
#     coffee = ingredients['coffee']
#     milk = ingredients.setdefault('milk', 0)
#
#     # Deduct the used resources from current available resources.
#     water_remaining = available_res['water'] - water
#     coffee_remaining = available_res['coffee'] - coffee
#     milk_remaining = available_res['milk'] - milk
#     remainder = {"water": water_remaining,
#                  "milk": milk_remaining,
#                  "coffee": coffee_remaining, }
#
#     return remainder
#
#
# def check_available_resources(available_res, drink):
#     """Receives current resource values and drink type and checks if
#     the resources are sufficient to make the drink ordered by the user.
#     Returns True if sufficient, else returns False."""
#     ingredients = MENU[drink]['ingredients']
#     water = ingredients['water']
#     coffee = ingredients['coffee']
#     milk = ingredients.setdefault('milk', 0)
#
#     if water > available_res['water']:
#         print("Sorry there is not enough water to make your drink.")
#         return False
#     elif coffee > available_res['coffee']:
#         print("Sorry, there is not enough coffee to make your drink.")
#         return False
#     elif milk > available_res['milk']:
#         print("Sorry, there is not enough milk to make your drink.")
#         return False
#     else:
#         # print("Sufficient resources")
#         return True
