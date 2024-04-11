list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3],
                  [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"},
             2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

for data in list_data:
    print(data * 2)

for list in embedded_lists:
    print(list)
    for item in list:
        print(item)

for data in dict_data:
    print(data)

for value in dict_data.values():
    print(value)

for value in dict_data.values():
    print(value)
    for item in value.values():
        print(item)

for value in dict_data.values():
    print(value["money"])

for data in list_data:
    if data < 3:
        print("Less than 3")
    elif data == 3:
        print("I found three")
    elif data > 3:
        print("Greater than 3")