import game


def main():
    game.welcome()

    # game loop: play the game until the game is over or the player quits
    while True:
        game.play_game()


if __name__ == "__main__":
    main()
