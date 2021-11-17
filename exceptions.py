import json


class GameOver(Exception):

    @staticmethod
    def result_writing(name, final_result, list_):
        json_data = open("scores.json")
        data = json.load(json_data)
        for pers in data:
            list_.append(pers)
        person = {
            name: final_result
        }
        list_.append(person)
        with open("scores.json", "w") as file:
            json.dump(list_, file)


    def __str__(self):
        return "You are dead. GAME OVER"


class EnemyDown(Exception):
    def __str__(self):
        return "enemy is dead"


class Score:
    def __init__(self, data):
        self.data = data

    def show_scores(self):
        json_data = json.load(self.data)
        tmp = []
        for score in json_data:
            tmp += list(score.items())
        tmp.sort(key=lambda i: i[1])
        tmp.reverse()
        if len(json_data) <= 10:
            for result in tmp:
                print(f"{result[0]}: {result[1]}")
        else:
            for result in tmp[:10]:
                print(f"{result[0]}: {result[1]}")

