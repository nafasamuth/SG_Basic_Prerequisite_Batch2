import time

class Meteor:
    def __init__(self, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z) -> None:
        super().__init__()
        self.position = {
            'x': pos_x,
            'y': pos_y,
            'z': pos_z
        }
        self.velocity = {
            'x': vel_x,
            'y': vel_y,
            'z': vel_z,
        }

    def change_position(self, time=0.001):
        """
        update position of meteor over time
        :param time: point of time
        :type time: float
        """
        # REPLACE YOUR CODE HERE


def euclidean_distance(meteor_a, meteor_b):
    """
    calculate euclidean distance of two meteor
    :param meteor_a: meteor a
    :param meteor_b: meteor b
    :type meteor_a: Meteor
    :type meteor_b: Meteor
    :return: float
    """
    from math import pow, sqrt
    return sqrt(
        pow(meteor_a.position['x'] - meteor_b.position['x'], 2)
        + pow(meteor_a.position['y'] - meteor_b.position['y'], 2)
        + pow(meteor_a.position['z'] - meteor_b.position['z'], 2)
    )


def circuit_exists(T, u, x, y):
    t = len(T)
    if x not in T:
        t += 1
    if y not in T:
        t += 1
    if t - 2 == u:
        return False
    return True


def generate_tree(G):
    """
    generate minimum spanning tree from graph G
    :param G: weighted graph of meteors
    :type G: dict of dict of float
    :return: dict of dict of float
    """
    n = len(G)
    T = {}

    # REPLACE YOUR CODE HERE

    return T


def tree_is_equal(tree_1, tree_2):
    """
    check whether given trees is equal
    :param tree_1: minimmum spanning tree 1
    :param tree_2: minimmum spanning tree 2
    :type tree_1: dict of dict of float
    :type tree_2: dict of dict of float
    :return: bool
    """
    if tree_1.keys() != tree_2.keys():
        return False

    for k in tree_1:
        if tree_1[k].keys() != tree_2[k].keys():
            return False

    return True


try:
    OBSERVATION_TIME = 1
    CHANGE_TIME = 0.01

    test_case = 1
    while True:
        # number of meteor
        n = int(input())

        # init list of meteor
        list_of_meteor = [Meteor for x in range(n)]

        # for each meteor, fill to corresponding field
        for i in range(n):
            # parse input
            x, y, z, vx, vy, vz = map(int, input().split(' '))

            # save parsed input to object meteor
            meteor = Meteor(
                pos_x=x,
                pos_y=y,
                pos_z=z,
                vel_x=vx,
                vel_y=vy,
                vel_z=vz,
            )

            # append object object meteor to list_of_meteor
            list_of_meteor[i] = meteor

        counter = 0         # number of changes
        previous_tree = {}  # variable to store previous tree
        current_tree = {}   # variable to store current tree
        meteor_graph = {}   # variable to store weighted graph,
                            # weight represents euclidean between to meteor
        iteration = 0       # variable to store iteration counter
        start = time.time() # variable to store initial time

        # simulate asteroid movement
        while True:
            # make meteor moving
            if iteration > 0:
                for i in range(len(list_of_meteor)):
                    list_of_meteor[i].change_position(time=CHANGE_TIME)

            # represent meteor in a weighted graph
            for i in range(n):
                meteor_graph[i] = {}
                for j in range(n):
                    if i is not j:
                        # represent the euclidean distance between meteor i
                        # and meteor j is ed
                        meteor_graph[i][j] = euclidean_distance(
                            list_of_meteor[i],
                            list_of_meteor[j]
                        )

            # generate minimum spanning tree
            current_tree = generate_tree(meteor_graph)

            # verify whether current tree match to previous tree
            # REPLACE YOUR CODE HERE

            iteration += 1

            # limit the observation time
            if time.time() - start > OBSERVATION_TIME:
                break

        # print result
        print("Case %d: %d" % (test_case, counter))

        test_case += 1
except EOFError:
    pass
