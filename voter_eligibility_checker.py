#Ask for a user's name and age
name_and_age = input("Enter your name and age separated by a space: ")

name, age = name_and_age.split(" ")

people = ()
people_attributes = (name, int(age),)
people = people + people_attributes


list_of_people = []

list_of_people.append(people)

class PersonNotFoundError(Exception):
    pass

def check_eligibility(name):
    for person in list_of_people:
        if name != person[0]:
            print("The name you entered could not be found")
        else:
            if person[1] >= 18:
                print(f"{name} is eligible to vote")
            else:
                print(f"{name} is not eligible to vote")
               
    

check_eligibility("Emmanuel")