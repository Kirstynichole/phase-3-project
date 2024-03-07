import random
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.lives = 0
        self.set_lives()

    def set_lives(self):
        self.lives = 3
        print(f"Life count: {self.lives}")

class Maze:
    def __init__(self, player):
        self.player = player
        self.valid_options = ["sword", "gold coin", "water pouch", "ruby ring", "turkey leg"]
        self.playing = True
        self.decision_history = []
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
            sys.exit()

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
                sys.exit()
            else:
                self.replay_last_decision()

    def lose_life_no_replay(self):
        self.player.lives -= 1
        if self.player.lives == 0:
            print("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                You lost your last life. Better luck next time.
                ~~~~~~~~~~~~~~~~~~~GAME OVER~~~~~~~~~~~~~~~~~~~
                """)
            self.playing = False
            sys.exit()

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
                sys.exit()

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
            sys.exit()

    def replay_last_decision(self):
        while self.playing:
            while self.decision_history:
                last_decision = self.decision_history.pop()
                print("""
                    Why don't you try that last decision again: 
                    """)
                if "choose item" in last_decision.lower():
                    self.choose_item()
                elif "opened door" in last_decision.lower():
                    self.open_door()
                elif "chose path" in last_decision.lower():
                    self.choose_path()
                elif "chose left" in last_decision.lower():
                    self.left_path()
                elif "sphynx" in last_decision.lower():
                    self.sphynx()
                elif "caves" in last_decision.lower():
                    self.caves()
                elif "town" in last_decision.lower():
                    self.town()
                elif "tavern" in last_decision.lower():
                    self.tavern()
                elif "dice_game" in last_decision.lower():
                    self.play_dice_game()
                elif "bar" in last_decision.lower():
                    self.bar()
                elif "rabbit_hole" in last_decision.lower():
                    self.rabbit_hole()
                elif "hedge_maze" in last_decision.lower():
                    self.hedge_maze()
                elif "quest_offer" in last_decision.lower():
                    self.quest_offer()
                elif "castle" in last_decision.lower():
                    self.castle()  
                elif "princess" in last_decision.lower():
                    self.princess()    
            ##ADD NEW DECISIONS HERE

    def play_game(self):
        while self.playing and self.player.lives > 0:
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You wake up in a strange room with a blindfold on, 
                you take the blindfold off and you see five items laid 
                out in front of you with a note that reads: 'choose wisely'
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
            self.choose_item()
            
            if not self.playing:
                break

    def choose_item(self):
        item_input = input("Do you choose a: sword, gold coin, water pouch, ruby ring, or a turkey leg?: ")
        if item_input in self.valid_options:
            self.player.items.append(item_input)
            if not self.decision_history or "Chose item" not in self.decision_history[-1].lower():
                self.decision_history.append(f"Chose item: {item_input.lower()}")
        else:
            self.invalid_input_message()
            self.choose_item()
        print(f"""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Once you pick up the {item_input}, all of the other items 
                disappear. You see two doors ahead, one purple and one blue.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
        self.open_door()

    def open_door(self):
        door_input = input("Which door do you open: purple or blue?: ")
        if "Opened door" not in self.decision_history[-1].lower():
            self.decision_history.append(f"Opened door: {door_input.lower()}")

        if door_input == "blue":
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You open the door and a waft of blue smoke engulfs you. You 
                start finding it hard to breath. Your vision goes dark. 
                This must be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
            self.lose_life()
        elif door_input == "purple":
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The purple door opens up into a forest, you step out onto a 
                path. In front of you is a cloaked man, he walks to a fork 
                in the road, he chooses the clear path on the right and 
                beckons you to follow. The path to the left is dark, and you 
                hear the sound of a roaring river.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
            self.choose_path()
        else:
            self.invalid_input_message()
            self.open_door()

    def choose_path(self):
        path_input = input("Which path do you choose: right or left? ")
        if "Chose Path" not in self.decision_history[-1].lower():
            self.decision_history.append(f"Chose Path: {path_input.lower()}")

        if path_input == "right":
            print(self.player.items)
            if "gold coin" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The cloaked man somehow knew you had a valuable item in 
                your pocket. He attacks you and takes it before you even 
                realize what's happening. Your vision goes dark. This must 
                be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                self.player.items = []
                self.lose_life()
            elif "ruby ring" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The cloaked man somehow knew you had a valuable item in your 
                pocket. He attacks you and takes it before you even realize 
                what's happening. Your vision goes dark. This must be what 
                it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                self.player.items = []
                self.lose_life()
            elif "sword" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The cloaked man somehow knew you had a weapon. He attacks 
                you before you even realize what's happening. You get 
                stabbed by your own sword. Your vision goes dark. This must 
                be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                self.player.items = []
                self.lose_life()
            else:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The cloaked man attacks you before you even realize what's
                happening. But he quickly realizes you have nothing of 
                value. Feeling guilty, he lets you leave unharmed. You 
                decide to backtrack and take the path to the left.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                input("Ready to continue? Press enter. ")
                self.left_path()
        elif path_input == "left":
            self.left_path()
        else:
            self.invalid_input_message()
            self.choose_path()

    def left_path(self):
        if "Chose left" not in self.decision_history[-1].lower():
            self.decision_history.append(f"Chose left")
        print('''
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You walk down the path until you reach the river. You can't 
                tell how deep it is, but the current looks aggressive. The 
                path continues and leads into dark caverns - you can't tell 
                what's inside. You can either try to swim across the river 
                or follow the path into the caverns.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                ''')
        river_input = input("Which path will you take, river or caverns? ")
        if river_input == "river":
            print('''
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Just as you start to wade through the river, the current 
                sweeps you off your feet and you remember you're a plebeian 
                and don't know how to swim. Your vision goes dark. This 
                must be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                ''')
            self.lose_life()
        elif river_input == "caverns":
            print('''
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You come face to face with a Sphynx. She is not happy to 
                have a visitor. She offers to let you pass if you answer 
                her riddle correctly. You're not sure what will happen if 
                you answer incorrectly, but it can't be good.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                ''')
            self.sphynx()
        else:
            self.invalid_input_message()
            self.choose_path()

    def sphynx(self):
        if "sphynx" not in self.decision_history[-1].lower():
            self.decision_history.append(f"sphynx")
        input("Ready to answer her riddle? ")
        riddle, answer = random.choice(list(self.riddles.items()))
        print(riddle)

        player_answer = input("All answers are one word only: ").lower()

        if player_answer == answer.lower():
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Surprisingly enough, you got it right. The Sphynx steps 
                aside and lets you pass. Behind the Sphynx are two doorways:
                one is a bright opening which you can tell leads back 
                outside, and one is dark and leads deeper into the caves.                
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
            def sphynx_doorway():
                post_sphynx_input = input("Which doorway do you choose, light or dark? ")
                if post_sphynx_input == "dark":
                    self.caves()
                elif post_sphynx_input == "light":
                    self.town()
                else:
                    self.invalid_input_message()
                    sphynx_doorway()
            sphynx_doorway()
        else:
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Unsurprisingly you are incorrect. The Sphynx gives you 
                barely a moment before she bites your head off. Literally. 
                Your consciousness goes dark. This must be what it feels 
                like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
            self.lose_life()
        print()

    def caves(self):
        if "caves" not in self.decision_history[-1].lower():
            self.decision_history.append(f"caves")
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The path through the cave is dark and winding. You keep 
                walking deeper and deeper, and just when you're thinking
                about turning around, you walk straight into a troll. He 
                looks you up and down and smirks. You quickly consider if
                you have anything that could be useful.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
            print(f"Current items: {self.player.items}")
            input("Continue? ")              

            if "sword" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You pull out the sword and he immediately backs off. Turns
                out he's a little lazy and very afraid of sharp objects.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                input("Continue? ")
            elif "ruby ring" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You pull out the ruby ring and offer it to him...
                and he immediatly picks you up and rips you in half. Turns
                out red clashes with his green skin. Your consciousness 
                goes dark. This must be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                self.lose_life_no_replay()
            elif "gold coin" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You pull out the gold coin and offer it to him...
                He takes it greedily and lets you pass. While you're happy
                to still be alive, there might have been better uses for
                that coin. But there's no use worrying about that now.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                input("Continue? ")
                self.player.items = []      
            elif "turkey leg" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You pull out the turkey leg and offer it to him...
                and he immediatly swallows it whole, along with your arm.
                You're bleeding out and there's no one here to help you.
                Maybe a turkey leg wasn't the most useful choice of item.
                Your vision goes dark. This must be what it feels like to 
                lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                self.lose_life_no_replay()
                self.player.items = []
            elif "water pouch" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You pull out the water pouch and nervously offer it to him...
                He is surprisingly ecstatic. Turns out his thirst hasn't 
                been quenched in years. While you're happy to still be alive, 
                there might have been better uses for that water. But 
                there's no use worrying about that now.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                input("Continue? ")
                self.player.items = [] 
            else:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You have nothing to offer to the troll, you look up at him 
                with empty hands...
                and he immediatly picks you up and rips you in half. Your 
                consciousness goes dark. This must be what it feels like to 
                lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                self.lose_life_no_replay() 
        def tavern_basement():
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Behind the troll is a questionable looking rope ladder, 
                which you can only hope leads back outside.
            
                You climb until you are about to collapse. You finally 
                reach the top and open a hatch. After a bit of investigating
                you realize you're in the basement of a tavern, which is so
                incredibly convenient. You head upstairs for some dinner.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """) 
            self.tavern() 
        tavern_basement() 

    def town(self):
        if "town" not in self.decision_history[-1].lower():
            self.decision_history.append(f"town")
        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You pass through the doorway and you're conveniently on the
                other side of the river. You continue down the path until
                you end up in a small town. You realize you haven't eaten 
                in quite a while so you wander around until you find a 
                decent looking tavern. You open the door and walk inside...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """) 
        input("Continue? ")
        self.tavern()

    def tavern(self):
        if "tavern" not in self.decision_history[-1].lower():
            self.decision_history.append(f"tavern")

            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You enter the tavern and there is a group of intimidating
                people sitting in the corner, a few empty seats at the bar,
                and a welcoming crowd playing a rowdy dice game. They beckon 
                you over.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
            join_game = input("Do you want to play dice, yes or no? ")
            if join_game == "yes":
                self.play_dice_game()
            elif join_game == "no":
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Maybe next time. Instead, you sit at the bar and try to 
                order something to eat and drink.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                self.bar() 
            else:
                self.invalid_input_message()
                self.tavern()

    def play_dice_game(self):
        if "dice_game" not in self.decision_history[-1].lower():
            self.decision_history.append(f"dice_game")
        dice = (1,2,3,4,5,6)
        print("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                You'll each roll 2 dice, whoever rolls a higher
                combined total wins. The game is best 2 of 3.
                ~~~~~~~~~~~~~~~~~~~~~~DICE~~~~~~~~~~~~~~~~~~~~~~                
            """)
        player_counter = 0
        opponent_counter  = 0 
        while player_counter < 2 and opponent_counter < 2:
            def dice_game():
                nonlocal player_counter
                nonlocal opponent_counter
                input("Roll dice? ")
                player_dice_roll = random.choice(dice)
                player_dice_roll2 = random.choice(dice)
                total_player_roll = player_dice_roll + player_dice_roll2
                print(f"You rolled a {player_dice_roll} & a {player_dice_roll2} for a total of {total_player_roll}")
                input("Opponent rolls...")
                opponent_dice_roll = random.choice(dice) 
                opponent_dice_roll2 = random.choice(dice)
                total_opponent_roll = opponent_dice_roll + opponent_dice_roll2
                print(f"Your opponent rolled a {opponent_dice_roll} & a {opponent_dice_roll2} for a total of {total_opponent_roll}")
                if total_player_roll > total_opponent_roll:
                    print("You won!")
                    player_counter += 1
                elif total_opponent_roll > total_player_roll:
                    print("Your opponent won!")
                    opponent_counter += 1
                else:
                    print("It's a tie! Keep playing to reach two wins.")
            dice_game()

        if player_counter == 2:
            print("Congratulations! You won 2 rounds so you won the game!")
            input("Continue? ")
            if "castle" in self.decision_history:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Your opponent hands you your winnings and you realize it's
                a small silver key. You know exactly what you'll use this
                for, and you don't waste any time...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*         
                """)
                self.player.items.append("silver key")
                self.castle()
            else:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Your opponent hands you your winnings and you realize it's
                a small silver key. You don't have a use for it yet but
                put it in your pocket anyway. You've definitely earned a 
                drink so you walk over and sit down at the bar.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*         
                """)
                self.player.items.append("silver key")

        else:
            print("Unfortunately your opponent won the game.")
            input("Continue? ")
            if "castle" in self.decision_history:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You didn't come all the way back here to accept defeat...
                Or did you? You can either play again, or admit defeat.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*         
                """)
                play_again = input("Which do you choose: play or defeat? ")
                if play_again == "defeat":
                    self.end_game()
                else:
                    self.play_dice_game()
            else:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Nothing gained nothing lost, but you definitely need a 
                drink, so you walk over and sit down at the bar.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*         
                """)
        self.bar()

    def bar(self):
        if "bar" not in self.decision_history[-1].lower():
            self.decision_history.append("bar")
            print(f"""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                        The bartender looks at you expectantly.
                        You take stock of what's in your pockets...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
            print(f"{self.player.name}'s items: {self.player.items}")
            input("Continue? ")
            if "turkey leg" in self.player.items:
                print(f"""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The bartender realizes you brought in your own food. This 
                is obviously incredibly offensive. Do you not trust the 
                food here? You try to explain but before you get a chance
                the bartender nods at the group of people in the corner.
                They approach menacingly and before you know it your vision
                goes dark. This must be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                self.lose_life_no_replay()
            elif "gold coin" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The bartender offers you a meal and a drink in exchange for
                your gold coin.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                meal_answer = input("Do you hand over your coin, yes or no? ")
                if meal_answer == "yes":
                    print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You are presented with the best drink and meal you've ever
                consumed. You feel completely happy and satisfied. You're 
                not thinking at all about the fact that you might need 
                that coin in the future...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                    """)
                    self.player.items.remove("gold coin")
                    print(self.player.items)
                elif meal_answer == "no":
                    print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The bartender is obviously incredibly offended. Why did you
                come to a bar if you don't plan to pay for anything? You 
                try to explain but before you get a chance the bartender 
                nods at the group of people in the corner. They approach 
                menacingly and before you know it your vision goes dark. 
                This must be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                    """)
                    self.lose_life_no_replay()
                else:
                    self.invalid_input_message()
                    self.bar()
            else:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The bartender realizes you have no way to pay for anything.
                This is obviously incredibly offensive. You look a bit 
                haggard though so the bartender offers to make you food in
                exchange for doing the dishes...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                dishes_answer = input("Do you agree to do the dishes, yes or no? ")
                if dishes_answer == "yes":
                    print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You are presented with the best drink and meal you've ever
                consumed. You feel completely happy and satisfied. You're 
                not thinking at all about the fact that these dishes are 
                going to take all night...
                
                After you finish, the bartender offers you a gold coin for
                your hard work. This is working out surprisingly well.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                    """)
                    self.player.items.append("gold coin")
                elif dishes_answer == "no":
                    print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The bartender is obviously incredibly offended. Why did you
                come to a bar if you don't plan to pay for anything? You 
                try to explain but before you get a chance the bartender 
                nods at the group of people in the corner. They approach 
                menacingly and before you know it your vision goes dark. 
                This must be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                    """)
                    self.lose_life_no_replay()
                else:
                    self.invalid_input_message()
        input("Continue? ")
        self.rabbit_hole()
            ##KEEP GOING HERE

    def rabbit_hole(self):
        if "rabbit_hole" not in self.decision_history[-1].lower():
            self.decision_history.append("rabbit_hole")
        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                It's late when you finally leave the tavern. You're in a 
                bit of a haze. You're not sure if it's from drinking or 
                exhaustion. As you're rubbing your eyes, a white blur streaks
                across your vision. You're not sure if you should see where 
                it's going or shrug it off...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
        rabbit_decision = input("Do you follow the white streak, yes or no? ")
        if rabbit_decision == "yes":
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You break out into a run to follow the blur. While you're 
                on the chase you realize it's a rabbit. And it has a pocket 
                watch. Why would a rabbit need a pocket watch? It's a nice 
                watch, and you are but a poor peasant, you think maybe you 
                should take it. Just as you reach this conclusion, the rabbit 
                disappears, and you seem to be falling...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
            input("Continue? ")
        else:
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You decide not to follow the streak. Was it a rabbit? You
                can't be sure. While you're pondering what you saw, you 
                trip over something hard, and you seem to be falling...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
            input("Continue? ")
        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                After falling for quite some time, you land with a crash on
                your back in what appears to be a very thorny bush with white 
                roses, which are painted red? You hear a very angry woman's 
                voice followed by footsteps. Someone with a paintbrush 
                dripping red paint onto the grass comes sprinting past, 
                shoves the paintbrush into your hand and says "Run!"
    
                You don't have time to think, off you go into the maze, 
                hedges twice your height on either side of the path.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
        input("Continue? ")
        self.hedge_maze()
    
    def hedge_maze(self):
        if "hedge_maze" not in self.decision_history[-1].lower():
            self.decision_history.append("hedge_maze")
        print("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                The hedge maze has one correct path and many
                incorrect paths. All options will be presented.
                Invalid responses will take you back to the start.
                ~~~~~~~~~~~~~~~~~~~~~~MAZE~~~~~~~~~~~~~~~~~~~~~~                
            """)
        input("Ready? ")
        maze1 = input("The path immediately splits in two directions, do you go right or left? ")
        if maze1 == "right":
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You turn right and continue ahead until you run into a 
                hedge. You have hedges on your right and in front of you so
                your only option is to turn left.
                
                After you turn left you almost run into another hedge, you 
                have to make another left, two rights, a left, and another 
                right.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
            maze2 = input("Again the path splits in two directions, do you turn right or left? ")
            if maze2 == "right":
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You make your choice and turn, running down. You hear a 
                strange hissing and clicking noise and the rustling of 
                something big moving quickly towards you but when you look 
                around you see nothing. Then, trembling with fear you look 
                up. Hovering above you, pincers clicking, is a spider the 
                size of three horses, and before you can even scream it
                pounces. Your vision goes dark. This must be what it feels 
                like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                self.lose_life()
            elif maze2 == "left":
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You follow the path as it takes an immediate left, another 
                left, and then a right. 
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                maze3 = input("Then you have two options: straight or right? ")
                if maze3 == "right":
                    print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The path winds back and forth and you dodge wall after wall. 
                They aren't turns per se, just left and right back and 
                forth. You hope this is the right way since it will be 
                annoying to turn back. You reach the opening only to find a 
                dreaded dead end. Great. You try and squeeze through a bush 
                in a corner, but all that got you was scrapes from the 
                branches and a couple bee stings from the nest you disrupted. 
                
                Something is wrong, your throat feels tight and your breaths 
                are wheezing. You look down at yourself and where the bees 
                have stung you is swollen. It looks like you are deathly 
                allergic to bees. Your vision goes dark. This must be what 
                it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                    """)
                    self.lose_life()
                elif maze3 == "straight":
                    print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The maze path widens and you can see you have three options 
                in front of you, none of which look promising...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                    """)
                    maze4 = input("Do you go left, right, or straight? ")
                    if maze4 == "left":
                        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You reach what at first looks like a dead end, upon closer 
                inspection there's a small door, only big enough for your 
                shoulders. There's a key hole and you go to press your eye 
                to it. The door handle says “well that's quite rude” and 
                you back away sheepishly. 
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                        """)
                        input("Continue? ")
                        if "silver key" in self.player.items:
                            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You remember you have a silver key in your pocket. You may 
                as well give it a try. You push the key into the lock and 
                surprisingly it works! Despite protests from the door knob,
                you twist it and open the door crawling inside.

                You burst out of the maze, breathless and run down into the
                dark, dense forest. The plants and animals appear to be 
                sentient but you do not stop to ask questions. You finally 
                come to rest at a log, behind you stumbles the person who
                gave you the paintbrush.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                            """)
                            input("Continue? ")
                            self.quest_offer()
                        else:
                            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The guards heard the door knob scolding and have found you, 
                they drag you back to their queen for sentencing. You are 
                found guilty. She does not ask for your final words before 
                ordering the executioner to bring her your head. The axe 
                swings down on your neck. Your vision goes dark. This must 
                be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                            """)
                            self.lose_life()
                    elif maze4 == "straight":
                        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You've reached a dead end, but sitting at the edge of the 
                maze is a small table set for a garden tea party. No one 
                sits at the table but a sign on the pastry tower says “eat 
                me”. You shrug, you're hungry from all this running and 
                could use a snack. So you take a large bite and savor the 
                lemony flavor of the tart, closing your eyes. When you open 
                your eyes you find the table getting larger and larger. Or 
                as it turns out you are getting smaller and smaller. You 
                shrink until you are as tall as the blades of grass. The 
                guards come storming into the area, and despite your best 
                efforts to get away, one large foot descends onto your head.
                Your vision goes dark. This must be what it feels like to 
                lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                        """)
                        self.lose_life()
                    elif maze4 == "right":
                        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The path turns right again and then narrows, and continues
                to narrow until you can barely fit. You turn sideways and
                keep pushing on, but it feels like the hedges are becoming
                more solid. And are they closing in on you? The walls touch
                your front and back. It's too late to turn around. Your 
                vision goes dark. You end up flatter than a pancake. This 
                must be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                        """)
                        self.lose_life()
                    else:
                        self.invalid_input_message()
                        self.hedge_maze()
                else:
                    self.invalid_input_message()
                    self.hedge_maze()
            else:
                self.invalid_input_message()
                self.hedge_maze()
        elif maze1 == "left":
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The path in front of you almost immediately turns right, 
                right, and then left. You are faced with two options 
                continue straight or turn right.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
            maze5 = input("Which do you choose: straight, or right? ")
            if maze5 == "straight":
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The path spirals until you're so dizzy you can't even see 
                straight. You've turned left more times than you can count.
                The world feels like it's spinning around you. Your vision 
                goes dark. This must be what it feels like to lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                self.lose_life()
            elif maze5 == "right":
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                After turning you take an immediate left, then right. You 
                have two options in front of you: walk through a narrow 
                passageway so small you almost missed it, or continue 
                straight on the path..
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                maze6 = input("Which do you chose: passageway or straight? ")
                if maze6 == "passageway":
                    print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You skid to a stop, a dead end wreathed in shadow. Before 
                you can turn you hear an eerie, echoing laugh. Out of the
                dark corner you see a gleaming feline grin before the 
                striped cat steps out, yellow eyes full of a cruel mischief. 
                The laughing cat considers you for a moment before unraveling 
                bit by bit like a ball of yarn. You turn away confused and 
                then feel a weight settle over your shoulders. The cats 
                claws make quick work of you. 
                
                Your vision goes dark. This must be what it feels like to 
                lose a life.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                    self.lose_life()
                
                elif maze6 == "straight":
                    print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You see a doorway in front of you. Could it be the exit?
                It seems too good to be true, but you have no other options.
                
                You burst out of the maze, breathless and run down into the
                dark, dense forest. The plants and animals appear to be 
                sentient but you do not stop to ask questions. You finally 
                come to rest at a log, behind you stumbles the person who
                gave you the paintbrush.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                    input("Continue? ")
                    self.quest_offer()
                else:
                    self.invalid_input_message()
                    self.hedge_maze()
            else:
                self.invalid_input_message()
                self.hedge_maze()
        else:    
            self.invalid_input_message()
            self.hedge_maze()

    def quest_offer(self):
        if "quest_offer" not in self.decision_history[-1].lower():
            self.decision_history.append("quest_offer")  
        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You realize the person who was painting the roses is wearing
                a guard's uniform. They explain that they were working for
                the Queen when she ordered their beheading. Their crime was
                something to do with painting white roses red? You are
                fully confused but don't have the energy to ask for 
                clarification.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
        input("Continue? ")
        if "water pouch" in self.player.items:
            guard_reward = ""
            if "silver key" in self.player.items and "gold coin" in self.player.items:
                guard_reward = "ruby ring"
            elif "silver key" in self.player.items:
                guard_reward = "gold coin"
            else:
                guard_reward = "silver key"
            print(f"""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You decide there's no time like the present to finally
                drink the water you brought. You offer some to the guard
                as well who seems to be having trouble catching their breath.
                The guard is incredibly grateful and in return gives you a
                {guard_reward} in return.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
            self.player.items.append(guard_reward)
            print(f"Current items: {self.player.items}")
            input("Continue? ")
        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                After you both have time to relax, you realize the guard 
                looks quite upset, and is... crying? You become slightly
                uncomfortable, you don't know what to do with crying people.
                You offer a comforting (patronizing?) pat on the shoulder,
                and the guard takes this an an invitation to tell you their
                life story...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
        input("Continue? ")
        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                After oversharing to the extreme, the guard explains that
                they are affianced to the princess of these lands, but her 
                mother (the queen) does not approve of their marriage 
                (you're not sure you do either, but you keep your opinions 
                to yourself) so she locked the princess in a tower protected 
                by a dragon. The guard offers you a quest: if you can rescue 
                the princess and bring her to the guard, you will receive
                safe passage home.
                
                This is a tempting offer considering you have no idea where
                you are, let alone how to find your way back home.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
        quest_answer = input("Will you accept the quest, yes or no? ")
        if quest_answer == "yes":
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Off to the castle you go...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
            input("Continue? ")
            self.castle()
        elif quest_answer == "no":
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You walk away and the queen finds you with red paint on 
                your hands You're put on trial, found guilty, and beheaded.
                Your vision goes black. This is definitely what losing a 
                life feels like.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
            self.lose_life()
        else:
            self.invalid_input_message()
            self.quest_offer()

    def castle(self):
        if "castle" not in self.decision_history[-1].lower():
            self.decision_history.append("castle")  

        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                                   ~                 ~      
                                  ^                 ^
                                /   \             /   \  
                               /     \           /     \  
                                |   |             |   |   
                                |   |             |   |   
                                |   |  _   _   _  |   |
                                | O |_| |_| |_| |_| O |
                                |-  |          _  | - |
                                |   |   - _^_     |   |
                                |  _|    //|\\\  - |   |
                                |   |   ///|\\\\\   |  -|
                                |-  |_  |||||||   |   |
                                |   |   |||||||   |-  |
                                |___|___|||||||___|___|
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
        input("Continue?") 
        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                When you find her tower, it sits in a wasteland of ash and 
                rock, where trees once stood in full bloom now barren,
                scavenger birds perched on their decaying branches, eyeing 
                you like you'll be their next snack. The water in the moat
                surrounding the tower is a dark sludge. A booming voice 
                rings out "A new snack for Pumpkin!" And with a roar, 
                Pumpkin the dragon descends from the thick clouds.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        """)
        input("Continue?") 
        print(f"""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                        You take stock of what's in your pockets...
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
        print(f"{self.player.name}'s items: {self.player.items}")
        input("Continue?") 

        if "ruby ring" in self.player.items:
            print(f"""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You're painfully aware of the fact that you cannot outfight
                or outsmart this dragon. Bribery seems like your best option.
                You pull the ruby ring out of your pocket, show it to the 
                dragon, and she stops in her tracks. It has been eons since
                she has seen something so beautiful. You hand it over 
                shakily and she flies away. 
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
            self.player.items.remove("ruby ring")
            input("Continue?") 

            if "silver key" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You look up at the enormous locked castle doors and ponder
                what to do next. You didn't imagine you would get this far, 
                so you don't exactly have a plan. But then you feel the
                weight of the silver key in your pocket. Surely this would 
                be too good to be true, but you have to try anyway. You
                walk up to the doors, slide the key into the lock, and you 
                hear a click...
                    
                You step into the castle and see stair after stair after 
                stair. This might be more than you bargained for, but you 
                start climbing.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                input("Continue?")
                self.princess() 

            elif "gold coin" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You look up at the enormous locked castle doors and ponder
                what to do next. You didn't imagine you would even get this 
                far. But then you feel the weight of the gold coin in your 
                pocket and a plan forms in your head. The dragon can't have 
                gone far, and you're already in her good graces...
                    
                Once you find Pumpkin, you offer your gold coin in exchange
                for a quick flight up to the tallest tower. She greedily 
                agrees and grabs you by the collar before you can specify
                HOW you'd like to be flown.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                input("Continue?") 
                self.princess()
            else:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You walk up to the doors at the base of the tower but when 
                you try to pull one open, you realize they're locked. You 
                pat your pockets but you already know you're fresh out of 
                keys. You step back and look up at the tower, you see a 
                figure leaning out of the window high above. She waves a 
                handkerchief at you. You wave back. She seems confused as 
                to why you're not coming up and you gesture sheepishly at 
                the locked door and mime not being able to open it. From 
                here you can see how annoyed she looks as she throws her 
                hands up in the air before disappearing from the window. 
                    
                A few minutes later you hear footsteps and the bolt slides 
                out of place and the door creaks open. The princess stands 
                hands on hips and rolls her eyes at you. “Some savior you 
                are, you can't even open the door”
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                input("Continue?") 
                self.princess() 

        elif "gold coin" in self.player.items:
            print("""
            *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            You're painfully aware of the fact that you cannot outfight
            or outsmart this dragon. Bribery seems like your best option.
            You pull the gold coin out of your pocket, show it to the 
            dragon, and she stops in her tracks. She might be a guard-
            dragon, but everyone has a price. You hand it over shakily 
            and she flies away. 
            *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
            input("Continue? ")
            if "silver key" in self.player.items:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You look up at the enormous locked castle doors and ponder
                what to do next. You didn't imagine you would get this far, 
                so you don't exactly have a plan. But then you feel the
                weight of the silver key in your pocket. Surely this would 
                be too good to be true, but you have to try anyway. You
                walk up to the doors, slide the key into the lock, and you 
                hear a click...
                
                You step into the castle and see stair after stair after 
                stair. This might be more than you bargained for, but you 
                start climbing.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                input("Continue?")
                self.princess() 
            else:
                print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You walk up to the doors at the base of the tower but when 
                you try to pull one open, you realize they're locked. You 
                pat your pockets but you already know you're fresh out of 
                keys. 
                
                You think back to the dice game you played earlier, you
                could've won a silver key there, but it didn't seem important
                at the time... You can go all the way back to the tavern, or
                you can admit defeat and call it a day.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
                key_decision = input("Which do you chose: tavern or defeat? ") 
                if key_decision == "defeat":
                    self.end_game()
                else:
                    self.tavern()

        elif "sword" in self.player.items:
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You lift your sword and charge at the dragon...
                She laughs before unleashing a plume of flame, roasting you
                to smithereens. She likes you crunchy. 
                
                Fade to black. There's no coming back from this one.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
            input("Continue?") 
            self.end_game()
        else:
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                You pat your pockets one last time for anything that could 
                be useful before turning to run... The dragon laughs before 
                unleashing a plume of flame, roasting you to smithereens. 
                She likes you crunchy. 
                
                Fade to black. There's no coming back from this one.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                """)
            input("Continue?") 
            self.end_game()
            
    def princess(self):
        print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The princess is a lot more beautiful than you expected, not 
                that you expected much. “I'm here to take you back to your 
                fiancé” you say. She makes a disgusted face and says “oh as 
                if I'd go back to that loser! They are more scared of my mom 
                than in love with me, they left me here for years and sent 
                someone else to come save me! I'm running far away from the 
                both of them!” 

                Well this wasn't in the script. Now you have to decide if
                you follow her or kidnap her and bring her back to the 
                guard. 
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
        princess_decision = input("Do you follow or kidnap? ")
        if princess_decision == "kidnap":
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                The princess has been spending her free time practicing 
                mixed martial arts and you're standing a lot closer to the 
                moat than you thought. When you try to pick her up, she 
                flips you into the moat and since you are still a plebeian 
                despite your recent heroics, you drown. 
                Your vision goes black. This is definitely what losing a 
                life feels like.
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
            self.lose_life()
        elif princess_decision == "follow":
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                Your journey out of the wasteland is a long one where you 
                bond and she teaches you to swim in a gentle river along the 
                way. You tell her of your travels in this land and she tells 
                you of her time in the tower and how she bonded with the 
                dragon Pumpkin. When you finally get to the city you realize, 
                this life with her is a lot more fulfilling than your old 
                life as a plebeian and you stop trying to convince her to go 
                back to her ex fiancé. 
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
            input('Continue? ')
            print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                5 years past and now you're trying to talk her into being 
                your fiancé, she's still as stubborn as ever but eventually 
                says yes. When word comes of her mother's passing, her people 
                plead for her to come back and rule. 
                
                How did you go from plebeian to Queen's consort? It all 
                started with two doors so close in color you're glad you 
                aren't colorblind. 
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            """)
            input('Continue? ')
            print('''
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                *-*-*-*-*-*- CONGRATULATIONS! YOU WIN AT LIFE! -*-*-*-*-*-*
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                                                    .''.       
                        .''.      .        *''*    :_\/_:     . 
                        :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
                    .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
                    :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
                    : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
                    '..'  ':::'     * /\ *     .'/.\'.   '
                        *            *..*         :
                        *
                        *
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                *-*-*-*-*-*-*-*-*-*-*-*-* THE END *-*-*-*-*-*-*-*-*-*-*-*-*
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            ''')
            sys.exit()
        else:
            self.invalid_input_message()
            self.princess()

print("""
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                *-*-*-*-*-*-*-*-*-*-*-*-* WELCOME *-*-*-*-*-*-*-*-*-*-*-*-*
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
                *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
""")
player_name = input("Enter player name: ")
player = Player(player_name)
maze = Maze(player)
maze.play_game()




