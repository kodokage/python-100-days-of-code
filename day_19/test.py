test_list = []

for item in range(3):
    test_dict = dict(name = f"{item}", age = item)
    print(test_dict)
    print(test_dict["name"])
    test_list.append(test_dict)

print(test_list)