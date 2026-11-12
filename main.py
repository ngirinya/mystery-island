from game import (
    show_title,
    show_welcome,
    show_menu,
    move_player,
    move_backward
)

from player import (
    get_player_name,
    use_energy,
    play_again
)

from inventory import (
    show_inventory,
    collect_item
)


def main():
    show_title()
    show_welcome()

    player_name = get_player_name()

    print(f"Welcome, {player_name}!")

    quit_game = False

    while True:
        location = "Beach"
        inventory = []
        energy = 5

        print("\nA new adventure begins!")

        while True:
            print(f"\nCurrent location: {location}")
            print(f"Current energy: {energy}")

            show_menu(location)

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                old_location = location

                location, won = move_player(location, inventory)

                if won:
                    break

                if location != old_location:
                    energy = use_energy(energy)
                    print(f"You used 1 energy. Remaining energy: {energy}")

            elif choice == "5":
                location, moved = move_backward(location)

                if moved:
                    energy = use_energy(energy)
                    print(f"You used 1 energy. Remaining energy: {energy}")

            elif choice == "2":
                collect_item(location, inventory)

            elif choice == "3":
                show_inventory(inventory)

            elif choice == "4":
                print("Thanks for playing Mystery Island!")
                quit_game = True
                break

            else:
                print("Invalid choice. Please choose 1, 2, 3, 4 or 5.")

            if energy <= 0:
                print("You have run out of energy!")
                print("GAME OVER! You lost.")
                break

        if quit_game:
            break

        if not play_again():
            print("Thanks for playing Mystery Island!")
            break


if __name__ == "__main__":
    main()