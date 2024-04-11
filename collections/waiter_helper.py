# Menu List
starters = ["Tomato Soup", "Garlic Bread", "Chicken Wings"]
mains = ["Spaghetti Bolognese", "Margherita Pizza", "Chilli Con Carne"]
desserts = ["Tiramisu", "Vanilla Sundae", "Chocolate Fudge Cake"]

# Level 4 --> Validate input function
def validate_order_input(order, options):
    while True:
        user_input = input(order)
        if user_input in options:
            return user_input
        else:
            print("This item does not exist in our menu, Please choose from the provided options!")

# Greet the customer
print("Hello and Welcome to our restaurant!")
# Print a list of starters, saving the customer's order
ordered_starter = validate_order_input(f"Here is a list of our starters: {str(starters)}, What would you like to order? ", starters)
#print(ordered_starter)

# Print a list of main courses, saving the customer's order
ordered_main = validate_order_input(f"Here is a list of our main courses: {str(mains)}, What would you like to order? ", mains)
#print(ordered_main)

# Print a list of desserts, saving the customer's order
ordered_dessert = validate_order_input(f"Here is a list of our desserts: {str(desserts)}, What would you like to order? ", desserts)
#print(ordered_dessert)

# Put the order into a list
customer_order_list = [ordered_starter, ordered_main, ordered_dessert]

# Print out the customer's order
print(f"This is your order: {customer_order_list} ")

# Level 3 --> Use dictionaries and now assign prices to items
price_dictionary = {
    starters[0]: 4,
    starters[1]: 5,
    starters[2]: 6,
    mains[0]: 15,
    mains[1]: 17,
    mains[2]: 19,
    desserts[0]: 9,
    desserts[1]: 6,
    desserts[2]: 3
}

bill = 0
if ordered_starter in price_dictionary:
    bill += price_dictionary[ordered_starter]
if ordered_main in price_dictionary:
    bill += price_dictionary[ordered_main]
if ordered_dessert in price_dictionary:
    bill += price_dictionary[ordered_dessert]
print(f"Your final bill total is £{bill}")