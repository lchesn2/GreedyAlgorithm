# Larah Chesnic Student ID: 001106662
import datetime
import data
from package import Package
from trucks import Truck
from numpy import *

current_date = datetime.datetime.now().date()
year = current_date.year
month = current_date.month
day = current_date.day

# add each truck object's total mileage
# big O is O(n)
def total_truck_mileage():
    total = 0.0
    for t in Truck.truck_object_list:
        total += round(t.mileage, 1)
    return total


# Big O O(n)
def check(value, hour, minute):
    # uses user input to create a user datetime
    user_date_time = datetime.datetime(year, month, day, hour, minute, 0)
    # find the package id to locate the start time
    # if the user date time is before the start time then the package hasn't left yet
    # if it is before the delivery time, then it's en route
    # otherwise it's delivered
    # printing out all package information or delivery times is constant time by using the hashmaps
    for p in Package.package_object_list:
        if p.package_id == value:
            if user_date_time < p.start_time:
                print('package', value, data.package_hashmap.get(value), 'STATUS: At Hub.')

            elif user_date_time < Truck.package_status_hashmap.get(value):
                print('package', value, data.package_hashmap.get(value), 'STATUS: En Route.')

            else:
                print('package', value, data.package_hashmap.get(value), 'STATUS: Delivered',
                      Truck.package_status_hashmap.get(value))


# Big O is O(n) because the check function is called
# uses booleans to continue prompting user or to move to next prompt
# user has options to check all packages or just by a specific package
# user can exit system or check total miles driven
def user():
    # finds the range of valid package numbers for user to search for
    start = Package.package_object_list[0].package_id
    end = len(Package.package_object_list)
    first_loop = True
    print('Welcome to WGUPS')
    while first_loop:
        # catches invalid entries such as no value or string
        try:
            print("To Exit the system, enter '-1'. ")
            print("To view total miles driven by trucks, enter '-2'.")
            hour_ = int(input("To begin tracking packages, enter an hour in hh format. To specify AM or PM, "
                              "please use military time: "))
            if hour_ == -1:
                first_loop = False
            elif hour_ == -2:
                print(round(total_truck_mileage(), 1), 'total miles driven.')
            # makes sure package is a valid package to search for
            elif hour_ <= 0 or hour_ >= 24:
                print("Sorry, that is not a valid hour.")
            else:
                sec_loop_minute = True
                while sec_loop_minute:
                    # asks user to enter hour and minute which will become parameters to the check function
                    try:
                        minute = int(input("Please enter a minute in mm format: "))
                        if minute < 0 or minute > 59:
                            print("Sorry, that is not a valid minute.")

                        else:
                            third_loop_package = True
                            while third_loop_package:
                                try:
                                    print("To view all packages at this time, enter '-3'")
                                    print("Valid package numbers:", start, '-', end)
                                    value = int(input("Enter a package number: "))
                                    if value == -3:
                                        for p in Package.package_object_list:
                                            check(p.package_id, hour_, minute)
                                            third_loop_package = False
                                            sec_loop_minute = False
                                    elif value < start or value > end:
                                        print("Sorry this is not a valid package number.")
                                    else:
                                        check(value, hour_, minute)
                                        third_loop_package = False
                                        sec_loop_minute = False

                                except:
                                    (ValueError)
                    except:
                        (ValueError)
        except:
            (ValueError)

    exit(-1)
