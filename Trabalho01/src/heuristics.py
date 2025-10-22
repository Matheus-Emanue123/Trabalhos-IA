import numpy as np

def manhattan_distance(pos1, pos2):
  
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def euclidean_distance(pos1, pos2):
 
    return np.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)