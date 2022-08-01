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
    input(f"{Fore.CYAN}Press ENTER to continue")
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

        # show game help
        if player_input == 'help':
            show_help()
            continue
        # grab item
        elif player_input.startswith("get"):
            if not current_game.room.items:
                print("There is nothing to pick up.")
                continue
            else:
                get_an_item(current_game, player_input)

        elif player_input == "inventory" or player_input == "inv":
            show_inventory(current_game)
            continue

        # move around the map
        elif player_input in ["n", "s", "e", "w"]:
            print(f"{Fore.GREEN} You move deeper into the dungeon.")
            continue
        # quit the game
        elif player_input == 'quit':
            # TODO: print final score
            print(f'{Fore.GREEN}Fleeing the Dungeon you leave the village in peril.')
            play_again()

        else:
            print('Incorrect command. Please type help to find the proper commands')


def show_inventory(current_game: Game):
    print(f"{Fore.CYAN} Your inventory:")
    for x in current_game.player.inventory:
        print(f"    - {x.capitalize()}")


def get_an_item(current_game, player_input):
    if len(current_game.room.items) > 0 and player_input[4:] == "":
        player_input = player_input + " " + current_game.room.items[0]["name"]

    # only adds an item that is not in the player inventory
    if player_input[4:] not in current_game.player.inventory:
        idx = find_in_list(player_input[4:], "name", current_game.room.items)

        if idx > -1:
            cur_item = current_game.room.items[idx]
            current_game.player.inventory.append(cur_item["name"])
            current_game.room.items.pop(idx)
            print(f"{Fore.CYAN} You picked up a {cur_item['name']}.")

    else:
        print(f"{Fore.YELLOW} You already have a {player_input[4:]}")


def find_in_list(search_string: str, key: str, list_to_search: list) -> int:
    idx = -1
    count = 0
    for item in list_to_search:
        if item[key] == search_string:
            idx = count
        count += 1
    return idx


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
