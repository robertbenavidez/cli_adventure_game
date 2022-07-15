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
        player_input = input('->')

        if player_input == 'help':
            print('help goes here')
        elif player_input == 'quit':
            # TODO: print final score
            print('Fleeing the Dungeon you leave the village in peril.')
            play_again()

        else:
            print('Incorrect command. Please type help to find the proper commands')


# restart game function
# TODO: currently the function quites with any command other than 'yes'
def play_again():
    yn = input('Play again? (yes/no) ->')

    if yn == 'yes':
        play_game()
    else:
        print('Until next time...')
        exit(0)


