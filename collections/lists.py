# Lists

# Collections are a way to store multiple pieces of data in one reference/object
# Lists are the most common/simplest collection

# Lists are often known as arrays in other languages
# Create a list called shopping_list with the following items: eggs, bread, bananas, biscuit, milk

shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

# Print the list to the screen
print(shopping_list)
print("This is your shopping list: " + str(shopping_list))

# Print the data type of shopping_list
print(f"The data type of your shopping list is {type(shopping_list)}")

# Print the first item in the list
print(f"The first item in our list is: {shopping_list[0]}")

# Print the last item in the list
print(f"The last item in our list is: {shopping_list[-1]}")

# Change the second item in the list (i.e. bread) to rice instead, then print to show this change
shopping_list[1] = "rice"
print(f"The last item in our list is: {shopping_list[1]}")

# Use the lists method to add the item 'carrots' to the list (should not use =), then check length of the list
shopping_list.append("carrots")
print("Our list is now this length:", len(shopping_list))

# Add another list with two items (toffee and coffee) to the shopping_list, use one of the list's method to add the two items in one go
extra_items = ["toffee", "coffee"]
shopping_list.extend(extra_items)

# Print the shopping_list to check toffee and coffee have been added correctly
print(shopping_list)

# Remove bananas from the shopping list, print the new shopping_list
shopping_list.remove("bananas")
print(shopping_list)

# Remove the last item, coffee, from shopping_list using the pop method. Print the new shopping list
shopping_list.pop()
print(shopping_list)

# Use the append method to add a new item to the list
shopping_list.append("watermelon")
print(shopping_list)

# Find a way to add a new list to our shopping list
new_items = ["lettuce", "cream"]
shopping_list.extend(new_items)

# Use the remove method to remove an item to your list
shopping_list.remove("biscuits")
print(shopping_list)

# Find a way to remove the last item from the list without referencing it
shopping_list.pop()
print(shopping_list)