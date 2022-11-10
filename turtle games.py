#                                                               Turtle race game             
# from turtle import Turtle,Screen
# import random
# import turtle

# screen=Screen();
# screen.setup(500,400)
# colors=["red","orange","yellow","green","blue","purple"];
# user_bet=screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race? Enter the color :")
# y_pos=[-70,-40,-10,20,50,80];
# allturtle=[];
# for turtle_index in range(0,6):
#     tim=Turtle(shape="turtle");
#     tim.color(colors[turtle_index]);
#     tim.penup();

#     tim.goto(x=-230, y=y_pos[turtle_index]);
#     allturtle.append(tim);
# if user_bet:
#     is_race_on=True
# while is_race_on:
#     for turtle in allturtle:
#         if turtle.xcor()>230:
#             winning_color=turtle.pencolor();
#             is_race_on=False;
#             if winning_color==user_bet:
#                 print("You win")
#             else:
#                 print(f"You lost winning color is {winning_color}")
#         rand_dis=random.randint(0,10);
#         turtle.forward(rand_dis);

# screen.exitonclick()
        #############################################                 ------over---------          ###########################################################3
#snake game

from food import Food
import time
from scoreboard import Scoreboard;
from turtle import Turtle , Screen
# from xml.etree.ElementTree import TreeBuilder
from snake import Snake
screen=Screen();
screen.setup(600,600);
screen.bgcolor("black");
screen.title("My Snake Game");
screen.tracer(0);
# starting_pos=[(0,0),(-20,0),(-40,0)];
snake=Snake()
food=Food();
scoreboard=Scoreboard();

screen.listen();
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.update()
game_ison=True;
while game_ison:
    screen.update();
    time.sleep(0.1);
    snake.move();
    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh();
        snake.extend();
        scoreboard.increasescore();
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        # game_ison=False; 
        # scoreboard.game_over();
        scoreboard.reset()
        snake.reset();

    #detect collision with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            # game_ison=False;
            scoreboard.reset();
            # scoreboard.game_over();
            snake.reset();
    
screen.exitonclick();














screen.exitonclick();
