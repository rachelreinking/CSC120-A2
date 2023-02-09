"""
   Filename: computer.py
Description: The computer class file as a part of A2: Object-ification, CSC120: Object-Oriented Programming
             in order to run a computer resale shop using object-oriented programming
     Author: Rachel Reinking
       Date: 8 February 2023
    
"""

class Computer:

    # What attributes will it need?
    """
    description: a string representing the name of the computer
    processor_type: a string representing the type of processor of the computer
    hard_drive_capacity: an integer representing the hard drive capacity of the computer
    memory: an integer representing the memory of the computer
    operating_system: a string representing the operating system of the computer
    year_made: an integer representing the year the computer was made
    price: an integer representing the price of the computer
    """
    description: str 
    processor_type: str 
    hard_drive_capacity: int 
    memory: int 
    operating_system: str 
    year_made: int 
    price: int 


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self: str,
                 description: str,
                 processor_type: str,
                 hard_drive_capacity: int,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        #pass # You'll remove this when you fill out your constructor

    # What methods will you need?

    """
    Takes in the new price of a commputer and updates the price of the computer
    """
    def update_price_computer(self, new_price):
        self.price = new_price

    """
    Takes in the operating system of a commputer and updates the operating system of the computer
    """
    def update_os_computer(self, new_os):
        self.operating_system = new_os

    """
    Takes in a computer and refurbishes the computer and updates the price of the computer based on the year made
    """
    def refurbish_computer(self):
        if self.year_made < 2000:
            self.price = 0 # too old to sell, donation only
        elif self.year_made < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif self.year_made < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff

    """
    Takes in a computer and prints all of the information about the computer in a line, separated by commas, 
    and ends with two new lines
    """
    def printdetails(self):
        print(self.description, 
              self.processor_type, 
              self.hard_drive_capacity, 
              self.memory, self.operating_system,
              self.year_made,
              self.price,
              sep=", ",
              end="\n \n")

