def main():
    print("===============================")
    print("   MYSTERY-ISLAND")
    print("      THE LOST LIGHTHOUSE")
    print("===============================")

    while player_name == "":
        print("Name cannot be empty.")
        player_name = input("What is your name? ").strip()

    
    energy = 100

    print(f"Player: {player_name}")
    print(f"Starting Energy: {energy}")


if __name__ == "__main__":
    main()