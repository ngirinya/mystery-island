energy = 10
location = "Beach"
playing = True

inventory = ["Rope", "Lantern"]

while playing:
    print("=== MYSTERY ISLAND ===")
    print("1. Explore the Beach")
    print("2. Explore the Jungle")
    print("3. Explore the Cave")
    print("4. Check the Inventory")
    print("5. Check the Energy")
    print("6. Exit Game")
    print("7. Collect Treasure")

    choice = input("choose an option: ")


    if choice == "1":
        if energy > 0:
            location = "Beach"
            print("Move to Beach")
            energy -= 2
            print(f"Remaining energy: {energy}")
            if energy == 0:
                print("Game Over!")
                playing = False
        else:
            print("You have no energy left!")
            playing = False        
    elif choice == "2":
        if energy > 0:
            location = "Jungle"
            print("Move to Jungle")
            energy -= 2
            print(f"Remaining energy: {energy}")
            if energy == 0:
                print("Game Over!")
                playing = False
        else:
            print("You have no energy left!")
            playing = False        
    elif choice == "3":
        if energy > 0:
            location = "Cave"
            print("Move to Cave")
            energy -= 2
            print(f"Remaining energy: {energy}")
            if energy == 0:
                print("Game Over!")
                playing = False
        else:
            print("You have no energy left!")
            playing = False        
    elif choice == "4":
        print(inventory)
    elif choice == "5":
        print(energy)
    elif choice == "6":
        print("Game Over. Goodbye")
        playing = False
    elif choice == "7":
        treasure = input("Which treasure do you want to collect? ")
        if treasure not in inventory:
            inventory.append(treasure)
            print(inventory)
        else:
            print("You already have this treasure")       
    else:
        print("Invalid choice. Please select an option from 1 to 7.")
        
              


