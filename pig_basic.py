import random
import os

class Player:
    def __init__(self, name, max_risk=None):
        self.name = name
        self.score = 0
        self.turn_score = 0
        #max risk per turn
        self.max_risk = 0
        self.die = 0

    def __str__(self):
        return "{} has a score of {}".format(self.name, self.score)

    def turn(self):
        self.die = random.choice([1, 2, 3, 4, 5, 6])
        d = self.die
        #print(self.name, 'die roll', d)
        self.game_score()

    def game_score(self):
        if self.die == 1:
            self.turn_score = 0
            #print('rolled a 1', self.turn_score)
            #print("accumulative game score", self.score)
            return
        else:
            #print('else turn score', self.turn_score, '+ die', self.die)
            self.turn_score += self.die
            #print('turn score', self.turn_score)
            self.roll_again()

    def roll_again(self):
        if self.turn_score >= self.max_risk:
            #print('dont roll again self score', self.score, '+ self turn score', self.turn_score)
            self.score += self.turn_score
            #print('self score', self.score)
            #print("accumulative game score", self.score)
            self.turn_score = 0
            return
        else:
            self.turn_score = 0
            #print('roll_again else')
            self.turn()

    def end_roll():
        return


class Game:
    def __init__(self, player1, player2, player3):
        self.round = 0

    def start_game(self):
        while self.round <= 6:
            self.round +=1
            #print('round', self.round)
            player1.turn()
            player2.turn()
            player3.turn()

    def end_game(self):
        return

os.system("clear")
player1 = Player(name='Basic Player')
player2 = Player(name='Strategy Player', max_risk=12)
player3 = Player(name='Risk Player', max_risk = 24)
game = Game(player1, player2, player3)
game.start_game()
p1 = player1.score
p2 = player2.score
p3 = player3.score
print(player1)
print(player2)
print(player3)
