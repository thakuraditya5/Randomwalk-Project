from turtle import  Screen
import turtle as t
import random

# Initialize turtle and colors
timmy = t.Turtle()
t.colormode(255)
def random_color():
    r= random.randint(0,255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r,b,g)
    return random_color

timmy.shape("turtle")
timmy.pensize(5)
timmy.speed(10)

# Directions list
directions = [0,90,180,270]  # Right and left turn angles
n = 1

# Loop to draw
while n <= 200:  # Change condition to loop for 20 times
    timmy.color(random_color())  # Set a random color
    timmy.setheading(random.choice(directions))  # Set a random direction
    timmy.forward(30)  # Move forward
    n += 1  # Increment the counter

screen = Screen()
screen.exitonclick()
