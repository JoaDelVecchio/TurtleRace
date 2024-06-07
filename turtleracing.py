from turtle import Turtle, Screen
import random

# Position the turtles at their starting points
def initial_position(turtles, colors):
    y = 60
    for color in colors:
        new_turtle = Turtle("turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(-230, y)
        turtles.append(new_turtle)
        y -= 30

# Start the race and determine the winner
def start_race(turtles, bet):
    game_on = True
    while game_on:
        for turtle in turtles:
            if game_on:
                turtle.forward(random.randint(0, 10))
                if turtle.xcor() >= 230:
                    game_on = False
                    if turtle.pencolor() == bet:
                        print(f"The {turtle.pencolor()} turtle won, your guess was right!")
                    else:
                        print(f"The {turtle.pencolor()} turtle won, your guess was wrong!")

# Main function to run the game
def game():
    colors = ["orange", "yellow", "red", "green", "blue", "purple"]
    turtles = []
    screen = Screen()

    screen.setup(500, 400)
    bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:")

    initial_position(turtles, colors)
    start_race(turtles, bet)
    screen.exitonclick()

game()
