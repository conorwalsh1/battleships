<h1 align="center">Battleships Game</h1>

![Responsive Test](assets/images/ceart-responsive.png)

---

[Live Website](https://conorwalsh1.github.io/ceart-kids-quiz/)

[Github Repository](https://github.com/conorwalsh1/ceart-kids-quiz)

---

# About

Welcome to Battleships. Battleships is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

Users play against a computer over a series of rounds to see who can find their opponents battleships first.

This website was built using a Macbook Pro 13".

## How To Play

Battleships is based on the classic pen-and-paper game. You can read more about it here on Wikipedia.

The player is prompted to enter their name, after which instructions are given and two boards are generated.

Player can see their ships idicated by the '@' symbol, but they cannot see where the computers ships are.

Guess are marked on board with an 'X', whilst hits are marked with a '$'.

Each new round allows player and computer to make a guess.

The game continues until one of the players sinks all of the others battleships.
    
## Features

- Random board generation.

- Ships are randomly placed on both boards at the start of each round.

-  Computer ships hidden from player.

- Accepts user input.

- Play against a computer.

- Alerts player when each ship has been hit how many are remaining on the board.

- Input validation - Players must enter a number within range of the board size and it must be a number, not a letter.

- Different messages generate at the end of the game, depending on if players wins or loses.

## Features To Add In Future

-   Larger ships that are bigger than just 1x1 coordinate.

- Player allowed to decide where their ships are placed.

- Player allowed to set board size and amounts of ships.

## Data Model

### Languages Used

-    Python

## Testing

I have manually tested the project by doing the following:

- Passed code through PEP8  linter which confirmed there are no problems.

- Gave invalid inputs, such as numbers outside range and letters instead of numbers.

- Tested in my local terminal and the Code Institute Heroku terminal.

### Fixed Bugs

- Each new round was producing a brand new board with new coordinates as I was running the create_board function in my next_round function as opposed to printing the board.

- The game would not come to a close as I had entered the next_round function an extra time by mistake, thus causing new rounds to constantly be generated.

### Remaining Bugs

-   There are no known bugs at this time.

## Deployment

This project was deployed using Code Institutes mock terminal for Heroku.

Deployment steps:

- Fork or clone this repository.

- Create a new Heroku app

- Set the buildbacks to Python and NodeJS in that order

- Link the Heroku app to the repository

- Click on deploy

### Content

-   Code Institute README.md template.

- Wikipedia for the details of the Battleships game.

-   All other content was written by Conor Walsh.


### Acknowledgements

-   I would like to thank my mentor Maria Hynes for guiding me along the right path throughout our mentoring sessions. There were times I struggled with getting the way I wanted the code to look out of my head and onto the screen, but she gave me great motivation to persevere and I am very grateful for her assistance. I would also like to thank the tutors that helped me along the way.

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

https://www.youtube.com/watch?v=waTN4mBWMtA - Board