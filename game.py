from model import *
from exceptions import *
from settings import *
import sys


user_name = input("Enter your name: ")
if len(user_name) <= 1:
    print("You enter incorrect name, use right symbols please")
    user_name = input("Enter your name")

player = Player(user_name, player_lives)
level = 1
enemy = Enemy(level)



def play(player_obj, enemy_obj, level):
    while True:
        try:
            player_obj.attack(enemy_obj)
            player_obj.defence(enemy_obj)
        except EnemyDown:
            print("You kill him")
            level = level + 1
            enemy_obj = Enemy(level)
            player.score = player.score + 5


if __name__ == "__main__":
    print("You need enter the 'start', if you want to start the game: ")
    print("You can enter 'help' to see another commands")
    while True:
        command = input("Enter a command: ")
        if command == "start":
            try:
                play(player, enemy, level)
            except GameOver:
                result_list = []
                GameOver().result_writing(player.player_name, player.score, result_list)
                print("Thank you")
                player = Player(user_name, player_lives)
            except KeyboardInterrupt:
                pass
            finally:
                print("Good bye")
        elif command == "exit":
            sys.exit()
        elif command == "help":
            print(command_help)
        elif command == "sts":
            file = open("scores.json")
            top_results = Score(file)
            top_results.show_scores()
        else:
            print("You enter a incorrect command")



