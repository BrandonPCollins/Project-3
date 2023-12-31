# Project 3 - Battleships 

![image](https://github.com/BrandonPCollins/Project-3/assets/131177569/49b95c33-2d48-47a6-bc50-2895e4d2900a)

My Python terminal project is a replication of the classic Pen and Paper game [Battleships](https://en.wikipedia.org/wiki/Battleship_(game)).

The game presented here is a single-player guessing game presented under the conceit of an Alien Invasion. Matched against an AI opponent, the player must guess the location of all the AI's randomly placed Battleships before the AI can guess theirs. To add an extra layer of intensity, and to stop games from dragging on, the player must complete this task within 15 turns, or lose. 

[The live version of my project can be found here](https://project-3-3f38e4872683.herokuapp.com/)

## Features

* Random board generation for both the player and the opposing AI. 

* Game accepts user input. The player enters a row, numbered 1 through 8, and a column, lettered A through H, in order to select a coordinate to attempt to "hit" the enemy ships. The player wins the game by hitting all 5 of the randomly placed ships on the opponent's board.

* Player's ships are demarcated with a blue 'O'

* Hit ships are denoted with a red 'X'

* Missed hits are shown via a '-'

![image](https://github.com/BrandonPCollins/Project-3/assets/131177569/fa41ec78-7104-4ca9-8b1d-a0492ddf54c2)

* Input validation, ensuring the player's guesses are within the grid board and preventing them from guessing the same position twice.

* AI opponent which will randomly guess player ship locations. 

* Win/Loss tracking at the conclusion of each game, numbering how many times the player has defeated or lost to the AI Aliens.

* Loop to allow the player to play again upon game completion

![image](https://github.com/BrandonPCollins/Project-3/assets/131177569/5a19d006-cc0d-4008-afb3-eed18f7a8b49)

### Future Features 

* Allow the player to set the variables for board size and ship size.
* Allow for the players to customise the number of turns they'd like to play for, adding an unlimited turns mode.
* Allow the player to place their ships manually rather than having them be placed randomly.
* Allow for ships that are larger than 1x1 space, as in the Battleships board game.

## Data Model

This project makes use of the Board class as its primary model. The game makes use of 3 instances of the Board class. The AI's board is composed of a Hidden Board; which is used to hold the hidden ships, and a Guess Board; displaying the player's current progress and updating as appropriate based on their input.

The Player's Board is a single board, used as an argument in the Create Ships function. There is no need to have a separate hidden board as the player is always aware of the state of their own board, including their own randomly placed ships and the status of the AI's guesses.

The boards are reprinted and updated at the conclusion of each turn cycle.

## Testing

I had several "play-testers" engage with the Heroku hosted app prior to the final submission of the project. I received valuable feedback from them regarding the mechanics and the UI of the game. Per their suggestions, I relocated the string informing the player how many turns was remaining in order to improve its visibility, while also increasing the number of turns available to the player. While a 10-turn time limit was more acceptable before introducing a competitive AI, with its implementation came the introduction of another fail state wherein the computer hits all the player's ships. Thus the turn count was increased to be more lenient on the first fail-state of time expiration to allow the player to have a greater opportunity of winning the game. 

For my validator testing I made use of PEP8online.com. It returned various errors relating to the ASCII art and my use of # in-line comments, though I wasn't certain how to remedy those and they had no effect on the functionality of the code so they were acceptable. 

It also helpfully noted the massive amount of white space my code contained, which I promptly removed via an auto-formatter. 

## Bugs

There were several bugs battled during the implementation of this project, particularly related to the rudimentary AI.

* Error where entering multiple letters within the column letter range. Fixed by including a length check on the user input to not exceed a single character.
![image](https://github.com/BrandonPCollins/Project-3/assets/131177569/8b52da87-6039-4c9c-97bf-0b6bffae9b49)

* Multiple logic path errors where the game would suddenly end after the first turn. Fixed by refactoring the AI turn logic.

* Bug where if the player chose to play again the boards would remain the same, including guesses and hit ships. Fixed by adding a loop which clears the board to the create ships function.

* Bug where if the player picked the same coordinates twice, the aliens would get a free turn. Fixed by incorporating a double pick into the get ships location function and preventing the game from proceeding by returning a value error until the player picked a new location.
  
## Known Bugs

* Errors within the validator relating to the use of ASCII art and in-line comments. Has no effect upon the code's functionality.

## Deployment

The project was deployed on Heroku using the mock terminal provided by Code Institute.

* Using Heroku credits create a new Heroku App.
* Set buildpack dependencies to Python and then NodeJS in the settings tab. They must be in this order.
* Link the Heroku app to the github repository
* Click **Deploy**

## Credits 

* The [How to Code Battleships in Python](https://www.youtube.com/watch?v=tF1WRCrd_HQ) by Knowledge Mavens on youtube was instrumental in giving my initial code the basis to build on. 

* The Code Institute [Ultimate Battleships](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/) sample ReadMe for providing the idea for the project.

* Code Institute for providing the template for the deployment terminal.

* Wikipedia's page for reference on the Battleship game.
