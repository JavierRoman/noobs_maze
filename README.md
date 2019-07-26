# Noops maze challenge solver.

In this project I implemented a very complete and easy to use program to solve Noops Maze Challenge (https://github.com/noops-challenge/mazebot). 

I'll be adding more algorithms in the future. For now only A Star Search algorithm is implemented. 

### Dependencies

You just need Python 3 to run this program.

### Use

Clone this repo in your computer and run:

```
python solver.py -h
```

This will show some help.

The arguments of this program are:  
**Required**
* -a --algorithm [algorithm]: Specifies the algorithm to use to solve the mazes.  

**Race mode**
* -r --race [username]: Starts race mode specifying the player's github username.

**Test mode**
* -n --numMazes [number of mazes]: Number of random mazes to solve.
* -m --minSize [minimum maze size]: Minimum maze size.
* -M --maxSize [maximum maze size]: Maximum maze size.  
  
You can't use Race Mode and Test Mode at the same time. The example below will fail.
```
python solver.py -a a_star -r javierroman -n 100
```
### Examples
After running the example below the program calls noops API to participate in a race with the name javierroman. It solves every maze in it.
```
python solver.py -a a_star -r javierroman
```
The example below serves as a test of the program. It asks for 10 random mazes with sizes between 10x10 and 20x20.
```
python solver.py -a a_star -n 10 -m 10 -M 20
```
If you don't specify -m and -M arguments 10 and 200 are used as defaults respectively.
```
python solver.py -a a_star -n 10
```

### Contribute
Feel free to contribute and to suggest new algorithms to be implemented.
