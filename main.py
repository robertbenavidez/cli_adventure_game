import game

from blessings import Terminal


def main():
    # clear terminal window
    term = Terminal()
    print(term.clear())
    # game loop: play the game until the game is over or the player quits
    game.play_game()


if __name__ == "__main__":
    main()
