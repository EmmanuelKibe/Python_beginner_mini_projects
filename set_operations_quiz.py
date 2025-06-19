#import random
import random

set1 = set(random.sample(range(1, 21), 5))
set2 = set(random.sample(range(1, 21), 5))

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")


def parse_input(user_input):
    return set(map(int, user_input.split(", ")))
    
    
#Ask the user to determine set operations
user_union = parse_input(input("What is the union of set 1 and set 2?: "))
user_intersection = parse_input(input("What is the intersection of set 1 and set 2?: "))
user_difference = parse_input(input("What is the difference between set 1 and set 2?: "))

correct_union = set1.union(set2)
correct_intersection = set1.intersection(set2)
correct_difference = set1.difference(set2)

score = 0

print("-- Result --")
if user_union == correct_union:
    print("Correct!")
    score += 1
else:
    print(f"Oops! The answer is {correct_union}")
    
if user_intersection == correct_intersection:
    print("Correct!")
    score += 1
else:
    print(f"Oops! The answer is {correct_intersection}")

if user_difference == correct_difference:
    print("Correct!")
    score += 1
else:
    print(f"Oops! The answer is {correct_difference}")
    
print(f"Your final score is: {score}")
