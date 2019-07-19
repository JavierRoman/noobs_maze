# Author: Javier Roman

import sys
from argparse import ArgumentParser
from maze_algorithms import a_star
from maze_utils import euclidean, MazeSolverArgumentsException
from noops_maze_api import *

algorithms = {"a_star": a_star} # Dictionary with different maze solving algorithms.

def parse_args():
    """
    This function parses execution arguments and return them.
    
    Raises:
        MazeSolverArgumentsException: This exception is raised when a conflict is found between arguments.
    
    Returns:
        class: Class with the different arguments.
    """
    parser = ArgumentParser()
    required_group = parser.add_argument_group('required arguments')
    required_group.add_argument("-a", "--algorithm", help="Maze solving algotithm", type=str, 
                        choices=algorithms.keys(), required=True)
    group1 = parser.add_argument_group('Race mode', 'Starts the race proposed by noops api.')  
    group1.add_argument("-r", "--race", type=str, metavar="USERNAME",
                    help="Starts a race specifying a github username account as participant.")
    group2 = parser.add_argument_group('Test mode', 'Test mode over some random mazes')
    group2.add_argument("-n", "--numMazes", metavar='NUMBER', type=int, help="Number of random mazes to test.")
    possible_values = [10, 20, 30, 40, 60, 100, 120, 150, 200]
    group2.add_argument("-m", "--minSize",  type=int, choices=possible_values, 
                      default=10, help="Minimum maze size.")
    group2.add_argument("-M", "--maxSize",  type=int, choices=possible_values, 
                      default=200, help="Maximum maze size.")
    try:
        args = parser.parse_args()
    except:
        print("-h/--help for more information.")
        sys.exit(1)
    else:
        if args.race and args.numMazes:
            parser.print_usage()
            raise MazeSolverArgumentsException("Race mode is mutual exclusive with Test mode.\n-h/--help for more information.")
        if args.minSize > args.maxSize:
            parser.print_usage()
            raise MazeSolverArgumentsException("Minimum size cannot be greater than maximum size.\n-h/--help for more information.")
        return args        

def main():
    try:
        args = parse_args()
    except MazeSolverArgumentsException as ve:
        print("ERROR:", ve)
    else:
        algorithm = algorithms[args.algorithm]
        if args.race is not None:
            login = args.race
            race(algorithm, login)
        else:
            nMazes = args.numMazes
            minSize = args.minSize
            maxSize = args.maxSize

            for i, maze in enumerate(mazes(nMazes, minSize, maxSize)):
                data = is_correct(algorithm(maze, euclidean), maze['mazePath'])
                print("Maze number {:02}".format(i+1))
                print("\tResult:", data['result'])
                print("\tMessage:", data['message'])
                print("\tThe best solution has {} steps. Your solution has {}"
                        .format(data['shortestSolutionLength'], data['yourSolutionLength']))
        

if __name__=="__main__":
    main()

    