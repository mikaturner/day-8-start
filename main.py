# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hi there!  I hope you are having a nice day")
  print("It's a chilly one isn't it?")
  print("I'm getting ready for nap.")

#Function that allows for input

def greet_with_name(name):
  print(f"Hi there {name} !  I hope you are having a nice day")
  print(f"It's a chilly one isn't it {name}?")
  print(f"I'm getting ready for nap {name}, I hope you get to take a break soon too!")

greet_with_name("Mika")

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What's the weather like in {location}?")

#greet_with("Jack Bauer", "Norway")

greet_with(location = "Switzerland", name = "Jenny")