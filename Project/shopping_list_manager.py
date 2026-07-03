
shopping_list = []

print("\nPlease enter 5 items:")
for i in range(5):
    item = input("Enter an item: ")
    shopping_list.append(item)

print("\n")

num = 1
for item in shopping_list:
    print(f"{num}. {item}")
    num = num + 1 

print(f"\nTotal Items = {len(shopping_list)}\n")