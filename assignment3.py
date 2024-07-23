# 1. Nested Decisions: The Adventure Game
#Objective: To practice the use of nested if statements.

# Task 1: 
# Code Correction 
# You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. 
# Identify and fix them.
# Buggy Code:

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# Task 2: Setting the Scene
# Based on your corrected code from Task 1, 
# expand the game. If the user chooses "cave", 
# ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
    action = input("return home and keep it safe! or explore further to seek more treasure ")
    if action == "return home and keep it safe!":
        print("light a tourch")
    elif action == "exploore further to seek more treasure":
        print("proceed in the dark")                

# Task 3: Default Path
# If the user makes an invalid choice at any point, 
# incorporate a pass statement to handle it. HINT: 
# How can an else statement be of use here?


value = 12
if value > 5:
  pass

else:
  print("Invalid")


# 2. Quick Decisions: The Event Planner
# Objective: To practice the use of shorthand if statements.
# Task 1: Code Correction 
# You are provided with a Python script that is supposed to help in event planning, 
# but it has errors. Identify and fix them.
# Buggy Code:
# 

attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Fixed code
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue Selection

# Based on the corrected code from Task 1, 
# further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

attendees = int(input("Enter number of attendees: "))
venue = "large hall and audio system" if attendees > 100 else "conference room and projector"
print(venue)

# Task 3: Catering Choices
# Ask the user 
# if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

food_choice = input("Interested in vegetarian food? yes/no?: ")
veggie_meal = input("We do have Veggie Delight Caterers, interested? yes/no: ")

if food_choice == "yes": 
  if veggie_meal == "yes":
    print("I highly recommend Gourmet Meals Caterers!")
  elif veggie_meal == "no":
    print("We got other options!")

else:
    if food_choice == "no":
      print("We got meat options too!")

#I got stuck in the last coding task, so please write it out so I can see where I made the error. Thanks.