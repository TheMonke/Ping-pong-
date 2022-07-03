# Ping pong?
# By @wiyosh001
import turtle
import winsound

wn = turtle.Screen()
wn.title("LOL")
wn. bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_1 = 0
score_2 = 0 

# Paddel#1
paddel_1 = turtle.Turtle()
paddel_1.speed(0)
paddel_1.shape("square")
paddel_1.color("white")
paddel_1.shapesize(stretch_wid=5, stretch_len=1)
paddel_1.penup()
paddel_1.goto(-350, 0)
# Paddel#2
paddel_2 = turtle.Turtle()
paddel_2.speed(0)
paddel_2.shape("square")
paddel_2.color("white")
paddel_2.shapesize(stretch_wid=5, stretch_len=1)
paddel_2.penup()
paddel_2.goto(350, 0)

# Main ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.50
ball.dy = 0.50

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Mulozi 1: 0 Mulozi 2: 0", align="center", font=("Courier", 24, "normal"))

#Function
def paddel_1_up():
    y = paddel_1.ycor()
    y += 20
    paddel_1.sety(y)

def paddel_1_down():
    y = paddel_1.ycor()
    y -= 20
    paddel_1.sety(y)

def paddel_2_up():
    y = paddel_2.ycor()
    y += 20
    paddel_2.sety(y)

def paddel_2_down():
    y = paddel_2.ycor()
    y -= 20
    paddel_2.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddel_1_up, "w")
wn.onkeypress(paddel_1_down, "s")
wn.onkeypress(paddel_2_up, "Up")
wn.onkeypress(paddel_2_down, "Down")


#Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1 
        pen.clear()
        pen.write("Mulozi 1: {} Mulozi 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Mulozi 1: {} Mulozi 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    
    # Paddel and ball collisons
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddel_2. ycor() + 40 and ball.ycor() > paddel_2.ycor() -40):
      ball.setx(340)
      ball.dx *= -1
      winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddel_1. ycor() + 40 and ball.ycor() > paddel_1.ycor() -40):
      ball.setx(-340)
      ball.dx *= -1
      winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)