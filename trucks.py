# Larah Chesnic Student ID: 001106662
import datetime
from package import Package
from hashmap import HashMap


class Truck:
    truck_object_list = []
    package_status_hashmap = HashMap()

    def __init__(self, truck_id, start_time):
        self.truck_id = truck_id
        self.start_time = start_time
        self.mileage = 0.0
        self.truck_address_list = []
        self.truck_bed = []
        self.address_vertex = []

    # look through each Package object, and each package in Truck bed. If the package is in the truck, add the
    # package's address number, but not if it's already been added
    # Big O is O(n^2)
    def get_hub_vertices(self):
        for p in Package.package_object_list:
            for x in self.truck_bed:
                if p.package_id == x:
                    if p.address_hub_number not in self.address_vertex:
                        self.address_vertex.append(p.address_hub_number)

    # The algorithm searches a list which contains only the address hubs needed to be visited, depending on which
    # packages are in the truck bed. It does not contain any duplicates if one or more packages are being delivered
    # to the same location. This is an efficient algorithm because each list is trimmed from the start to only
    # contain data that is needed. Furthermore, this list continues to shrink as each address visited is removed with
    # each iteration.

    # Big O is O(n^3)
    def deliver(self, start_vertex, distance_list, start_time):
        while len(self.address_vertex) > 0:
            distance = []
            # adds distances from the start vertex to every other vertex that must be visited to a list
            for x in self.address_vertex:
                distance.append(distance_list[start_vertex][x])
            # declares smallest index to be the first one
            smallest_index_in_hub_list = 0
            # checks every other one to find the shortest distance from the start
            for i in range(1, len(distance)):
                if distance[i] < distance[smallest_index_in_hub_list]:
                    smallest_index_in_hub_list = i
            # uses calculated vertex to find the distance in the distance matrix
            self.mileage += round(distance_list[start_vertex][self.address_vertex[smallest_index_in_hub_list]], 1)
            # calculates how many minutes from the start time the truck drove to deliver package
            minutes = round((self.mileage / 18.0) * 60.0, 1)
            delta_time_to_add = datetime.timedelta(minutes=minutes)
            deliver_time = start_time + delta_time_to_add
            # for packages, if they are in the truck bed and their address hub matches the address hub the truck is
            # deliver to, remove the package from the truck bed and update hashmap's delivery status w/package id as key
            for p in Package.package_object_list:
                if p.package_id in self.truck_bed:
                    if p.address_hub_number == self.address_vertex[smallest_index_in_hub_list]:
                        self.truck_bed.remove(p.package_id)
                        self.package_status_hashmap.add(p.package_id, deliver_time)
            distance.clear()
            # the new start vertex is the most recently visited address hub
            start_vertex = self.address_vertex[smallest_index_in_hub_list]
            del self.address_vertex[smallest_index_in_hub_list]

    # adds a start time to each package so that in user interface, the user entered time can be compared
    # to the time that the package leaves the station
    # Big O is O(n)
    def add_package_start_time(self, package):
        if isinstance(package, Package):
            for x in self.truck_bed:
                if package.package_id == x:
                    package.start_time = self.start_time
