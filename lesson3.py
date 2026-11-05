playing = True

while playing:
    print("=== MYSTERY ISLAND ===")
    print("1. Expore the Beach")
    print("2. Expore the Jungle")
    print("3.Exit Game")

    choice = input("choose an option: ")

    if choice == "1":
        print("You are exploring the Beach")
    elif choice == "2":
        print("you are exploring the Jungle")
    elif choice == "3":
        print("Thank you for playing")
        playing = False
    else:
        print("Invalid input. Try Again!")            