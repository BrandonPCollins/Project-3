![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome USER_NAME,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

# Project 3 - Battleships 

![image](https://github.com/BrandonPCollins/Project-3/assets/131177569/1f99f1d0-9777-488e-a794-954c3ee3d006)


https://project-3-3f38e4872683.herokuapp.com/ 

## How to Play 

My Python project is based on the classic Pen and Paper game Battleships.

## Features

### Future Features 

## Data Model? 

## Testing

I had several "player-testers" engage with the Heroku hosted app prior to the final submission of the project. I received valuable feedback from them regarding mechanics and the UI of the game. Per their suggestions, I relocated the string informing the player how many turns was remaining in order to improve its visibility, while also increasing the number of turns available to the player. While a 10-turn time limit was more acceptable prior to the introduction of a competitive AI, with its implementation came the introduction of another failstate wherein the computer hits all the player's ships. Thus the turn count was increased to be more leniant on the first fail-state of time expiration to allow the player to have a greater opportunity of winning the game. 

## Bugs

There were several bugs battled during the implementation of this project, particularly related to the rudimentary AI.

## Deployment

The project was deployed on Heroku using the mock terminal provided by Code Institute.

## Credits 






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
