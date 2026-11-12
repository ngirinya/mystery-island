def get_player_name():
    player_name = input("What is your name? ").strip()

    while player_name == "":
        print("Name cannot be empty.")
        player_name = input("What is your name? ").strip()

    return player_name


def use_energy(energy, amount=1):
    energy -= amount

    if energy < 0:
        energy = 0

    return energy


def play_again():
    replay = input(
        "\nWould you like to play again? (yes/no): "
    ).strip().lower()

    while replay not in ("yes", "no"):
        print("Invalid answer. Please enter yes or no.")
        replay = input("Play again? ").strip().lower()

    return replay == "yes"