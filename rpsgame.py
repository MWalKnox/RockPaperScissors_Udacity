import time
import random
import sys

# Two sections of this code is very similar to another
# github repository because this was my "guide" of sorts
# I fully understand what the two sections of similar code do


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


action = ['rock', 'paper', 'scissors']

print_pause("Welcome to the game! We assume you know the rules, "
            "but here\'s a quick rundown: \n")
print_pause("Rock dulls scissors. Rock wins.")
print_pause("Paper covers rock. Paper wins.")
print_pause("Scissors cut paper. Scissors wins.")
print_pause("The best two out of three wins. \n")

human_player = input("Hello Human. What is your name? \n")
print("\nPrepare your strategy, ", human_player, "! \n")


# Parent Class - Base for all players
class Player():
    def __init__(self):
        self.score = 0

    def play(self):
        return action[0]

    def learn(self, player_last_action):
        pass


# Random Player - Based on Parent Class
class RandomPlayer(Player):
    def play(self):
        index = random.choice(0, 2)
        return action[index]


# Reflect Player - Based on Parent Class
class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.player_last_action = None

    def play(self):
        if self.player_last_action is None:
            return Player.play(self)
        return self.player_last_action

    def learn(self, player_last_action):
        self.player_last_action = player_last_action


# Cycle Player - Based on Parent Class
class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.last_move = None

    def play(self):
        move = None
        if self.last_move is None:
            move = Player.play(self)
        else:
            index = action.index(self.last_move) + 1
            if index >= len(action):
                index = 0
            move = action[index]
        self.last_move = move
        return move


# Human Player - Based on Parent Class
class HumanPlayer(Player):
    def play(self):
        human_move = input('Your turn; choose ' + ', '.join(action) + '\n')
        while human_move not in action:
            human_move = input('Invalid move, try again\n')
        return human_move


# Game
class Game():
    def __init__(self):
        self.human = HumanPlayer()
        self.cycle = CyclePlayer()

    def play_game(self):
        for match in range(3):
            self.play_match()
            print('The score is: ' + str(self.human.score) + ' x ' +
                  str(self.cycle.score) + '\n')
        if self.human.score > self.cycle.score:
            print("Great job,", human_player, "you win!\n")
            print("Continue to play?")
            play_again()
        elif self.human.score > self.cycle.score:
            print('I win!')
            print('The Grand Total: ' + str(self.human.score) + ' to ' +
                  str(self.cycle.score))
        else:
            print('Continue to play?')
            play_again()

    def play_match(self):
        player1_move = self.human.play()
        player2_move = self.cycle.play()
        move_made = Game.check_action(player1_move, player2_move)

        self.human.learn(player2_move)
        self.cycle.learn(player1_move)

        print(human_player, 'chose "' + player1_move + '" and I chose "'
              + player2_move + '"')
        if move_made == 1:
            self.human.score += 1
            print(human_player, "\'s Match! \n")
        elif move_made == 2:
            self.cycle.score += 1
            print('My Match!\n')
        else:
            print('This match is a draw!\n')


# Check Actions and Points
    @classmethod
    def check_action(cls, move1, move2):
        if Game.stronger_action(move1, move2):
            return 1
        elif Game.stronger_action(move2, move1):
            return 2
        else:
            return 0

    @classmethod
    def stronger_action(cls, move1, move2):
        if (move1 == 'rock' and move2 == 'scissors'):
            return True
        elif (move1 == 'scissors' and move2 == 'paper'):
            return True
        elif (move1 == 'paper' and move2 == 'rock'):
            return True
        return False


# Offer an out
def play_again():
    print("Answer yes or no:")
    again = input("Yes\n"
                  "No\n").lower()
    if again.lower() == 'yes':
        print("Great! Give me a second to set it up again!")
        Game()
        game.play_game()
    if again.lower() == 'no':
        print("Okay, thank you for playing rock, paper, scissors with me!")
    # sys.exit()
    else:
        KeyboardInterrupt
        print("Swift Exit! Hope you had fun!")
#        play_again()


game = Game()
game.play_game()
