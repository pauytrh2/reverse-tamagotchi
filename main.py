import keyboard
from random import randint
from cat_faces import *
from defenses import *
import os
from time import sleep

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

    def check_health(self):
        if self.health < 1:
            print(f"Cat is dead...")
            exit()

    def print_cat_face(self, isL=False):
        if isL:
            print(self.L_face)
        else:
            if self.health > 75:
                print(self.happy_face)
            elif self.health > 50:
                print(self.meh_face)
            elif self.health > 0:
                print(self.sad_face)
            else:
                print(self.dead_face)

    def kick(self):
        dodge_chance = randint(1, 100)
        if dodge_chance <= 75: # 75%
            self.defend()
            return

        damage = randint(1, 10)
        if self.health - damage < 1:
            self.health = 0
            print(f"You kicked the poor cat... now he is on {self.health} health...")
            self.print_cat_face()
            self.check_health()
        else:
            self.health -= damage
            print(f"You kicked the poor cat... now he is on {self.health} health...")
            self.print_cat_face()

    def defend(self):
        defense_choice = randint(0, len(defenses) - 1)
        print(f"You *try* to kick the cat but {defenses[defense_choice]}")
        self.print_cat_face(isL=True)

poor_cat = Cat()

clear()

print("Press 'k' to kick the cat, or 'q' to quit.")

while True:
    if keyboard.is_pressed('k'):
        clear()
        poor_cat.kick()
        sleep(0.1)
    
    elif keyboard.is_pressed('q'):
        clear()
        print("You decided not to kick the cat... (loserrr)")
        break