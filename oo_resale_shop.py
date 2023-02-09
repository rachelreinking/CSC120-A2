"""
   Filename: oo_resale_shop.py
Description: The resale shop class file as a part of A2: Object-ification, CSC120: Object-Oriented Programming
             in order to run a computer resale shop using object-oriented programming
     Author: Rachel Reinking
       Date: 8 February 2023
    
"""

from computer import *

class ResaleShop:

    # What attributes will it need?
    """
    inventory: a list where we will store the items in the computer resale store. The index indicates the item number
    """
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
        #pass # You'll remove this when you fill out your constructor

    # What methods will you need?

    """
    Takes in description, processor type, hard drive capacity, memory, operating system, year made, and price,
    which is all the information about a new computer, adds it to the inventory list, and returns the assigned
    item number
    """
    def buy(self, 
            description,
            processor_type,
            hard_drive_capacity,
            memory,
            operating_system,
            year_made,
            price):
        computer = Computer(description, 
                            processor_type, 
                            hard_drive_capacity, 
                            memory, 
                            operating_system, 
                            year_made, 
                            price)
        self.inventory.append(computer)
        return self.inventory.index(computer)

    """
    Takes in an item number, removes the associated computer if it is the inventory, prints error message otherwise
    """
    def sell(self, index):
        self.inventory.pop(index)

    """
    Takes in an item number and returns whether or not that item is in the inventory
    """
    def inInventory(self, index) -> bool:
        if index in range(len(self.inventory)):
            return True
        else:
            return False

    """
    Takes in an item number and a new price, updates the price of the associated computer in the inventory
    if it is the inventory, prints error message otherwise
    """
    def update_price_inventory(self, index, new_price):
        if self.inInventory(index):
            Computer.update_price_computer(self.inventory[index], new_price)
        else:
            print("Item", index, "not found. Cannot update price.")

    """
    Takes in an item number and a new operating system, updates the operating system of the associated computer 
    in the inventory if it is the inventory, prints error message otherwise
    """
    def update_os_inventory(self, index, new_os):
        if self.inInventory(index):
            Computer.update_os_computer(self.inventory[index], new_os)
        else:
            print("Item", index, "not found. Cannot update operating system")

    """
    Takes in an item number and updates the price of the refurbished computer in the inventory if it is in the 
    inventory, prints error message otherwise
    """
    def refurbish_inventory(self, index):
        if self.inInventory(index):
            Computer.refurbish_computer(self.inventory[index])
        else:
            print("Item", index, "not found. Cannot refurbish item")

    """
    Prints all items in the dictionary as long as it is not empty, and prints an error message if it is empty
    """    
    def print_inventory(self):
        if (self.inventory):
            for i in self.inventory:
                Computer.printdetails(i)
        else:
            print("No inventory to display")
