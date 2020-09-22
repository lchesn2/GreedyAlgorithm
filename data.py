# Larah Chesnic Student ID: 001106662
import csv
from matrix import Vertex, Matrix
from hashmap import HashMap
from package import Package

vertices_hashmap = HashMap()
distance_list = []
package_hashmap = HashMap()

def import_data():
    # open csv file for each row in the package information using a comma as a delimiter, add each comma separated piece
    # to both the Hashmap and to a package object
    # Big O is O(n)
    with open('package.csv') as csvfile:
        package_details = csv.reader(csvfile, delimiter=',')
        for row in package_details:
            package_hashmap.add(int(row[0]),
                                {'Address': row[1], 'Deadline': row[5], 'City': row[2], 'Zip': row[4],
                                 'Mass': row[6]})
            package = Package(int(row[0]), row[1], row[2], row[4], row[5], int(row[6]), row[7], 0)
            package.package_object_list.append(package)
    # read csv data for addresses, using comma as delimiter. From each row add the address number which is used as a
    # label and the address as a vertex object. Add the address as a key and its respective address number,
    # it subtracts one from the address number so that it starts at zero
    # Big O is O(n)
    with open("hub_address_info.csv") as csvfile:
        mileage_details = csv.reader(csvfile, delimiter=',')
        for row in mileage_details:
            v = Vertex(int(row[1]) - 1, row[2])
            vertices_hashmap.add(str(row[2]), int(row[1]) - 1)
            Vertex.vertex_object_list.append(v)

    # converts entire row of string to float
    def convert_float(string):
        dist = float(string)
        return dist

    # read csv data to add distances to a nested matrix
    # Big O is O(n)
    with open("distance_data.csv") as file:
        mileage = csv.reader(file)
        for row in mileage:
            distance_rows = list(map(convert_float, list(row)))
            distance_list.append(distance_rows)

    # create Matrix specify number of vertices
    m = Matrix(len(Vertex.vertex_object_list))

    # add distance data to nested list
    # Big O is O(n^2)
    for i in range(0, len(Vertex.vertex_object_list)):
        for x in range(0, len(Vertex.vertex_object_list)):
            m.add_edge(i, x, distance_list[i][x])