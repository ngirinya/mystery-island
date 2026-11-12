def show_title():
    print("==============================")
    print("       MYSTERY ISLAND")
    print("     THE LOST LIGHTHOUSE")
    print("==============================")


def show_welcome():
    print("\nWelcome to Mystery Island!")
    print("You have awakened on a mysterious island.")
    print("Your starting location is the Beach.")


def show_menu(location):
    print("\nWhere would you like to go?")

    if location == "Beach":
        print("1. Move to Jungle")

    elif location == "Jungle":
        print("1. Move to Cave")
        print("5. Return to Beach")

    elif location == "Cave":
        print("1. Move to Old Bridge")
        print("5. Return to Jungle")

    elif location == "Old Bridge":
        print("1. Move to Lighthouse")
        print("5. Return to Cave")

    elif location == "Lighthouse":
        print("1. Light the Lighthouse beacon")
        print("5. Return to Old Bridge")

    print("2. Collect an item")
    print("3. Check inventory")
    print("4. Quit")


def move_player(location, inventory):
    won = False

    if location == "Beach":
        location = "Jungle"
        print("You have moved to the Jungle.")

    elif location == "Jungle":
        location = "Cave"
        print("You have moved to the Cave.")

    elif location == "Cave":
        if "Rope" in inventory:
            location = "Old Bridge"
            print("You have crossed safely to the Old Bridge.")
        else:
            print("You need a Rope to cross safely!")

    elif location == "Old Bridge":
        location = "Lighthouse"
        print("You have arrived at the Lighthouse!")

    elif location == "Lighthouse":
        if "Lantern" in inventory:
            print("You use your lantern to light the beacon!")
            print("Congratulations! You have won the game!")
            won = True
        else:
            print("You need a Lantern to light the beacon.")

    return location, won


def move_backward(location):
    old_location = location

    if location == "Jungle":
        location = "Beach"
        print("You have returned to the Beach.")

    elif location == "Cave":
        location = "Jungle"
        print("You have returned to the Jungle.")

    elif location == "Old Bridge":
        location = "Cave"
        print("You have returned to the Cave.")

    elif location == "Lighthouse":
        location = "Old Bridge"
        print("You have returned to the Old Bridge.")

    else:
        print("You cannot move backward from the Beach.")

    moved = location != old_location

    return location, moved