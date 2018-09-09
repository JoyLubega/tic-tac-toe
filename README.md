[![Namuli Joyce](https://img.shields.io/badge/Namuli%20Joyce-TicTacToe-green.svg)]()
[![Coverage Status](https://coveralls.io/repos/github/JoyLubega/tic-tac-toe/badge.svg?branch=ft-gameplay)](https://coveralls.io/github/JoyLubega/tic-tac-toe?branch=ft-gameplay)
[![Build Status](https://travis-ci.org/JoyLubega/tic-tac-toe.svg?branch=master)](https://travis-ci.org/JoyLubega/tic-tac-toe)
 [![Maintainability](https://api.codeclimate.com/v1/badges/93370e098a6dc0e82c5e/maintainability)](https://codeclimate.com/github/JoyLubega/tic-tac-toe/maintainability)

# TIC-TAC-TOE API

This api plays the game called tic-tac-toe in the US, and called naughts and crosses in some countries.  Instructions for how to play the game are here if you’ve never played before: http://www.exploratorium.edu/brain_explorer/tictactoe.html

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
- Just clone this repository by typing: `https://github.com/JoyLubega/tic-tac-toe.git`
- Switch to project directory: `cd tic-tac-toe`
- Install project requirements using python pip. But wait, you have to have some stuff before you get to this point. So these are:

### Prerequisites

- Python3.6 and above
- Python virtual environment
Just type:
```
python -V
```
in your terminal and if its not greater than or equal to 3.6, you're not in big trouble, there are tons of tutorials to get up up and running with these. Just grub one then come back when done.

### Installing

Now, you have python3 and a way of running a virtual environment. Lets set up the project environment.(remember we're still in the app directory)

1. Create your virtual environment. Usually, without any wrappers:
```
python -m venv env
```
2. Start your virtual environment:
```
source env/bin/activate
```
3. Install the project requirements specified in the requirements.txt file. Usually,
```
pip install -r requirements.txt
```


This is enough to get you started.
You can now run the api using:

`python run.py`

    
## Running the tests

Easy, just: `nosetests --with-coverage`

## API Endpoints
You can use postman or even curl to reach out to the following api endpoints:

URL Endpoint	|               HTTP Request    | Resource Accessed | Access Type|
----------------|-----------------|-------------|------------------
/game           |      GET	      | Get the next move|publc




## Built With

* [Python Flask](https://www.fullstackpython.com/flask.html) - The web framework used for this API

## Acknowledgments

* Andela  - Inspiring the idea.