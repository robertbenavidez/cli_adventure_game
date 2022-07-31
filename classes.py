import descriptions

import random

from colorama import Fore

class Player:
    def __init__(self):
        self.hp: int = 100
        self.treasure: int = 0
        self.monsters_defeated: int = 0
        self.xp: int = 0
        self.turns: int = 0
        self.inventory: list = []


class Room:
    def __init__(self, items: list, monster: dict):
        self.description: str = descriptions.descriptions[random.randint(0, len(descriptions.descriptions) - 1)]
        self.sound: str = descriptions.sounds[random.randint(0, len(descriptions.sounds) - 1)]
        self.smell: str = descriptions.smells[random.randint(0, len(descriptions.smells) - 1)]
        self.items: list = items
        self.monster: dict = monster

    def print_description(self):
        print(f"{Fore.GREEN}{self.description}")
        print(self.smell)
        print(self.sound)


class Game:
    def __init__(self, player: Player):
        self.player = player
        self.room = None
        self.Num_monsters: int = 0
        self.rooms: dict = {}
        self.x: int = 0
        self.y: int = 0

    def set_rooms(self, rooms: dict):
        self.rooms = rooms

    def set_current_room(self, room: Room):
        self.room = room
