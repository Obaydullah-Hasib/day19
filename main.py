from turtle import Turtle, Screen
import random

new_turtle = Turtle()
screen = Screen()

# def move_forwards():
#     turlte.forward(10)
# def move_backwards():
#     turlte.backward(10)
# def move_right_angle():
#     turlte.left(10)
# def move_left_angle():
#     turlte.right(10)
# def reset():
#     turlte.reset()
# screen.listen()
# screen.onkeypress(key="w", fun=move_forwards )
# screen.onkeypress(key="s", fun=move_backwards )
# screen.onkeypress(key="a", fun=move_right_angle )
# screen.onkeypress(key="d", fun=move_left_angle )
# screen.onkeypress(key="c", fun=reset )
screen.setup(height=.75,width=.750)
screen_widht = screen.window_width()
screen_height= screen.window_height()
print(screen_widht)
is_race_on = False
all_turtles=[]
colors=['red','orange','yellow','green','blue','purple']
y_positions=[-250,-150,-50,50,150,250]
for index, color  in enumerate(colors):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-(screen_widht/2)+20, y=y_positions[index])
    all_turtles.append(new_turtle)
user_bet = screen.textinput(title="Make you Bet!!!", prompt="Which turtle will win? Enter a color: ").lower()
if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= (screen_widht/2)-30:
            is_race_on=False
            wining_color = turtle.pencolor()
            if user_bet == wining_color:
                print(f"You've won! The {wining_color} turtle is the winner!")
            else:
                print(f"You lost! The {wining_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()