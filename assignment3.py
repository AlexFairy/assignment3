"""
# Task 1: 
# Code Correction 

place = input("Choose a place: forest or cave? ").lower()

if place == "forest":
    action = input("climb a tree or cross a river? ").lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
else:
    print("Make a proper selection!")


# Task 2: Setting the Scene

place = input("Choose a place: forest or cave? ").lower()

if place == "forest":
  action = input("climb a tree or cross a river? ").lower()
  if action == "climb a tree":
      print("You found a bird's nest!")
  elif action == "cross a river":
      print("You found a boat!")
  else:
      print("Incorrect selection. Try again!")
elif place == "cave":
  print("You find a hidden treasure!")
  print("Please either select 1 or 2.")
  action = input("1. return home and keep it safe! or 2. explore further to seek more treasure: ").lower()
  if action == "1":
        print("light a tourch")
  elif action == "2":
        print("proceed in the dark")
  else:
      print("Incorrect selection. Try again!")                

# Task 3: Default Path
# If the user makes an invalid choice at any point, 
# incorporate a pass statement to handle it. HINT: 
# How can an else statement be of use here?


value = int(input("Type a number: "))
if value > 5:
  print(f"The input number is bigger than 5! Good job!")
elif value < 5:
  print("The input number is smaller than 5! Good job!")
else:
  pass
  print(f"Incorrect")

  
# Task 1: Code Correction 

# Buggy Code:

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
"""
# Task 3: Catering Choices
# Ask the user 
# if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers")

user_input = input("Interest in vegetarian cuisine?(yes/no) ").lower()

if user_input == 'yes':
  print("I highly reccomend Veggie Delight Caterers")
  user_input = input("Interested?(yes/no) ").lower()
  if user_input  == 'yes':
    print("We'll get started on your order!")
  elif user_input == 'no':
    print("Then I can reccomend Gourtmet Meals Caterers")
  else:
    print("Incorrect entry!")
else:
  print("We do have other options such as meat and fish")