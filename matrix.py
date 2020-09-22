# Larah Chesnic Student ID: 001106662
class Vertex:
    # creates object list which is used to determine the size of the nested list,
    # this feature helps this software adjust to larger tables of distances being added
    vertex_object_list = []

    def __init__(self, label, address):
        self.label = label
        self.address = address


# creates nested list as a matrix for the csv distance data
class Matrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0 for column in range(vertices)]
                       for row in range(vertices)]

    # because each edge is undirected the weight is added bidirectionally
    def add_edge(self, hub_a, hub_b, weight):
        self.matrix[hub_a][hub_b] = weight
        self.matrix[hub_b][hub_a] = weight

    # ability to remove edges
    def remove_edge(self, hub_a, hub_b):
        self.matrix[hub_a][hub_b] = None
        self.matrix[hub_b][hub_a] = None
