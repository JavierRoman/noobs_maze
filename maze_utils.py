# Author: Javier Roman

import math



def euclidean(node, goal):
    """
    Euclidean squared distance.
    
    Args:
        node (tuple): Current position.
        goal (tuple): Goal location.
    
    Returns:
        float: Float value with the squared distance between the two points.
    """
    distance = 0
    for n, g in zip(node, goal):
        distance+=(n-g)**2

    return distance

def neighbours(current, maze_map):
    """
    This function retrieves all the possible moves from the current cell.
    
    Args:
        current (tuple): 2D possition in the maze.
        maze_map (list): List of lists with the representation of the maze. 
                         ["X": represents a wall, " ": represents an empty cell, 
                         "A": represents the starting point, "B": represents the ending point]
    Returns:
        tuple: Cell neighbour location.
    """
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for dr, dc in directions:
        nr, nc  = current[0]+dr, current[1]+dc
        if nr < 0 or nc < 0:
            continue
        try:
            if maze_map[nr][nc] != 'X':
                yield (nr, nc)
        except IndexError:
            continue

def direction(nodeA, nodeB):
    """
    This function retrieves the direction followed to get from one node to another.
    
    Args:
        nodeA (tuple): Initial node.
        nodeB (tuple): Final node.
    
    Returns:
        str: An string with the directions to follow to reach the goal 
             ["N": North, "S": South, "E": East, "W": West]
    """
    dirs = {(0, -1): "W", (0, 1): "E", (1, 0): "S", (-1, 0): "N"}
    aR, aC = nodeA
    bR, bC = nodeB

    return dirs[(bR-aR, bC-aC)]

def path(previous_nodes, current):
    """
    This function reconstruct the path retrieving the set of directions needed to
    go from the starting point to the end point.
    
    Args:
        previous_nodes (dict): Dictionary with the previous node explored for each node.
        current (tuple): 2D current position.
    
    Returns:
        str: String with the directions needed to follow to reach the destination.
    """
    best_path = []
    while current in previous_nodes:
        prev = previous_nodes[current]
        best_path = [direction(prev, current)] + best_path
        current = prev
    return ''.join(best_path)

def best_estimation(explored_nodes, estimations):
    """
    This function retreives the best option from the set of explored options.
    
    Args:
        explored_nodes (list): List of explored nodes.
        estimations (dict): Dictionary with the estimations calculated with the
                            formula: f = g + h where g is the distance from the 
                            beggining to that node and h the heuristic from that 
                            node to the goal.
    
    Returns:
        tuple: 2D location of the best node.
    """
    best_est = math.inf
    best_node = None

    for node in explored_nodes:
        estimation = estimations[node]
        if best_est > estimation:
            best_node = node
            best_est = estimation
    return best_node

