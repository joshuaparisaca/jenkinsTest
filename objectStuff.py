import datetime
import math

human1_name = "Joshua"
human1_age = 24
human1_height = 66

human2_name = "Alex"
human2_age = 25
human2_height = 68

def print_human_info(name, age, height):
    print(name, age, height)

class Human(object): #This creates an object with values passed into this class
    def __init__(self, name, age, height):
        self.age = age #You need these attibutes to create an object
        self.name = name
        self.height = height

    def print_stats(self): #This prints out the attributes of the values passed to the class/object 
        print("The human's name is " + self.name + " and their height is " +
                str(self.height) + " and they are " + str(self.age) + " years old.")

human1 = Human(human1_name, human1_age, human1_height) #Creates an object based on variable values
human2 = Human(human2_name, human2_age, human2_height)

human1.print_stats() #Prints out the stats based on the variable values the object has
human2.print_stats()

#human_list = []
#for row in rows:
#   human_list.append(Human(row.name, row.age, row.height))
    #Use this type of syntax to read from a file and input the values of a object into the "human" object and into a list 