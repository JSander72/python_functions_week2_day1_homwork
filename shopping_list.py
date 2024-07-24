def add_item(shopping_list):
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

def remove_item(shopping_list):
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def print_list(shopping_list):
    if shopping_list:
        print("Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")
def main():
    shopping_list = []

    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Show shopping list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
