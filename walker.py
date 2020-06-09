import numpy as np

"""

Matthew Cotton

"""

def get_depths(d):

    depths = [0]

    if d:
        for i in range(1, d+1):

            depths.extend(([i]*(3*(2**(i-1)))))

    return depths

def bethe_adj_mat(d, z):

    nodes = int(3*(2**d) - 2)

    connect_mat = np.zeros((nodes, nodes))

    if d:

        connect_mat[1, 0] = 1
        connect_mat[0, 1] = 1

        for i in range(0, int(nodes/2)-1):
            for j in range(1, z):
                connect_mat[2*i+1+j][i] = 1
                connect_mat[i][2*i+1+j] = 1

    return connect_mat

class Lost_Walker:
    """
    Basic walker.

    Keeps track of its location

    """

    def __init__(self, start_node, connect_mat):
        """

        Random Walker on the network.

        """
        self.__node = start_node
        self.__connect_mat = connect_mat
        #self.__con_mat = np.array(con_mat)
        self.__last_loc = None

    def change_node(self, new_node):
        self.__node = new_node
        return self.__node

    def get_node(self):
        return self.__node

    def step(self):
        self.__last_loc = None
        move_to = np.random.choice(adj_locs())

        if move_to == 'exit':
            self.__last_loc = get_node()

        change_node(move_to)

        return move_to


    def adj_locs(self):
        if self.__node == 'exit':
            return ['exit']
        else:
            return np.append(np.nonzero(connect_mat[self.__node])[0], 'exit')

    def get_last(self):
        return self.__last_loc

    def walk(self):

        time = 0

        while not self.get_last() == None:
            self.step()
            times += 1

        return (self.__last_loc, times)

class Network:

    def __init__(self, con_mat, time_limit, exit=True):
        """

        Network for the walk to take place.

        """
        self.__con_mat = np.array(con_mat)

    def get_connections(self, node):
        possible_destinations = np.nonzero(con_mat[0])[0]

        if self.__exit:
            possible_destinations = np.append(possible_destinations, 'exit')

        return np.random.choice(possible_destinations)
