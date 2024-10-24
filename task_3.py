# ამის ჩემით დაწერის შანსი არ იყო, მაგრამ მაინტერესებდა როგორ გამოიყურებოდა, ამიტომ მოვიძიე

import turtle
from random import uniform
import math

def setup_screen(size):
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Monte Carlo Pi Approximation")
    screen.setworldcoordinates(-0.1, -0.1, 1.1, 1.1)  # Set coordinate system
    screen.tracer(0)  # Turn off animation for speed
    return screen

def draw_axes():
    # Create turtle for drawing axes
    axes = turtle.Turtle()
    axes.hideturtle()
    axes.pensize(2)
    
    # Draw x-axis
    axes.penup()
    axes.goto(0, 0)
    axes.pendown()
    axes.goto(1, 0)
    
    # Draw y-axis
    axes.penup()
    axes.goto(0, 0)
    axes.pendown()
    axes.goto(0, 1)

def draw_quarter_circle():
    # Create turtle for drawing quarter circle
    circle = turtle.Turtle()
    circle.hideturtle()
    circle.pensize(2)
    
    # Draw quarter circle
    circle.penup()
    circle.goto(0, 0)
    circle.pendown()
    
    # Draw arc
    for angle in range(91):  # 0 to 90 degrees
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        circle.goto(x, y)

def plot_point(x, y, inside):
    # Create point turtle
    point = turtle.Turtle()
    point.hideturtle()
    point.penup()
    point.speed(0)
    
    # Set color based on whether point is inside circle
    point.color('red' if inside else 'green')
    
    # Draw point
    point.goto(x, y)
    point.dot(3)

def monte_carlo_pi():
    # Get number of points from user
    number = int(turtle.textinput("Input", "Please enter a natural number larger than 1: "))
    
    # Setup visualization
    screen = setup_screen(number)
    draw_axes()
    draw_quarter_circle()
    1
    hits = 0
    # Generate and plot points
    for _ in range(number):
        x = uniform(0, 1)
        y = uniform(0, 1)
        inside = (x * x + y * y) <= 1
        
        if inside:
            hits += 1
        
        plot_point(x, y, inside)
        
        # Update every 100 points
        if _ % 100 == 0:
            screen.update()
    
    # Final update
    screen.update()
    
    # Calculate and display pi approximation
    pi_approximation = 4 * hits / number
    print(f"Approximation of π: {pi_approximation}")
    
    # Keep window open
    screen.exitonclick()

# Run the simulation
monte_carlo_pi()