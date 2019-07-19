# Author: Javier Roman

from maze_utils import *

def a_star(maze, heuristic):
    """
    A star search algorithm.
    
    Args:
        maze (list): List of lists with the representation of the maze. 
                     ["X": represents a wall, " ": represents an empty cell, 
                      "A": represents the starting point, "B": represents the ending point]

        heuristic (function): Heuristic from a node to the goal. Euclidian or Manhattan distance.
    
    Returns:
        str: An string with the directions to follow to reach the goal 
             ["N": North, "S": South, "E": East, "W": West]
    """
    start = maze["startingPosition"]
    start = (start[1], start[0])
    end = maze["endingPosition"]
    end = (end[1], end[0])
    maze_map = maze["map"]

    explored_nodes = [start]
    previous_nodes = {}

    g = {start: 0}
    f = {start: g[start] + heuristic(start, end)} 

    while len(explored_nodes) > 0:
        current = best_estimation(explored_nodes, f)
        if current == end:
            return path(previous_nodes, current)

        explored_nodes.remove(current)

        for neighbour in neighbours(current, maze_map):
            new_g = g[current]+1
            if not neighbour in g or new_g < g[neighbour]:
                previous_nodes[neighbour] = current
                g[neighbour]=new_g
                f[neighbour] = new_g + heuristic(neighbour, end)
                if neighbour not in explored_nodes:
                    explored_nodes.append(neighbour)
    return ""