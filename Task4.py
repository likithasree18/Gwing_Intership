def intro():
    print("\nWelcome to the Adventure Game!")
    print("You are standing at the edge of a dark forest.")
    print("There are rumors of treasure hidden deep inside.")
    print("Will you dare to enter?\n")
    choice = input("Enter 'yes' to enter the forest or 'no' to walk away: ").lower()
    if choice == 'yes':
        forest_path()
    elif choice == 'no':
        print("\nYou chose safety. Sometimes, it's wise not to risk it all.")
        end_game("Game Over.")
    else:
        print("Invalid choice. Try again.")
        intro()

def forest_path():
    print("\nYou walk into the forest. It's quiet... too quiet.")
    print("Soon, you reach a fork in the path.")
    choice = input("Do you go 'left' toward the river or 'right' into the thick trees? ").lower()
    if choice == 'left':
        river_scene()
    elif choice == 'right':
        wolves_scene()
    else:
        print("Invalid choice. Try again.")
        forest_path()

def river_scene():
    print("\nYou walk towards the sound of flowing water and find a wide river.")
    print("You see a small boat and a bridge that looks unstable.")
    choice = input("Do you take the 'boat' or cross the 'bridge'? ").lower()
    if choice == 'boat':
        treasure_island()
    elif choice == 'bridge':
        bridge_falls()
    else:
        print("Invalid choice. Try again.")
        river_scene()

def wolves_scene():
    print("\nYou push through the trees but suddenly hear growling.")
    print("A pack of wolves surrounds you.")
    choice = input("Do you 'climb' a tree or try to 'run'? ").lower()
    if choice == 'climb':
        safe_tree()
    elif choice == 'run':
        wolves_attack()
    else:
        print("Invalid choice. Try again.")
        wolves_scene()

def treasure_island():
    print("\nYou paddle across the river and reach a small island.")
    print("Behind a tree, you find a chest filled with gold and jewels!")
    end_game("Congratulations! You found the treasure!")

def bridge_falls():
    print("\nYou step onto the bridge, but halfway across, it collapses!")
    print("You fall into the river and are swept away by the current.")
    end_game("You didn't make it. Game Over.")

def safe_tree():
    print("\nYou climb the tree quickly. The wolves circle below but eventually leave.")
    print("From the tree, you spot a hidden cave nearby.")
    choice = input("Do you go to the 'cave' or head back 'home'? ").lower()
    if choice == 'cave':
        cave_treasure()
    elif choice == 'home':
        print("\nYou return home safely, but empty-handed.")
        end_game("You survived, but the treasure remains a mystery.")
    else:
        print("Invalid choice. Try again.")
        safe_tree()

def wolves_attack():
    print("\nYou try to run, but the wolves are too fast.")
    end_game("You were caught. Game Over.")

def cave_treasure():
    print("\nYou sneak into the cave. It's dark but you find glowing stones.")
    print("Inside, there's a treasure chest filled with ancient coins.")
    end_game("You found the hidden cave treasure! Well done!")

def end_game(message):
    print(f"\n{message}")
    print("Thank you for playing!\n")
    restart = input("Do you want to play again? (yes/no): ").lower()
    if restart == 'yes':
        intro()
    else:
        print("Goodbye!")

# Start the game
if _name_ == "_main_":
    intro()