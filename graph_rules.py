import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp
import pandas as pd

def distance_mat(init_mat):
    # returns shortest distances between any two nodes
    # this is a little clumsy and networkx has this functionality: nx.shortest_path_length(G)

    nodes = len(init_mat)

    dist_mat = np.zeros((nodes, nodes))
    paths = np.copy(init_mat)

    for power in range(1, nodes):

        for i in range(nodes):
            for j in range(nodes):
                if dist_mat[i][j] == 0 and paths[i][j]:
                    dist_mat[i][j] = power

        paths = np.dot(paths, init_mat)

    for i in range(nodes):
        dist_mat[i][i] = 0

    return dist_mat

def walks_ensemble(start, trials, connect_mat):
    # returns a list of the exit stations of an ensemble of walkers, all at the same starting point.

    exits = []

    for i in range(trials):

        next_loc = start


        while next_loc != 'exit':

            location = int(next_loc)
            paths = np.append(np.nonzero(connect_mat[location])[0], 'exit')

            next_loc = np.random.choice(paths)

        exits.append(location)

    return exits

def track_ensemble(start, trials, connect_mat):
    # returns a list of the exit stations of an ensemble of walkers, all at the same starting point.

    visited = []

    for i in range(trials):

        next_loc = start
        track = []


        while next_loc != 'exit':

            location = int(next_loc)
            paths = np.append(np.nonzero(connect_mat[location])[0], 'exit')

            next_loc = np.random.choice(paths)

            track.append(location)

        visited.append(track)

    return visited

def weighted_track_ensemble(start, trials, weighted_connect_mat):
    # returns a list of the exit stations of an ensemble of walkers, all at the same starting point.

    visited = []

    for i in range(trials):

        next_loc = start
        track = []

        while next_loc != 'exit':

            location = int(next_loc)

            adjacent_stats = [[index]*int(weighted_connect_mat[location][index]) for index in np.nonzero(weighted_connect_mat[location])[0]]

            paths = np.append([item for sublist in adjacent_stats for item in sublist], 'exit')

            next_loc = np.random.choice(paths)

            track.append(location)

        visited.append(track)

    return visited

def return_route(start, trials, connect_mat):
    # returns a list of the exit stations of an ensemble of walkers, all at the same starting point.

    visited = []

    for i in range(trials):

        next_loc = start
        track = []

        track.append(next_loc)

        #so that it is never equal to the start location

        paths = (np.nonzero(connect_mat[start])[0])


        next_loc = np.random.choice(paths)

        while next_loc != start:

            location = int(next_loc)
            paths = (np.nonzero(connect_mat[location])[0])

            next_loc = np.random.choice(paths)
            track.append(location)

        track.append(next_loc)

        visited.append(track)

    return visited

def time_track_ensemble(start, trials, connect_mat, time):
    # returns a list of the exit stations of an ensemble of walkers, all at the same starting point.

    visited = []

    for i in range(trials):

        next_loc = start
        track = []


        for t in range(time):

            location = int(next_loc)

            next_loc = np.random.choice(np.nonzero(connect_mat[location])[0])

            track.append(location)

        visited.append(track)

    return visited


class Line:

    def __init__(self, line_pairs, dist_mat):

        self.dist_mat = dist_mat
        self.line_pairs = line_pairs


        line_list = list(line_pairs['station1'])

        line_list.extend(list(line_pairs['station2']))
        self.line_list = line_list #note this is from 0 to 303, therefore need to -1 for dist_mat indices

        self.dists_to_line = [min([self.dist_mat[i-1, j] for i in self.line_list]) for j in range(len(dist_mat))]


    def dist_to_node(self, node): #ensure that node is the '-1' version
        return self.dists_to_line[node]
