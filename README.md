# mini_games_pygame_zero

This project is a collection of three mini-games developed using Pygame Zero. The project provides a fun and interactive gaming experience with the following games:

    Number Challenge: Sort random numbers in ascending order without prior knowledge of the next number.
    Snake: Classic snake game where you control a snake to eat food and grow longer while avoiding collisions with walls or bombs.
    Wordle: A word-guessing game where you attempt to guess a secret word by inputting words and receiving feedback on correctness.

The project leverages Pygame Zero, a beginner-friendly game development framework that simplifies game creation and provides a straightforward API for handling game logic, graphics, and input.

Installation
To run the game, follow these steps:

    Download the zip file containing all the necessary files
    Ensure you have at least Python (version 3.10.x) installed on your system.
    Install the necessary dependencies (pygame and pygame zero) by running the following command in your terminal:
    Note: These steps are only necessary if you do not have pygame and pygame zero installed on your computer.

Run `pip install pygame zero` and `pip install pygame`

Note:
Sometimes the script has trouble accessing the dictionary files (for the Wordle game) inside the folder. To avoid that issue,
you can manually change the 'dico_path' variable on line 14 to the absolute path of the folder containing the dictionary. 
Make sure to do this if the Wordle game does not work.

Game Descriptions

Number Challenge
The objective is to arrange a series of random numbers in ascending order without prior knowledge of the next number in the sequence. The game offers five different levels of difficulty, each presenting a list of numbers 5 to 25 numbers.

Snake
The Snake game is a classic arcade game where you control a snake and guide it to eat apples, which make the snake grow longer. Be careful not to collide with walls or bombs it will result in game over. Try to achieve the longest possible length and beat your previous records.

Wordle
Wordle is a word-guessing game where you're given a secret word of a specific length. You'll need to input words and receive feedback on correctness. Use the feedback to narrow down the possible word options and try to guess the secret word within the given number of attempts. Test your vocabulary and deduction skills to crack the code!

Game Controls
Each game in the has its own set of controls:

Number Challenge Controls
    Use the mouse to select the position of the given number in the list.

Snake Controls
    Use the arrow keys (Up, Down, Left, Right) to control the snake's movement.

Wordle Controls
    Type words using the keyboard and press Enter to submit your guesses.

Design Pattern Usage Overview:
In our project, we have employed several design patterns to enhance the structure and behavior of our code.

Creational Patterns
    Singleton Pattern:
    We have utilized the Singleton pattern for the Game classes and the Session class. This ensures that only a single instance of each class is created, promoting global access and avoiding unnecessary duplication.

    Factory Pattern:
    To centralize the creation of games, we have adopted the Factory pattern. The GameFactory class encapsulates the logic for creating games, providing a unified interface for game instantiation.

Structural Patterns
    Bridge Pattern:
    The Bridge pattern plays a crucial role in managing the draw functions for each game. By implementing an instance attribute (self.drawer) as a ScreenDraw object, we achieve a separation between the game logic and the drawing functionality. This allows for flexible drawing behavior specific to each game. The relationships between the Game classes and other classes also exhibit characteristics of the Bridge pattern, such as the ListOfNumbers object in NumberChallengeGame and the SnakePlayer object in the Snake game. Additionally, the Wordle game class incorporates the Typing class as an instance attribute, further exemplifying the usage of the Bridge pattern.

Behavioral Patterns
    State Pattern:
    To manage the different states of the drawer, determining which draw function to invoke, we have employed the State pattern. By defining various states such as "Game Menu," "Win," or "Play Screen," the drawer adapts its behavior accordingly. For instance, if the game has not yet started, the game menu is displayed, while a win state triggers the display of the win screen. This pattern provides a flexible and extensible approach to handle varying states and their associated behaviors.

Through the application of these design patterns, our project demonstrates enhanced modularity, code organization, and flexibility, leading to improved maintainability and extensibility.

Author: Maïmouna N'Diaye
