# Larah Chesnic Student ID: 001106662
import datetime


class Package:
    package_object_list = []
    # creates package objects
    def __init__(self, package_id, address, city, zip_code, delivery_time, mass, note, address_hub_number):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.delivery_time = delivery_time
        self.mass = mass
        self.note = note
        self.address_hub_number = address_hub_number
        self.start_time = datetime


