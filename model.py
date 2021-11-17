from exceptions import *
from random import randint


class Enemy:
    level = int
    lives = int

    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_enemy_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown

class Player:

    def __init__(self, player_name, lives):
        self.player_name = player_name
        self.lives = lives
        self.score = 0
        self.allowed_attacks = [1, 2, 3]

    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            return 0
        if attack == 1 and defense == 2:
            return 1
        if attack == 1 and defense == 3:
            return -1
        if attack == 2 and defense == 3:
            return 1
        if attack == 2 and defense == 1:
            return -1
        if attack == 3 and defense == 1:
            return 1
        if attack == 3 and defense == 2:
            return -1

    def decrease_player_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    def attack(self, enemy_obj):
        user_input = int(input("Enter 1 (wizard), 2 (warrior), 3(robber) to attack: "))
        if user_input not in self.allowed_attacks:
            print("You have to enter only 1, 2 or 3")
            return self.attack(enemy_obj)
        else:
            enemy = enemy_obj.select_attack()
            result = Player.fight(user_input, enemy)
            if result == 0:
                print("It is a draw")
            if result == 1:
                print("You attacked successfully")
                enemy_obj.decrease_enemy_lives()
                self.score = self.score + 1
            if result == -1:
                print("You missed")



    def defence(self, enemy_obj):
        user_input = int(input("Enter 1 (wizard), 2 (warrior), 3(robber) to defence: "))
        enemy = enemy_obj.select_attack()
        result = Player.fight(enemy, user_input)
        if result == 0:
            print("It is a draw")
        if result == -1:
            print("You defence is successful")
        if result == 1:
            print("You missed")
            self.decrease_player_lives()

