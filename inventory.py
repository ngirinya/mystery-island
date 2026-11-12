def show_inventory(inventory):
    print("\nYour inventory:")

    if inventory:
        for item in inventory:
            print(item)
    else:
        print("Your inventory is empty.")


def collect_item(location, inventory):
    if location == "Jungle":
        item = "Rope"

    elif location == "Cave":
        item = "Lantern"

    else:
        print("There is nothing to collect here.")
        return

    if item not in inventory:
        inventory.append(item)
        print(f"You collected the {item}!")
    else:
        print(f"You already have the {item}.")