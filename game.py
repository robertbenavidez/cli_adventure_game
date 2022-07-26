import random
import armory
import bestiary
from classes import Player, Room, Game
from colorama import Fore, init


# welcome prints out the welcome text
def welcome():
    print(Fore.RED + "                                                 DUNGEON ADVENTURE")

    print(Fore.GREEN + """
    The village of Dogwood has been terrorized by strange, deadly creatures for months now. Unable to endure any 
    longer, the villagers pooled their wealth and hired the most skilled adventurer they could find: you. After
    listening to their tale of woe, you agree to enter the labyrinth where most of the creatures seem to originate,
    and destroy the foul beasts. Armed with a longsword and a bundle of torches, you descend into the labyrinth, 
    ready to do battle....
    """)


def play_game():
    # makes sure colorama works on various operating systems
    init()

    adventurer = Player()

    current_game = Game(adventurer)

    welcome()
    input('Press ENTER to continue')
    explore_labyrinth(current_game)


# generate a room
def generate_room() -> Room:
    items = []
    monster = {}

    # There is a 25% chance an item is in this room.
    if random.randint(1, 100) < 26:
        i = random.choice(list(armory.items.values()))
        items.append(i)

    # There is a 25% chance a monster is in this room.
    if random.randint(1, 100) < 26:
        monster = random.choice(bestiary.monsters)

    return Room(items, monster)


def explore_labyrinth(current_game: Game):
    while True:
        room = generate_room()

        current_game.room = room

        current_game.room.print_description()

        for i in current_game.room.items:
            print(f"{Fore.YELLOW}You see a {i['name']}")
        player_input = input(Fore.LIGHTYELLOW_EX + '->').lower().strip()

        if current_game.room.monster:
            print(f"{Fore.RED}There is a {current_game.room.monster['name']} here!")

        if player_input == 'help':
            show_help()

        elif player_input in ["n", "s", "e", "w"]:
            print(f"{Fore.GREEN} You move deeper into the dungeon.")
            continue
        # quit the game
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


def get_yn(question: str) -> str:
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
    print(Fore.GREEN + """Enter a command
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
