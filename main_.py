# Larah Chesnic Student ID: 001106662
import data
from package import Package
from trucks import Truck
from datetime import datetime
import datetime
import user_interface

def main():

    # create truck objects, add start time for each truck
    one_start = datetime.datetime(user_interface.year, user_interface.month, user_interface.day, 9, 5, 0, 0)
    two_start = datetime.datetime(user_interface.year, user_interface.month, user_interface.day, 8, 0, 0, 0)
    three_start = datetime.datetime(user_interface.year, user_interface.month, user_interface.day, 10, 20, 0, 0)
    truck_1 = Truck(1, one_start)
    truck_2 = Truck(2, two_start)
    truck_3 = Truck(3, three_start)

    # add truck objects to list
    Truck.truck_object_list.append(truck_1)
    Truck.truck_object_list.append(truck_2)
    Truck.truck_object_list.append(truck_3)

    # manually loaded truck beds
    truck_1.truck_bed = [1, 2, 6, 7, 11, 25, 26, 29, 30, 31, 32, 33]
    truck_2.truck_bed = [3, 5, 13, 14, 15, 16, 18, 19, 20, 21, 34, 36, 37, 38, 39, 40]
    truck_3.truck_bed = [4, 8, 9, 10, 12, 17, 22, 23, 24, 27, 28, 35]

    # for each package, add the address's hub number from a hashmap using the address as the key
    # fill each truck bed with respective packages
    # Big O is O(n)
    for p in Package.package_object_list:
        p.address_hub_number = data.vertices_hashmap.get(p.address)
        Truck.add_package_start_time(truck_1, p)
        Truck.add_package_start_time(truck_2, p)
        Truck.add_package_start_time(truck_3, p)

    # for each package id in truck bed find the address hub number and add it to a list in truck class
    # run deliver function, see truck module
    # big O is O(n^4) because deliver is O(n^3)
    for truck in Truck.truck_object_list:
        truck.get_hub_vertices()
        truck.deliver(0, data.distance_list, truck.start_time)

    # driver of truck 1 must return to hub to drive truck three
    truck_1.mileage += data.distance_list[11][0]

data.import_data()
main()
user_interface.user()
