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
    lighthouse_unlocked = False

    inventory = []

    treasure_items = ["Golden Key", "Old Map", "Silver Coin"]

    clue_items = [
        "A broken lighthouse map",
        "An old lighthouse symbol",
        "A mysterious lighthouse message"
    ]

    clues_found = []
    
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
    max_energy = energy
    rest_count = 0
        

    print(f"Starting Energy: {energy}")
    print(f"Starting Health: {health}")


    
    while True:  
        print("\nChoose where you want to explore:")
        print("1. Beach")
        print("2. Jungle")
        print("3. Cave")
        print("4. Enter the Lost Lighthouse")
        print("5. Check Inventory")
        print("6. Quit")
        print("7. Rest and Restore Energy")
        
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
                if "Golden Key" in inventory:
                    print("Golden key fits!.")
                    print("The hidden room is unlocked.")
                    print("CONGRATULATION! YOU WIN.")
                    break
                else:
                    print("You need  a Golden key to unlock the hidden room.")
                    continue   
            else:
                print("The Lighthouse is locked")
                print("Find three clues before entering")
                continue 
        elif choice == "5":
            print("\nYOUR INVENTORY")

            if inventory:
                for item in inventory:
                    print(f"- {item}")

            else:
                print("Your inventory is empty.")
            continue
        elif choice == "7":
            if rest_count >= 2:
                print("You  used all your opportunities.")
            elif energy >= max_energy:
                print("Your energy is already full. You do not need rest.")
            else:
                energy_restored = min(30, max_energy - energy)
                energy += energy_restored
                rest_count += 1

                print("You take a rest")
                print(f"Energy Restored: {energy_restored}")
                print(f"Current Energy: {energy}")
                print(f"Rest opportunities remaining: {2 - rest_count}")
            continue                             
        elif choice == "6":
            print("Thanks for playing")
            break    
        else:
            print("Invalid location.Please choose from 1 to 7.")
            continue    

        energy_cost *= energy_multiplier

        if energy >= energy_cost:
            energy -= energy_cost
            print(f"\nYou explored the {location}!")
            print(f"\nEnergy consumed: {energy_cost}")
            print(f"Energy remaining: {energy}")

            score += points_earned
            exploration_count += 1
            
            print(f"Points earned: {points_earned}")
            print(f"Total score: {score}")

            event = random.randint(1, 10)

            if event <= 2:
                print("You discovered hidden treasure!")
                found_item = random.choice(treasure_items)
                if found_item not in inventory:
                    inventory.append(found_item)
                    print(f"You collected: {found_item}")
                else:
                    print(f"You have the: {found_item}")    
                score += 10
                print("Bonus points: 10")
                print(f"New total score: {score}")
            elif event <= 5:
                print("Oh no! You encountered a trap!")
                if health >= trap_damage:
                    health -= trap_damage
                else:
                    health = 0

                print(f"Health remaining: {health}")
            elif event <= 7:
                available_clues = [
                    clue for clue in clue_items
                    if clue not in clues_found 
                ]
                if available_clues:
                    found_clue = random.choice(available_clues)
                    clues_found.append(found_clue)

                    print(f"You discovered: {found_clue}")
                    print(f"Total clues found: {len(clues_found)}")
                else:
                    print("You have already discovered all the clues.")        
            else:
                print("Nothing unusual happens.")

            if len(clues_found) >= 3 and not lighthouse_unlocked:
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