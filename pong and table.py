import turtle
# creating turtle variable fro background
shell=turtle.Screen()
shell.title("pong and table")
shell.bgcolor("pink")
shell.setup(width=1000, height=600)

# creating left turtle
left=turtle.Turtle()
left.color("black")
left.penup()
left.shape("square")
left.setposition(-400,0)
left.shapesize(stretch_wid=6, stretch_len=2)
left.speed(0)

# creating right turtle
right=turtle.Turtle()
right.color("black")
right.penup()
right.shape("square")
right.setposition(400,0)
right.shapesize(stretch_wid=6, stretch_len=2)
right.speed(0)

# creating the ball
ball=turtle.Turtle()
ball.color("blue")
ball.penup()
ball.shape("circle")
ball.speed(40)
ball.dx=5
ball.dy=-5
# intializing the score
leftplayer=0
rightplayer=0

# displaying the score
score=turtle.Turtle()
score.speed(0)
score.color("red")
score.penup()
score.hideturtle()
score.setposition(0,260)
score.write("Leftplayer : 0 Rightplayer : 0",align="center", font=("Courier", 24, "normal"))

# functions to move left paddle up and down
def down():
    y=left.ycor()
    y=y-20
    left.sety(y)

def up():
    y=left.ycor()
    y=y+20
    left.sety(y)

# functions to move right paddle up and down
def dessous():
    y=right.ycor()
    y=y-20
    right.sety(y)

def haut():
    y=right.ycor()
    y=y+20
    right.sety(y)

# binding the function with the key
turtle.listen()
turtle.onkey(down,"s")
turtle.onkey(up, "w")
turtle.onkey(dessous, "Down")
turtle.onkey(haut, "Up")


while True:
    shell.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
# checking borders/ where the ball should bounce back from the boundaries
    if ball.ycor()>280:
        ball.sety(280)
        ball.dy*=-1
    if ball.ycor()<-280:
        ball.sety(-280)
        ball.dy*=-1

    # where the ball should reset at when it goes to far outside behind the paddle if the paddle misses
    if ball.xcor()>500:
        ball.goto(0,0)
        ball.dy *=-1
        leftplayer=leftplayer+1
        score.clear()
        score.write("Leftplayer : {} Rightplayer : {}".format(leftplayer, rightplayer),align="center", font=("Courier",24, "normal"))
    if ball.xcor()<-500:
        ball.goto(0,0)
        ball.dy*=-1
        rightplayer=rightplayer+1
        score.clear()
        score.write("Leftplayer : {} Rightplayer : {}".format(leftplayer,rightplayer),align="center", font=("Courier",24, "normal"))

        # code for paddle and ball collision
    #     if statement here we have given a range in which the collision affect should do its job when
    #     it reaches the right paddle. the range for x is between 360 and 370 and the range for y is between
    #     100/up and -100/down so if the ball touches the paddle between the range it will go to the other
    #     side and u will have a chance in getting a point, the smaller the range the harder it is.
    #
    if (ball.xcor()>360 and ball.xcor()<370) and (ball.ycor()<right.ycor()+100 and ball.ycor()>right.ycor()-100):
        ball.setx(360)
        # ^where the ball goes after it hits the right paddle
        ball.dx*=-1

    # #  same thing here just on the left side so the numbers wll change
    if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<left.ycor()+100 and ball.ycor()>left.ycor()-100):
        ball.setx(-360)
    #     # ^where the ball goes after it hits the left paddle
        ball.dx *= -1
        # velocity^