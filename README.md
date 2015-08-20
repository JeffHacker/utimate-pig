# Run pig_basic.py and pig_interactive.py using Python3
# Run pig_charting.ipynb using Ipython Notebook

## Ultimate Pig
 
## Description

Use Monte Carlo simulations to find the ultimate player of Pig Solitaire.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Modeling games and simulations

### Performance Objectives

After completing this assignment, you should be able to:

* Play Pig well
* Use subclasses
* Create Monte Carlo simulations

## Details

### Deliverables

* A Git repo containing at least:
  * an IPython notebook
  * a `requirements.txt` file

### Requirements  

* At least 5 different charts

## The Rules of Pig Solitaire

In 7 turns, you are attempting to get the highest score possible.

Each turn, you have two choices:

* __Roll__. Roll a six-sided die. If you roll a 1, your turn is over and you add no points to your score. Roll a 2 - 6, and you can add that number to your turn total and .
* __Hold__. If you hold, you add the turn total to your score.


## Normal Mode

Create a simulation of different types of players of Pig Solitaire. You should have a base Player class that only rolls once per turn. Then create Player subclasses -- at least 2 -- that have different strategies. Create charts showing how they do in a large number of trials. Attempt to create an optimal player and back up your assertion with charts and data.

Your classes, findings, and charts should be in an IPython notebook.

## Hard Mode

In addition to the requirements from **Normal Mode**:

Once you have your optimal Pig Solitaire player, create a second simulation. This could be in a separate notebook or the same one. This simulation will be of the game of Pig. Pig works like Pig Solitaire, but you play against another person, and are trying to be the first to score 100 points. There is no round limit.

Create a new type of player for Pig. Your new player should play against the strategy as your optimal Pig Solitaire player. (You will probably have a new class for your optimal Pig Solitaire player, as playing Pig will need the class to take in more data each turn.) Try to create an optimal competitive Pig player, when the opponent is your optimal Pig Solitaire player. Back up your assertions with charts and data.

## Additional Resources

* [Demonstration of how to give game state to simulated players](http://nbviewer.ipython.org/gist/cndreisbach/c2bad3de531e2b6122a9#)
