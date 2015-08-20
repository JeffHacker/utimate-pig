import random
import os

class Player:
    def __init__(self, name, max_risk=None):
        self.name = name
        self.score = 0
        self.turn_score = 0
        self.die = 0

    def __str__(self):
        return "{} has a score of {}".format(self.name, self.score)

    def turn(self):
        self.die = random.choice([1, 2, 3, 4, 5, 6])
        d = self.die
        print("Die shows...", self.die)
        self.game_score()

    def game_score(self):
        if self.score >= 100:
            game.active = False
        elif self.die == 1:
            self.turn_score = 0
            print("")
            print("** You rolled a 1... No Score this roll **")
            print("")
            input("** Press Enter for next Player's turn **")
            return
        else:
            self.turn_score += self.die
            print("So far this turn you have rolled...", self.turn_score)
            self.roll_again()

    def roll_again(self):
        if self.score >= 100:
            game.active = False
        else:
            i = input("'R'oll again?  or Enter to pass >").lower()
            if i == 'q':
                game.active = False
            if i == 'r':
                print("Your score so far is...", self.turn_score)
                self.turn()
            else:
                self.score += self.turn_score
                self.turn_score = 0
                return


class Game:
    def __init__(self, player1, player2):
        self.active = True

    def start_game(self):
        os.system("clear")
        print("LET'S PLAY PIG")
        print("")
        print("Game Play is to 100 points, BUT other player gets one last chance to beat you!")
        print("")
        print("ROLL ALL YOU WANT, BUT IF YOU ROLL A '1' YOU LOSE YOUR POINTS THIS TURN")
        print("")
        print("Enter 'R' to roll again")
        print("Press Enter to Pass and lock in your score")
        print("Enter 'Q' to quit")
        print("")
        input("continue")
        while game.active == True:
            os.system("clear")
            print("player 1 score:", player1.score)
            print("player 2 score:", player2.score)
            print("")
            print("Player 1 Turn!!!")
            player1.turn()
            os.system("clear")
            print("player 1 score:", player1.score)
            print("player 2 score:", player2.score)
            print("")
            print("Player 2 Turn!!!")
            print("Your score so far is...", player2.score)
            player2.turn()


os.system("clear")
player1 = Player(name="Player 1")
player2 = Player(name="Player 2")
game = Game(player1, player2)
game.start_game()
os.system("clear")
print(player1)
print(player2)
