"""
Design Patterns Final Project - Mini Games using pygame zero
Description: Mini games built with Python and Pygame zero.
Authors: Maïmouna N'Diaye & Leonore Ndebele
"""

from random import randint
import pgzrun
from pgzero.actor import Actor
import os, sys
from collections import Counter
from pygame import Rect

# dico_path = os.path.dirname(sys.argv[0])
dico_path = "/home/mn/EPITA/Design Patterns/Final_Project"
os.chdir(dico_path)

# Game factory to create the different types of games
class GameFactory:
    def create_game(self, game_type):
        """ Creates and return a game object of the game type selected. """
        self.type = game_type
        if self.type == 'Number Challenge':
            return NumberChallenge()
        elif self.type == 'Wordle':
            return Wordle() 
        elif self.type == 'Snake':
            return Snake() 
        else:
            raise ValueError('Invalid Game Type')

# Managing the different screens through a ScreenDraw class
# using State pattern
class ScreenDraw:
    def __init__(self, game):
        self.state = 'Game Menu' # Default state
        self.game = game # The game object

    def execute(self):
        """ Executes the draw funtion depending on the state and the
            game chosen. """
        if self.state == 'Main Menu':
            self.game = None
        elif self.state == 'Game Menu':
            self.draw_game_menu()
        elif self.state == 'Play Screen':
            self.draw_play_screen()
        elif self.state == 'Lose':
            self.draw_lose_screen()
        elif self.state == 'Win':
            self.draw_win_screen()       

    def center_pos(self, obj):
        """ Returns the right x position to center a button"""
        return (800 - obj.width)//2
    
    def draw_main_menu(self):
        pass

    def draw_game_menu(self):
        pass

    def draw_play_screen(self):
        pass

    def draw_win_screen(self):
        pass

    def draw_lose_screen(self):
        pass

class NumberChallengeDraw(ScreenDraw):
    """ Draw class for th number challenge. """
    def __init__(self, game):
        self.state = 'Game Menu'
        self.game = game

    def draw_game_menu(self):
        screen.clear()
        screen.fill(('#00001b')) # Background color
        screen.draw.text('Number Challenge Game', centerx=300, centery=75, color=(255,255,255), fontsize=65)
        screen.draw.text('Choose Your Level', centerx=300, centery=180, color=(255,255,255), fontsize=65)
        screen.draw.text('Press Escape to go back to the Main Menu', centerx=300, centery=750, color=(255,255,255), fontsize=30)

        # drawing the level buttons
        for i in self.game.level_buttons:
            i.draw()
        
        # Writting the level and the numbers asscociated with them
        for i,y in zip(self.game.levels.keys(), range(300,len(self.game.levels) * 70 + 301, 70)):
            screen.draw.text(f'Level {i}', (50, y + 10), color=('#EE51B1'), fontsize=65)
            screen.draw.text(f'{self.game.levels[i]} Numbers', (300, y), color=('#ffffff'), fontsize=65)
            
    def draw_play_screen(self):
        screen.clear()
        screen.fill(('#00001b')) # Background color
        # Displaying the level
        screen.draw.text(f'Level {self.game.level}', (470, 20), color=('#ffffff'), fontsize=50)
        
        # Drawing the cubes
        for i in self.game.cubes:
            i.draw()
        
        # Positioning the number next to the cube accordingly
        for i in range(len(self.game.cubes.content)):
            if i < 9:
                x = 50
            elif i == 9:
                x = 50
            elif i < 20 and i > 9:
                x = 200
            else:
                x = 350
            screen.draw.text(f'{i + 1}', (x - 15, self.game.cubes[i].y - 10), color=('#000000'), fontsize=30)
         
        # Drawing each cube with the "number assigned to it"
        for i in range(1, self.game.list_of_numbers.number_of_slots + 1):
            screen.draw.text(f'{self.game.list_of_numbers[i]}', (self.game.cubes[i - 1].x + 35, self.game.cubes[i - 1].y - 10), color=('#ffffff'), fontsize=40)
        
        # Drawing the number
        screen.draw.text(str(self.game.current_number), (280,60), color=(255,255,255), fontsize=65)
        screen.draw.text('Press Escape to go back to the Game Menu', centerx=300, centery=750, color=(255,255,255), fontsize=30)


    def draw_win_screen(self):
        screen.clear()
        screen.fill(('#00001b')) # Background color
        screen.draw.text('You Won !!! ', (200, 120), color=(255,255,255), fontsize=65)
        screen.draw.text('Congratulations', (120, 250), color=(255,255,255), fontsize=65)
        
        # Drawing replay button
        self.game.replay_button.draw()
        screen.draw.text('REPLAY', (self.game.replay_button.x - 90, self.game.replay_button.y - 20), color=('#EE51B1'), fontsize=65)
        screen.draw.text('Press Escape to go back to the Game Menu', centerx=300, centery=750, color=(255,255,255), fontsize=30)

    def draw_lose_screen(self):
        screen.clear()
        screen.fill(('#00001b')) # Background color
        screen.draw.text('You Lost ! ! ! ', (200, 150), color=(255,255,255), fontsize=65)
        screen.draw.text('Better Luck Next Time', (50, 230), color=(255,255,255), fontsize=65)
        
        # Drawing replay button
        self.game.replay_button.draw()
        screen.draw.text('REPLAY', (self.game.replay_button.x - 90, self.game.replay_button.y - 20), color=('#EE51B1'), fontsize=65)
        screen.draw.text('Press Escape to go back to the Game Menu', centerx=300, centery=750, color=(255,255,255), fontsize=30)

class WordleDraw(ScreenDraw):
    def draw_game_menu(self):
        # Colored squares to explain the game
        green_square = LetterContainer(30, 300, 'green')
        yellow_square = LetterContainer(30, 380, 'yellow')
        grey_square = LetterContainer(30, 460, 'grey')

        screen.fill('#FDD495')
        screen.draw.text('Welcome to \nWORDLE ', centerx=300, centery=120, color=(255,255,255), fontsize=80)
        screen.draw.text('Guess the word using the hints', centerx=300, centery=240, color=(255,255,255), fontsize=40)
        
        green_square.draw()
        screen.draw.text('The letter is in the right position', (110, 320), color=(255,255,255), fontsize=40)
        yellow_square.draw()
        screen.draw.text('The letter is in the wrong position', (110, 400), color=(255,255,255), fontsize=40)
        grey_square.draw()
        screen.draw.text('The letter is not in the word', (110, 480), color=(255,255,255), fontsize=40)
                
        screen.draw.text('Click the start button or press Enter to Start', centerx=300, centery=600, color=(255,255,255), fontsize=25)
        self.game.start_button.draw()
        screen.draw.text('START', (self.game.start_button.x - 75, self.game.start_button.y - 20), color=('#ffffff'), fontsize=65)
        screen.draw.text('Press Escape to go back to the Main Menu', centerx=300, centery=750, color=(255,255,255), fontsize=25)

    def draw_play_screen(self):
        screen.clear()
        screen.fill('#FDD495')
        screen.draw.text('Type your guess and press enter to validate', centerx=300, centery=75, color=(255,255,255), fontsize=30)
        screen.draw.text('Press Escape to go back to the Game Menu', centerx=300, centery=750, color=(255,255,255), fontsize=25)
        
        # Drawing the squares where the letters go
        for row in self.game.letter_containers:
                for container in row:
                    container.draw()

        # Draws a red box around the word if it is not in
        # the dictionnary
        if self.game.red_box is not None:
            self.game.red_box.draw(color='red')
        
        # Writting the letters in the squares
        for round in range(self.game.round + 1):
            for letter, num in zip(self.game.handle_typing.guess[round], range(len(self.game.handle_typing.guess[round]))):
                screen.draw.text(letter.upper(), (90 + num * 90, 165 + round * 90), color=(255,255,255), fontsize=80)   
             
    def draw_win_screen(self):
        screen.clear()
        screen.fill('#FDD495')
        screen.draw.text('You Won !!! ', (200, 120), color=(255,255,255), fontsize=65)
        screen.draw.text(f'Congratulations ! \n You got it \n in {self.game.round}', centerx=300, centery=250, color=(255,255,255), fontsize=65)
        # Drawing replay button
        self.game.replay_button.draw()
        screen.draw.text('REPLAY', (self.game.replay_button.x - 90, self.game.replay_button.y - 20), color=('#ffffff'), fontsize=65)

        # Drawing the container of the winning line
        for container in self.game.letter_containers[self.game.round - 1]:
            container.design.y = 400
            container.draw()
        
        # Drawing the letters of the winning line
        for letter, num in zip(self.game.handle_typing.guess[self.game.round - 1], range(len(self.game.handle_typing.guess[self.game.round -1]))):
            screen.draw.text(letter.upper(), (90 + num * 90, 400), color=(255,255,255), fontsize=80)   
            
    def draw_lose_screen(self):
        screen.clear()
        screen.fill('#FDD495')
        screen.draw.text('You Lost ! ', centerx=300, centery=150, color=(255,255,255), fontsize=65)
        screen.draw.text(f'The word was',centerx=300, centery=230, color='white', fontsize=80)
        screen.draw.text(f'{self.game.handle_typing.word.upper()}',centerx=300, centery=300 , color='red', fontsize=80)
        screen.draw.text('Your last guess', centerx=300, centery=380, color=('#ffffff'), fontsize=50)
        # Drawing replay button
        self.game.replay_button.draw()
        screen.draw.text('REPLAY', (self.game.replay_button.x - 90, self.game.replay_button.y - 20), color=('#ffffff'), fontsize=65)

        # Displaying last guess

        # Changing the positions of the containers and displaying them
        for container in self.game.letter_containers[self.game.round - 1]:
            container.design.y = 450
            container.draw()
        
        # Displaying the letters at the correct positions
        for letter, num in zip(self.game.handle_typing.guess[self.game.round - 1], range(len(self.game.handle_typing.guess[self.game.round -1]))):
            screen.draw.text(letter.upper(), (90 + num * 90, 460), color=(255,255,255), fontsize=80)   
            
class SnakeDraw(ScreenDraw):
    def draw_game_menu(self):
        # Apple and bomb for game description
        apple = Actor('apple.png', (65, 250))
        bomb = Actor('bomb.png', (65, 360))

        screen.clear()
        screen.blit('bg_image_snake.png', (0, 0)) # Background image
        screen.draw.text('Welcome to the \nSNAKE GAME ', centerx=300, centery=120, color=(255,255,255), fontsize=65)
        
        # Game description
        apple.draw()
        screen.draw.text('Apples make the snake longer', (110, 240), color=(255,255,255), fontsize=40)
        bomb.draw()
        screen.draw.text('Bombs reduce its size', (110, 350), color=(255,255,255), fontsize=40)
        screen.draw.text('If you hit the walls or when the snake \nbecomes too short you lose instantly', centerx=300, centery=480, color=(255,255,255), fontsize=40)
         
        screen.draw.text('Click the start button or press Enter to Start', centerx=300, centery=600, color='#00001b', fontsize=25)
        self.game.start_button.draw()
        screen.draw.text('START', (self.game.start_button.x - 70, self.game.start_button.y - 20), color=('#ffffff'), fontsize=65)
        screen.draw.text('Press Escape to go back to the Main Menu', centerx=300, centery=750, color=(255,255,255), fontsize=30)

    def draw_play_screen(self):
        def draw_snake(snake):
            """ Draws the snake."""
            # Drawing snake head - only the snake's head rotates           
            self.game.player.rotated_image.draw()
            # drawing the rest of the snake's body
            for i in snake.content[1:]:
                i.draw()

        screen.clear()
        screen.blit('bg_image_snake.png', (0, 0)) # Background image
        
        # Drawing the snake, the apple, the bomb and the score
        draw_snake(self.game.player)
        self.game.apple.draw()
        self.game.bomb.draw()
        screen.draw.text('Score: ' + str(self.game.score), (20,10), color=(255,255,255), fontsize=65)

        if not self.game.begin:
            screen.draw.text('Press any key to start', centerx=300, centery=400, color=(255,255,255), fontsize=80)
            
    def draw_win_screen(self): # Empty you can't win
        pass

    def draw_lose_screen(self):
        screen.clear()
        screen.blit('bg_image_snake.png', (0, 0)) # Background image
        screen.draw.text('You Lost ! ! ! ', (200, 150), color=(255,255,255), fontsize=65)
        screen.draw.text(f'SCORE: {self.game.score}', (50, 230), color=(255,255,255), fontsize=65)

        # Drawing replay button
        self.game.replay_button.draw()
        screen.draw.text('REPLAY', (self.game.replay_button.x - 90, self.game.replay_button.y - 20), color=('#ffffff'), fontsize=65)

# Define game classes for each game and implement the methods
# Singleton and Abstract Factory patterns for game classes
class Game:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.type = None # Game type
        self.drawer = None # Asscociated drawer object
        
    def on_key_down(self):
        pass

    def on_mouse_down(self, pos):
        pass

    def update(self):
        pass

    def draw(self):
        pass

class NumberChallenge(Game):
    # Storing game levels and their associated number challenge
    # in a dictionary
    levels = {i:j for i,j in zip(range(1,6), range(5, 26, 5))}
    max = 999 # Biggest number generated
    # Different colors for cubes
    cube_types = ['blue_cube1.png', 'pink_cube1.png', 'purple_cube1.png']
    # replay_button
    replay_button = Actor('number_button.png', (265, 450))
    
    # Creating a level button for each level
    #  and keeping them in a list
    level_buttons = []
    for i in range(5):
        level_buttons.append(Actor('number_button.png', (130, 335 + i * 70)))
    
    def __init__(self):
        self.type = 'Number Challenge'
        # Game Variables with their default values 
        self.lose = False
        self.win = False
        self.start = False
        self.level = None
        self.cubes = None
        self.list_of_numbers = ListOfNumbers()
        self.drawer = NumberChallengeDraw(self)
        # The current number that the player has to position
        self.current_number = self.generate_num()

    def reinitialize(self):
        self.lose = False
        self.win = False
        self.start = False
        self.list_of_numbers.empty()
        self.cubes = Cubes(self.list_of_numbers.number_of_slots, NumberChallenge.cube_types)
        # The current number that the player has to position
        self.current_number = self.generate_num()

    def generate_num(self):
        """ Returns a random number between 0 and the max
        that is not already in the list."""
        num = randint(0,NumberChallenge.max) 
        # Returns num only if it is not already in the list
        # Making sure that we do not get duplicates
        while num in self.list_of_numbers: 
            num = randint(0, NumberChallenge.max)
        return num
        
    def on_key_down(self, key):
        # Defining the behavior of the escape key
        if key == keys.ESCAPE:
                # Quits game if playing and goes to the game menu
                if self.drawer.state == 'Play Screen' or self.drawer.state == 'Lose' or self.drawer.state == 'Win':
                    self.reinitialize()
                    self.drawer.state = 'Game Menu'
                # Goes to the main menu if you're in the game menu
                elif self.drawer.state == 'Game Menu':
                    self.drawer.state = 'Main Menu'

    def on_mouse_down(self, pos):
        if not self.start:
            for i in NumberChallenge.level_buttons:
                if i.collidepoint(pos):
                    # Finds the level chosen by the player
                    self.level = NumberChallenge.level_buttons.index(i) + 1
                    # Set the lenght of the list of number
                    self.list_of_numbers.check_level(self.level)
                    # Passes the number of slots to the Cubes to create the right number of cubes
                    # through the Cubes class
                    self.cubes = Cubes(self.list_of_numbers.number_of_slots, NumberChallenge.cube_types)
                    # Starts the game
                    self.start = True
                    self.drawer.state = 'Play Screen'
        
        elif (self.start and (not self.win) and (not self.lose)): # when playing 
            # Checks which cube was selected by the player
            for i in self.cubes.content:
                if i.collidepoint(pos):
                    slot = self.cubes.content.index(i) + 1
                    # Adding the number to the list at the chosen position
                    status = self.list_of_numbers.add_number(self.current_number, slot)
                    
                    if status: # if number added succesfully
                        # checks if the list is full meaning the player won
                        if self.list_of_numbers.full(): 
                            self.win = True
                            self.drawer.state = 'Win' 
                        else: 
                            # generating a new number
                            self.current_number = self.generate_num()
                    
                    # if the number can't be placed anywhere in the list meaning
                    # the player lost
                    if status is None: 
                        self.lose = True  
                        self.drawer.state = 'Lose'                
        
        if self.lose or self.win:
            # If replay button is clicked
            if NumberChallenge.replay_button.collidepoint(pos):
                # Reinitializes the values and restart the game
                self.reinitialize()
                self.start = True
                self.drawer.state = 'Play Screen'

    def draw(self):
        """ Calls the execute function of the drawer object.
        The drawer object will show the correct screen based on its state """
        self.drawer.execute()
    
class Wordle(Game):
    def __init__(self):
        self.type = 'Wordle'
        self.drawer = WordleDraw(self)

        # Game Variables with default values as attributes
        self.lose = False
        self.win = False
        self.start = False
        self.round = 0
        self.letter_containers = [[], [], [], [], [], []]
        # dictionary of all 5 letter words to check if a word exist
        self.valid_dico = 'wordle_dico.txt' 
        self.valid_words = []
        # smaller dictionary where the words will be selected
        self.dico = 'dico.txt'
        self.dico_content = []   
        self.red_box = None     

        # Creating the buttons and setting their positions
        self.replay_button = Actor('wordle_button.png')
        self.replay_button.x = self.drawer.center_pos(self.replay_button)
        self.replay_button.y = 650
        self.start_button = Actor('wordle_button.png')
        self.start_button.y = 650
        self.start_button.x = self.drawer.center_pos(self.replay_button) 
        
    def reinitialize(self):
        self.lose = False
        self.win = False
        self.start = True
        # self.replay = False
        self.round = 0
        self.letter_containers = [[], [], [], [], [], []]   
        self.handle_typing = Typing(self.valid_words, self.dico_content)  
        self.red_box = None
        self.setting_up()  

    @staticmethod
    def get_content(file):
        """ Reads the content of a dictionary file and returns a list of
        all the words of the dictionary."""
        content = []
        with open(file, 'r') as dico:
            for line in dico:
                # Remove leading/trailing whitespace and adding it to the list
                content.append(line.strip()) 
        return content

    def setting_up(self):
        """ Gets the content of both th dictionaries and create a Typing object
        that will handle the typing and create th eletter containers."""
        self.dico_content = self.get_content(self.dico)
        self.valid_words = self.get_content(self.valid_dico)
        self.handle_typing = Typing(self.valid_words, self.dico_content) # creating the Typing object
        # Creating the letter containers            
        for i in range(6):
            for j in range(5):
                self.letter_containers[i].append(LetterContainer(80 + j * 90, 160 + i * 90))

    def on_key_down(self, key):
        # Handle the behavior o the escape key
        if key == keys.ESCAPE:
                # Goes to game menu screen after reinitializing
                if self.drawer.state == 'Play Screen' or self.drawer.state == 'Lose' or self.drawer.state == 'Win': 
                    self.reinitialize()
                    self.drawer.state = 'Game Menu'
                # Goes to the main menu
                elif self.drawer.state == 'Game Menu':
                    self.drawer.state = 'Main Menu'

        # Pressing return starts the game 
        if not self.start:
            if key == keys.RETURN:
                self.start = True
                self.drawer.state = 'Play Screen'
                self.setting_up()
        
        if self.start:
            if key in [i for i in range(97, 123)]: # if a letter is typed
                # Enter the letter
                self.handle_typing.enter_letter(chr(key), self.round)
            elif key == 8: # if Backspace is pressed
                # remove the last letter typed
                self.handle_typing.remove_letter(self.round)
            elif key == keys.RETURN: # when a word is submitted
                validate = self.handle_typing.validate(self.round)
                if validate == 'Invalid': # If the word is not in the dictionary
                    # Creating a red box around the guess if the word does not exist
                    self.red_box = LetterContainer(75, 155 + 90 * self.round, width=435, height=75)
                elif validate:
                    # if the word is in the dictionary, goes to the next round
                    self.round += 1
                
                    right_count = 0 # number of times  letter is at the right place
                    # Checks the state and changes the color of the box for each
                    # letter while increasing the right count
                    for cell in range(5):
                            if self.handle_typing.state[self.round - 1][cell] == 0:
                                self.letter_containers[self.round - 1][cell].change_color('grey')
                            elif self.handle_typing.state[self.round - 1][cell] == 1:
                                self.letter_containers[self.round - 1][cell].change_color('yellow')
                            elif self.handle_typing.state[self.round - 1][cell] == 2:
                                self.letter_containers[self.round - 1][cell].change_color('green')
                                right_count += 1
                                # if all the letters are right then the player wins
                                if right_count == 5:
                                    self.win = True
                                    self.drawer.state = 'Win' 
                    
                    # If it is the last round and the player did not win then they lose
                    if self.round == 6 and not self.win:
                        self.lose = True
                        self.drawer.state = 'Lose'

            # deletes the red box around the word when you have less than 5 letters        
            if self.handle_typing.current_slot <= 4:
                self.red_box = None

    def on_mouse_down(self, pos):
        # Start the game when the start button is clicked
        if self.drawer.state == 'Game Menu':
            if self.start_button.collidepoint(pos):
                self.start = True
                self.drawer.state = 'Play Screen'
                self.setting_up()
        
        if self.drawer.state == 'Lose' or self.drawer.state == 'Win':
            if self.replay_button.collidepoint(pos):
                # Reinitialize function to set everything to initial values 
                # and start the game
                self.reinitialize()
                self.drawer.state = 'Play Screen'

    def update(self):
        pass

    def draw(self):
        """ Calls the execute function of the drawer object.
        The drawer object will show the correct screen based on
        its state. """
        self.drawer.execute()

class Snake(Game):    
    def __init__(self):
        self.type = 'Snake'
        self.drawer = SnakeDraw(self)
        self.player = SnakePlayer() 
        # Game Variables with default values as attributes
        self.lose = False
        self.begin = False
        self.start = False
        self.score = 0
        self.drawer.state = 'Game Menu'
        self.replay_button = Actor('wordle_button.png', (265, 650))
        self.start_button = Actor('wordle_button.png', (265, 650))
        self.apple = Actor('apple.png', (randint(50, 550), randint(50, 750)))
        self.bomb = Actor('bomb.png', (randint(50, 550), randint(50, 750)))
    
    def reinitialize(self):
        self.lose = False
        self.win = False
        self.start = False
        self.begin = False
        self.score = 0
        self.player = SnakePlayer()

    def on_key_down(self, key):
        # Behavior of the escape key
        if key == keys.ESCAPE:
                # Reinitializes the game variables and goes to the game menu
                if self.drawer.state == 'Play Screen' or self.drawer.state == 'Lose' or self.drawer.state == 'Win':
                    self.reinitialize()
                    self.drawer.state = 'Game Menu'
                # Goes to the main menu if you're in the game menu
                elif self.drawer.state == 'Game Menu':
                    self.drawer.state = 'Main Menu'

        if self.begin:
            # Managing the movements of the snake based on the keys
            if key == keys.LEFT:
                self.player.direction = 'left' # set snake direction to left
                # Changing the angle to the right one based on the previous angle
                if self.player.rotation_angle == 180 or self.player.rotation_angle == -180:
                    self.player.rotation_angle -= 90 
                elif self.player.rotation_angle == 0 or self.player.rotation_angle == 360 or self.player.rotation_angle == -360:
                    self.player.rotation_angle += 90
                self.player.move_left() # moving the snake in the corresponding direction
        
            elif key == keys.RIGHT:
                self.player.direction = 'right' # set snake direction to right
                # Changing the angle to the right one based on the previous angle
                if self.player.rotation_angle == 180 or self.player.rotation_angle == -180:
                    self.player.rotation_angle += 90 
                elif self.player.rotation_angle == 0 or self.player.rotation_angle == -360 or self.player.rotation_angle == -360:
                    self.player.rotation_angle -= 90
                self.player.move_right() # moving the snake in the corresponding direction

            elif key == keys.UP:
                self.player.direction = 'up' # set snake direction to up
                # Changing the angle to the right one based on the previous angle
                if self.player.rotation_angle == 90 or self.player.rotation_angle == -270: 
                    self.player.rotation_angle -= 90 
                elif self.player.rotation_angle == -90 or self.player.rotation_angle == 270:
                    self.player.rotation_angle += 90
                self.player.move_up() # moving the snake in the corresponding direction

            elif key == keys.DOWN:
                self.player.direction = 'down' # set snake direction to down
                # Changing the angle to the right one based on the previous angle
                if self.player.rotation_angle == 90 or self.player.rotation_angle == -270:
                    self.player.rotation_angle += 90 
                elif self.player.rotation_angle == -90 or self.player.rotation_angle == 270:
                    self.player.rotation_angle -= 90 
                self.player.move_down() # moving the snake in the corresponding direction

            # subtracts from the angle so that it always is withing the
            # range (-360, 360)
            while self.player.rotation_angle > 360:
                self.player.rotation_angle -= 360
            while self.player.rotation_angle < -360:
                self.player.rotation_angle += 360
            
            # Rotating the head of the snake
            original_image = self.player.head()
            original_image.angle = self.player.rotation_angle
            self.rotated_image = original_image
        else:
            # if the game has started, pressing any key will make the snake move
            # by setting self.begin to True
            if self.start:
                self.begin = True
            else: # if game not started, pressing return will start it  
                if key == keys.RETURN:
                    self.start = True
                    self.drawer.state = 'Play Screen'

    def on_mouse_down(self, pos):
        if self.drawer.state == 'Game Menu':
            # Start the game if the start button is pressed
            if self.start_button.collidepoint(pos):
                self.start = True
                self.drawer.state = 'Play Screen'
        
        if self.drawer.state == 'Lose':
            # if the replay button is pressed
            if self.replay_button.collidepoint(pos):
                # Reinitialize function to set everything to initial values
                self.reinitialize()
                self.start = True
                self.drawer.state = 'Play Screen'

    def update(self):
        if self.begin:
            # If snake head touches apple, increase score
            if self.player.head().colliderect(self.apple):
                # "Respawn" the apple by changing its position
                self.apple.pos = (randint(50, 550), randint(50, 750))
                self.score += 10
                # Increase the lenght of the body of the snake
                self.player.add()

            # if snahead touches a bomb
            if self.player.head().colliderect(self.bomb):
                if len(self.player.body()) > 1:
                    # "Respawn" the bomb by changing its position
                    self.bomb.pos = (randint(50, 550), randint(50, 750))
                    self.player.remove() # decrease the lenght of the body of the snake
                else:
                    # Loses if the body of the snake is too short
                    self.lose = True
                    self.drawer.state = 'Lose'

            # if the snake's head hits the wall, the player loses
            if self.player.collide_body() or self.player.collide_wall():
                self.lose = True
                self.drawer.state = 'Lose'

            # Increases the speed proportionally to the player's score
            self.player.move(self.score/40) 

    def draw(self):
        """ Calls the execute function of the drawer object.
        The drawer object will show the correct screen based on
        its state.  """
        self.drawer.execute()

############### For number Challenge ###############

# Class that manages the list of number: adding numbers, checking the position so 
# that the list remains ordered
class ListOfNumbers:
    def __init__(self, number_of_slots=0):
        self.number_of_slots = number_of_slots
        self.content = {i:'' for i in range(1, self.number_of_slots + 1)}
    
    def __getitem__(self, slot):
        return self.content[slot]
    
    def __setitem__ (self, slot, value) -> None:
        self.content[slot] = value
    
    def __len__(self):
        return len(self.content)
    
    def add_number(self, num, slot):
        """ Tries adding the num in the list at the position provided.
        Returns None if no available slots to put the number.
        Returns False if there are available slots but slot is 
        not one of them. Returns True if the number was added successfully  """
                   
        available_slots = self.check_available_slots(num)
        if not available_slots: # if it is empty
            return None
        
        # checks if 'slot' is in the available slots, returns False if not
        # meaning that the number cannot be at position 'slot' but could
        # be place elsewhere in the list
        for i in available_slots:
            if i == slot:
                self[slot] = num
                return True
        return False
        
    def __str__(self):
        repr = ''
        for i in range(1, self.number_of_slots + 1):
            repr += f'{i} : {self[i]}\n' 
        return repr
    
    def check_available_slots(self, num, start = 1, available_slots = []):
        """ Checks and returns the available slots (the potential slots where
        the number could be placed in the list). Returns the available slots as a
        list of number or returns None if none were found."""
        
        # if the list is empty returns all the slots starting from 'start'
        if all(self[i] == '' for i in range(start, self.number_of_slots + 1)):
            return [i for i in range(start, self.number_of_slots + 1)]

        # if the start is greater than the number of slots then
        # stop the search because everything was checked
        if start == self.number_of_slots + 2:
            return available_slots
        
        # If the slot is empty, adds it to the available slots
        if self[start] == '':
            available_slots.append(start)
            # Recursively calls the function for the next slot
            return self.check_available_slots(num, start = start + 1, available_slots = available_slots)
        
        # If the current number is greater than the number we need to position 
        # meaning we can't position the number further, returns available slots
        elif self[start] > num: 
            return available_slots
        
        # If the current number is less than the number we need to position meaning 
        # we can't put it before that number 
        elif self[start] < num:
            available_slots = [] # empty available slots 
            # keep checking for the next slot
            return self.check_available_slots(num, start = start + 1, available_slots = available_slots)
    
    def check_level(self, level):
        """ Check the level chosen by the user and changes the value of the
        number_of_slots attribute accordingly. 
        Updates the content and deletes any previous values.
        Returns None."""

        if level == 1:
            self.number_of_slots = 5
        elif level == 2:
            self.number_of_slots = 10
        elif level == 3:
            self.number_of_slots = 15
        elif level == 4:
            self.number_of_slots = 20
        elif level == 5:
            self.number_of_slots = 25
        
        self.content = {i:'' for i in range(1, self.number_of_slots + 1)}

    def full(self):
        """ Returns true if the list is full and false otherwise."""
        return all(i != '' for i in self.content.values())
    
    def empty(self):
        """ Empty the content of the list by setting evry value to an
        empty string. """
        self.content = {i:'' for i in range(1, self.number_of_slots + 1)}
    
    def __contains__(self, number):
        return number in self.content.values()

# Class that manages the creation and positioning of the cubes 
class Cubes:
    def __init__(self, number_of_cubes, cube_types=['blue_cube1.png']):
        self.number_of_cubes = number_of_cubes
        self.cube_types = cube_types
        self.content = []
        self.create_cubes()
    
    def __contains__(self, item):
        return item in self.content
    
    def __getitem__(self, index):
        return self.content[index]
    
    def __setitem__ (self, index, value) -> None:
        self.content[index] = value
    
    def create_cubes(self):
        """ Generates and returns a list of number_of_slots amount of cube (actor objects). 
        The color of each cube is randomly generated. 
        Returns a list of Actor objects"""

        # Changes the x positions of the cubes tofit the screen depending on the number
        # of cubes
        for i in range(self.number_of_cubes):
            if i == 0:
                self.content.append(Actor(self.cube_types[randint(0, 2)], (50, 200)))
            elif i < 10:
                self.content.append(Actor(self.cube_types[randint(0, 2)], (50, self.content[i - 1].y + 50)))
            elif i == 10:
                self.content.append(Actor(self.cube_types[randint(0, 2)], (200, 200)))
            elif i > 10 and i < 20:
                self.content.append(Actor(self.cube_types[randint(0, 2)], (200, self.content[i - 1].y + 50)))
            elif i == 20:
                self.content.append(Actor(self.cube_types[randint(0, 2)], (350, 200)))
            elif i > 20:
                self.content.append(Actor(self.cube_types[randint(0, 2)], (350, self.content[i - 1].y + 50)))

############### For Snake ###############

class SnakePlayer:
    snake_parts = ['mini_snake_head.png', 'snake_body.png','mini_snake_tail.png']
    
    def __init__(self):
        self.content = [Actor('mini_snake_head.png', (300, 300)), Actor('1st_body.png', (340, 300)), Actor('mini_snake_tail.png', (380, 300))]
        self.rotation_angle = 90
        self.rotated_image = self.content[0]
        self.rotated_image.angle = self.rotation_angle
        self.direction = 'left'

    def head(self): # Maybe make it a property
        return self.content[0]
    
    def tail(self): # Maybe make it a property
        return self.content[-1]
    
    def body(self):
        return self.content[1:-2]
    
    # def collide_tail(self):
    #     return self.content[0].colliderect(self.content[-1])

    def collide_body(self):
        return any([self.content[0].colliderect(i) for i in self.content[2:]])

    def collide_wall(self):
        if self.content[0].x >= 600 or self.content[0].x <= 0:
            return True
        if self.content[0].y >= 800 or self.content[0].y <= 0: 
            return True
        return False
    
    def add(self):
        self.content.insert(-1, Actor('mini_snake_body.png', (self.content[-2].x + 25, self.content[-2].y)))
        self.content[-1].pos = (self.content[-2].x + 40, self.content[-2].y)

    def remove(self):
        self.content.pop(-2)
        self.content[-1].pos = (self.content[-2].x + 40, self.content[-2].y)

    def move(self, speed):
        self.speed = speed
        if self.direction == 'left':
            self.move_left()
        elif self.direction == 'right':
            self.move_right()
        elif self.direction == 'up':
            self.move_up()
        elif self.direction == 'down':
            self.move_down()

    def move_right(self):
        for i in self.content:
            i.x += 3 + self.speed

    def move_left(self):
        for i in self.content:
            i.x -= 3 + self.speed
            
    def move_up(self):
        for i in self.content:
            i.y -= 3 + self.speed

    def move_down(self):
        for i in self.content:
            i.y += 3 + self.speed

############### For Wordle ###############

class LetterContainer:
    def __init__(self, x, y, color=None, width=65, height=65):
        # self.design = Rect(position, width_height=(45, 45))
        self.design = Rect(x, y, width, height)
        self.design.x = x
        self.design.y = y
        self.color = color
    
    def __str__(self) -> str:
        return f'LetterContainer: {self.design}\n Position: {self.design.x, self.design.y}\nColor: {self.color}\n'
    
    def draw(self, color='black'):
        if self.color is not None:    
            screen.draw.filled_rect(self.design, self.color)
        else:
            screen.draw.rect(self.design, color)
    
    def set_position(self, x, y):
        # self.position = Rect(x, y, width_height=45)  
        self.design.x = x
        self.design.y = y
    
    def change_color(self, color):
        self.color = color

class Typing:
    def __init__(self, valid_words, dico):
        self.dico = dico
        self.valid_words = valid_words
        self.current_slot = 0
        self.generate_word()
        self.guess = [[], [], [], [], [], []]
        self.state = [[None, None, None, None, None], [None, None, None, None, None], 
                      [None, None, None, None, None], [None, None, None, None, None], 
                      [None, None, None, None, None], [None, None, None, None, None]]
    
    def generate_word(self):
        max = len(self.dico) - 1
        self.word = self.dico[randint(0, max)]
        self.word_counter = Counter(self.word)
    
    def check_word(self, round):
        # used to make sure the game displays the right colors (hints)
        # when a letter is multiplied
        counter = Counter(self.word)
        for i in range(5):
            if self.guess[round][i] == self.word[i]:
                self.state[round][i] = 2
                if counter[self.guess[round][i]] != 0:
                    counter[self.guess[round][i]] -= 1
                else:
                    # If the letter had been marked before, 
                    # marks it yellow instead and marks it green at the current position
                    self.state[round][self.guess[round].index(self.word[i])] = 0
            elif self.guess[round][i] in ''.join(self.word) and counter[self.guess[round][i]] != 0:
                self.state[round][i] = 1
                counter[self.guess[round][i]] -= 1
            else:
                self.state[round][i] = 0  
    
    def enter_letter(self, letter, round):
        if self.current_slot < 5:
            self.guess[round].append(letter)
            self.current_slot += 1

    def remove_letter(self, round):
        if len(self.guess[round]) >= 1:
            self.guess[round].pop()
            self.current_slot -= 1

    def validate(self, round):
        if self.current_slot == 5: 
            if ''.join(self.guess[round]) in self.valid_words:
                self.check_word(round)
                self.current_slot = 0
                return True
            else:
                return 'Invalid'
        return False
        
###################################### Pygame Zero Main Part ######################################

# To keep track of the games and the state
class Session:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.game = None
        self.game_start = False

# Setting game window size
HEIGHT = 800
WIDTH = 600

# Creating a session object
session = Session()

# Create the game icons
game_icons = [Actor('number_challenge_icon.png', (120, 400)), Actor('snake_icon.png', (460, 560)), Actor('wordle_icon.png', (120, 700))]

games = ['Number Challenge', 'Snake', 'Wordle']

game_factory = GameFactory() # Creating the game factory

def on_key_down(key):
    # If no game is selcted, exit, otherwise, execute the function for the
    # selected game
    if session.game is None or session.game.drawer.state == 'Main Menu':
        if key == keys.ESCAPE:
            exit()
    else:   
        session.game.on_key_down(key)

def on_mouse_down(pos):
    # If no game is selected
    # Creates an instance of the game chosen by the user
    if session.game is None or session.game.drawer.state == 'Main Menu':
        for i in game_icons:
            if i.collidepoint(pos):
                session.game = game_factory.create_game(games[game_icons.index(i)])           
    else:
        # Otherwise, execute the function for the selected game
        session.game.on_mouse_down(pos)

def update() :
    # Execute the function for the selected game if a game is selected
    if session.game is None or session.game.drawer.state == 'Main Menu':
        pass
    else:
        session.game.update()

def draw():
    # Display the main menu screen
    if session.game is None or session.game.drawer.state == 'Main Menu':
        screen.fill(('#00001b'))
        screen.draw.text('MINI GAMES', (150, 50), color=(255,255,255), fontsize=65)
        screen.draw.text('WHICH GAME DO \nYOU WANNA PLAY', (100, 150), color=(255,255,255), fontsize=65)

        screen.draw.text('Number \n Challenge', (250, 320), color=('#ffffff'), fontsize=90) 
        screen.draw.text(f'{games[1]}', (130, 530), color=('#ffffff'), fontsize=90) 
        screen.draw.text(f'{games[2]}', (280, 670), color=('#ffffff'), fontsize=90) 

        for icon in game_icons:
            icon.draw()
    else:
        # Execute the function for the selected game if a game is selected
        session.game.draw()

# Running the game
pgzrun.go()
