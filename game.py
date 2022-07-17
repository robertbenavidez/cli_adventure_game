def welcome():
    print("                                                 DUNGEON ADVENTURE")

    print("""
    The village of Dogwood has been terrorized by strange, deadly creatures for months now. Unable to endure any 
    longer, the villagers pooled their wealth and hired the most skilled adventurer they could find: you. After
    listening to their tale of woe, you agree to enter the labyrinth where most of the creatures seem to originate,
    and destroy the foul beasts. Armed with a longsword and a bundle of torches, you descend into the labyrinth, 
    ready to do battle....
    """)


def play_game():
    welcome()
    input('Pres ENTER to continue')
    explore_labyrinth()


def explore_labyrinth():
    while True:
        player_input = input('->').lower().strip()

        if player_input == 'help':
            show_help()
        elif player_input == 'quit':
            # TODO: print final score
            print('Fleeing the Dungeon you leave the village in peril.')
            play_again()

        else:
            print('Incorrect command. Please type help to find the proper commands')


# restart game function
def play_again():
    yn = get_yn("Play again?")

    if yn == 'yes':
        play_game()
    else:
        print('Until next time...')
        exit(0)


def get_yn(question):
    while True:
        answer = input(question + " (yes/no) -> ").lower().strip()
        if answer not in ["yes", "no", "y", "n"]:
            print("Please enter yes or no.")
        else:
            if answer == "y":
                answer = "yes"
            elif answer == "n":
                answer = "no"
            return answer


def show_help():
    print("""Enter a command
    - n/s/e/w - move in a direction
    - map - show a map and of the dungeon 
    - look - look around and describe your environment
    - equip - <item> - use an item from your inventory
    - unequip <item> stop using an item from your inventory
    - fight - attach a foe
    - examine <object> - examine an object more closely
    - get <item> - pick up an item 
    - drop <item> - drop an item
    - rest - restore some health by resting
    - inventory - show current player inventory
    - status - show current player status
    - quit - end the game""")
