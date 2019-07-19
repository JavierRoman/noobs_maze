# Author: Javier Roman

import requests
from maze_utils import euclidean

url = 'https://api.noopschallenge.com'

def mazes(num, minSize=10, maxSize=200):
    """
    This function generates mazes calling to the API.
    
    Args:
        num (int): Number of mazes to generate.
        minSize (int, optional): Minimum size of the maze. Defaults to 10.
        maxSize (int, optional): Maximum size of the maze. Defaults to 200.
    
    Returns:
        dict: Dictionary with information of the maze.
    """

    params = dict(minSize=minSize, maxSize=maxSize)
    return (requests.get(url=url+"/mazebot/random", params=params).json() for i in range(num))

def is_correct(directions, post_url):
    """
    This function checks if the proposed solution is correct
    
    Args:
        directions (str): Directions that the agent needs to follow to arrive to the destination.
                          This string uses the characters [N: North, S: South, E: East, W: West]
        post_url (str): Base url to post the solution.
    
    Returns:
        dict: Dictionary with the response of the API.
    """
    dir_json = {"directions": directions}
    return requests.post(url+post_url, json=dir_json).json()

def race(algorithm, login="javierroman"):
    """
    This function starts a race calling to the API.
    
    Args:
        login (str, optional): Github username of the player. Defaults to "javierroman".
    """
    data = requests.post(url=url+"/mazebot/race/start", json={"login": login}).json()
    print(data['message'], '\n')
    mazeCounter = 1
    while "nextMaze" in data:
        maze = requests.get(url=url+data["nextMaze"]).json()
        data = is_correct(algorithm(maze, euclidean), maze['mazePath'])
        if 'message' in data:
            print("Result:", data['result'])
            print("Message:", data['message'])
            print("Certificate:", url+data['certificate'])
        else:
            print("Maze number {:02}".format(mazeCounter))
            print("\tResult:", data['result'])
            print("\tElapsed:", data['elapsed'])
            print("\tThe best solution has {} steps. Your solution has {}"
                    .format(data['shortestSolutionLength'], data['yourSolutionLength']))
            mazeCounter+=1