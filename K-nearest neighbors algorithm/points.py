"""Description of class "Points" for realization k-neares neighbors algorithm.

This class is for generating, storing, and modifying points (multiple objects).

"""
import matplotlib.pyplot as plt

class Points:

    def __init__(self, number_of_sets = 2):
        if (number_of_sets >= 2) and (number_of_sets <= 10):
            self.number_of_sets = number_of_sets
        else:
            self.number_of_sets = 2
        self._color_part = 1/number_of_sets

        itr = iter(range(number_of_sets))

        # make list of point colors
        self._colors = list(map(lambda x: x + self._color_part * next(itr)
                               , list(number_of_sets * [0])))

        # make lists(sets points) in list 'points'
        self.points = [[list() for i in range(2)] for i in range(number_of_sets)]

    def add_one_point(self, set_id, point):

        """Adding one point to the set number 'set_id'"""

        if (set_id < 0) or (set_id > self.number_of_sets):
            set_id = 0
        if (type(point) == 'tuple') and (len(point) == 2):
            self.points[set_id][0].append(point[0])
            self.points[set_id][1].append(point[1])
        else:
            print("Incorrect point.")
    def add_points(self, set_id, array_x, array_y):

        """Adding lists of points 'array_x' and 'array_y' in a set number 'set_id'"""

        if (len(array_x) < len(array_y)):
            array_y = array_y[:(len(array_y)-len(array_x))]
        elif (len(array_x) > len(array_y)):
            array_x = array_x[:(len(array_x)-len(array_y))]
        if (len(self.points[set_id][0]) == 0):
            self.points[set_id][0] = array_x[:]
            self.points[set_id][1] = array_y[:]
        else:
            for i in range(len(array_x)):
                self.points[set_id][0].append(array_x[i])
                self.points[set_id][1].append(array_y[i])
    def show_sets(self):

        for i in range(self.number_of_sets):
            plt.scatter(self.points[i][0], self.points[i][1], s=10, color=str(self._colors[i]))
        plt.show()