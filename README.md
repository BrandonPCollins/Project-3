# Project 3 - Battleships 

![image](https://github.com/BrandonPCollins/Project-3/assets/131177569/49b95c33-2d48-47a6-bc50-2895e4d2900a)

My Python terminal project is a replication of the classic Pen and Paper game [Battleships](https://en.wikipedia.org/wiki/Battleship_(game)).

The game presented here is a single-player guessing game presented under the conceit of an Alien Invasion. Matched against an AI opponent, the player must guess the location of all the AI's randomly placed Battleships before the AI can guess theirs. To add an extra layer of intensity, and to stop games from dragging, the player must complete this task within 15 turns, or lose. 

[The live version of my project can be found here](https://project-3-3f38e4872683.herokuapp.com/)

## Features

### Future Features 

* Allow the player to set the variables for board size and ship size.
* Allow for the players to customise the number of turns they'd like to play for, adding an unlimited turns mode.
* Allow the player to place their ships manually rather than having them be placed randomly.
* Allow for ships that are larger than 1x1 space, as in the Battleships board game.

## Data Model? 

## Testing

I had several "play-testers" engage with the Heroku hosted app prior to the final submission of the project. I received valuable feedback from them regarding mechanics and the UI of the game. Per their suggestions, I relocated the string informing the player how many turns was remaining in order to improve its visibility, while also increasing the number of turns available to the player. While a 10-turn time limit was more acceptable prior to the introduction of a competitive AI, with its implementation came the introduction of another failstate wherein the computer hits all the player's ships. Thus the turn count was increased to be more leniant on the first fail-state of time expiration to allow the player to have a greater opportunity of winning the game. 

## Bugs

There were several bugs battled during the implementation of this project, particularly related to the rudimentary AI.

There was an error 
![image](https://github.com/BrandonPCollins/Project-3/assets/131177569/8b52da87-6039-4c9c-97bf-0b6bffae9b49)


## Deployment

The project was deployed on Heroku using the mock terminal provided by Code Institute.

## Credits 

* The [How to Code Battleships in Python](https://www.youtube.com/watch?v=tF1WRCrd_HQ) by Knowledge Mavens on youtube was instrumental in giving my initial code the basis to build on. 

* The Code Institute [Ultimate Battleships](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/) sample ReadMe for providing the idea for the project.


## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
