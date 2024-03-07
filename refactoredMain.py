import random

class Player:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.lives = 0
        self.set_lives()

    def set_lives(self):
        self.lives = 3
        print(f"Life count: {self.lives}")

class Setup:
    def __init__(self, player):
        self.player = player
        self.valid_options = ["sword", "gold coin", "water pouch", "ruby ring", "turkey leg"]
        self.playing = True
        self.riddles = {"I have keys, but no locks and space, and no rooms. You can enter, but you can't go outside. What am I?": "keyboard",
                        "Where can you finish a book without finishing a sentence?": "prison",
                        "Walk on the living, they don't even mumble. Walk on the dead, they mutter and grumble. What are they?": "leaves",
                        "I'm a fruit. If you take away my first letter, I'm a crime. If you take away my first two letters, I'm an animal. If you take away my first and last letter, I'm a form of music. What am I?": "grape"}

    def invalid_input_message(self):
        print("""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Nice try, but that wasn't an option. Please choose one of the listed items.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
    
    def lose_life(self):
        self.player.lives -= 1
        if self.player.lives == 0:
            print("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                You lost your last life. Better luck next time.
                ~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~
                """)
            self.playing = False

        else:
            print(f"New life count: {self.player.lives}")
            continue_input = input("Do you wish to continue, yes or no? ").lower().strip()
            if continue_input == "no":
                print("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            Better luck next time.
                ~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~
                """)
                self.playing = False
            # else:
            #     self.replay_last_decision()

    def lose_life_no_replay(self):
        self.player.lives -= 1
        if self.player.lives == 0:
            print("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                You lost your last life. Better luck next time.
                ~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~
                """)
            self.playing = False

        else:
            print(f"New life count: {self.player.lives}")
            continue_input = input("Do you wish to continue, yes or no? ").lower().strip()
            if continue_input == "no":
                print("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            Better luck next time.
                ~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~
                """)
                self.playing = False

    def end_game(self):
            print("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Congratulations!!!!! 
                You have won the: “bad at decision making” award 
                and your prize is to go back to the beginning! 
                Better luck next time.
                ~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~
                """)
            self.playing = False

class Game:
    def __init__(self, setup_player, starting_event):
        self.setup_player = setup_player
        self.current_event = starting_event

    def play_game(self):
        while self.setup_player.playing:
            print(self.current_event.text)
            print(self.current_event.question)
            command = input('enter command> ')
            next_event = self.current_event.transitions[command]
            # next_event = self.current_event.transitions.get(command)
            if not set(player.items).intersection(next_event.require_items) and next_event.require_items != []:
            # if not set(self.setup_player.player.items).intersection(next_event.require_items):
                print("you don't have required item")
            else:
                self.current_event = next_event

class Event():
    def __init__(self, text, question, required_items=[]) -> None:
        self.require_items = required_items
        self.text = text
        self.question = question
        self.transitions = {}

player_name = input("Enter player name: ")
player = Player(player_name)
setup_player = Setup(player)
start_game = Event("""\n
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You wake up in a strange room with a blindfold on, you take 
                the blindfold off and you see five items laid out in front 
                of you with a note that reads: 'choose wisely' 
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n
                """, "Do you choose a: sword, gold coin, water pouch, ruby ring, or a turkey leg?: ")
door = Event("""\n
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Once you pick your item, all of the other items disappear. 
                You see two doors ahead, one purple and one blue.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n
                """, "Which door do you open: purple or blue?: ")

# door = Event("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\nOnce you pick your item, all of the other items \ndisappear. You see two doors ahead, one purple and one blue.\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*", "Which door do you open: purple or blue?: ")
# start_game.set_transition("sword", door)
start_game.transitions["sword"] = door

choose_path = Event("""\n
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The purple door opens up into a forest, you step out onto a 
                path. In front of you is a cloaked man, he walks to a fork 
                in the road, he chooses the clear path on the right and 
                beckons you to follow. The path to the left is dark, and you 
                hear the sound of a roaring river.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n
                """,
                "Which path do you choose: right or left? ")
wrong_door = Event("""\n
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You open the door and a waft of blue smoke engulfs you. You 
                start finding it hard to breath. Your vision goes dark. 
                This must be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n""",
                "Would you like to continue? ")

door.transitions["purple"] = choose_path
door.transitions["blue"] = wrong_door

left_path = Event('''\n
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You walk down the path until you reach the river. You can't 
                tell how deep it is, but the current looks aggressive. The 
                path continues and leads into dark caverns - you can't tell 
                what's inside. You can either try to swim across the river 
                or follow the path into the caverns.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n
                ''',
                "Which path will you take, river or caverns? ")

right_path = Event()

choose_path.transitions["left"] = left_path
choose_path.transitions["right"] = right_path



# if game.play_game.command in Setup.valid_options:
#     player.items.append(game.play_game.command)
#     print(player.items)
#     start_game.transitions["sword"] = door
# else:
#     Setup.invalid_input_message()
#     game 


# town_start = Event('you wake up in town, which way do you go?')
# town_left = Event('going left out of the town you are in a forest',['sword'])
# town_right = Event('going right out of the town you are in the market')
# town_start.transitions['right'] = town_right
# town_right.transitions['back'] = town_start
# town_start.transitions['left'] = town_left

game = Game(setup_player,start_game)
game.play_game()