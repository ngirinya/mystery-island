import random
def main():
    print("===============================")
    print("   MYSTERY-ISLAND")
    print("      THE LOST LIGHTHOUSE")
    print("===============================")

    player_name = input("What is your name? ").strip()

    while player_name == "":
        print("Name cannot be empty.")
        player_name = input("What is your name? ").strip()

    
    score = 0
    exploration_count = 0
    clues_found = 0
    lighthouse_unlocked = False

    print(f"Player: {player_name}")
    while True:
        difficulty = input("choose difficulty (easy/normal/hard): ").strip().lower()
        if difficulty == "easy":
            energy = 150
            health = 150
            energy_multiplier = 1
            trap_damage = 5
            break
        elif difficulty == "normal":
            energy = 100
            health = 100
            energy_multiplier = 1.5
            trap_damage = 10
            break
        elif difficulty == "hard":
            energy = 70
            health = 70
            energy_multiplier = 2
            trap_damage = 20
            break
        else:
            print("Invalid difficulty. Please choose again.")

    print(f"Starting Energy: {energy}")
    print(f"Starting Health: {health}")

    min_energy_cost = 10 * energy_multiplier            


    while True:
        if energy < min_energy_cost:
            print("you do not have enough to continue.")
            break

        print("\nChoose where you want to explore:")
        print("1. Beach")
        print("2. Jungle")
        print("3. Cave")
        print("4. Enter the Lost Lighthouse")
        print("5. Quit")
        
        choice = input("Choose a location: ").strip()
        
        if choice == "1":
            location = "Beach"
            energy_cost = 10
            points_earned = 5   
        elif choice == "2":
            location = "Jungle"
            energy_cost = 20
            points_earned = 10
        elif choice == "3":
            location = "Cave"
            energy_cost = 30
            points_earned = 15
        elif choice == "4":
            if lighthouse_unlocked:
                print("\nYou enter the lost Lighthouse.")
                print("You have found the source of the island's mystery!.")
                print("CONGRATULATION! YOU WIN.")
                break
            else:
                print("The Lighthouse is locked")
                print("Find three clues before entering")
                continue      
        elif choice == "5":
            print("Thanks for playing")
            break    
        else:
            print("Invalid loaction.Please choose from 1 to 4.")
            continue

        energy_cost *= energy_multiplier

        if energy >= energy_cost:
            energy -= energy_cost
            print(f"\nYou explored the {location}!")
            print(f"\nEnergy consumed: {energy_cost}")
            print(f"Energy remaining: {energy}")

            score += points_earned
            exploration_count += 1
            clues_found += 1

            print(f"Points earned: {points_earned}")
            print(f"Total score: {score}")
            print(f"Total clues found: {clues_found}")

            event = random.randint(1, 10)

            if event <= 2:
                print("You discovered hiddin treasure!")
                score += 10
                print("Bouns points: 10")
                print(f"New total score: {score}")
            elif event <= 5:
                print("Oh no! You encountered a trap!")
                if health >= trap_damage:
                    health -= trap_damage
                else:
                    health = 0

                print(f"Healt remaining: {health}")    

            else:
                print("Nothing unusual happens.")

            if clues_found >= 3 and not lighthouse_unlocked:
                lighthouse_unlocked = True
                print("\nCongratulation!")
                print("You have discovered all three clues!.")
                print("THE LOST LIGHTHOUSE IS NOW UNLOCKED.")              

        else:
            print("You do not have enough energy")
            continue
 
        if energy <= 0 or health <= 0:
            print("You have run out of energy or health. Game Over.")
            break
    print("\n========== GAME SUMMARY ==========")
    print(f"Player: {player_name}")
    print(f"Final Energy: {energy}")
    print(f"Final Score: {score}")
    print(f"Final Health: {health}")
    print(f"Successful Explorations: {exploration_count}")
    print("==================================")                    

if __name__ == "__main__":
    main()