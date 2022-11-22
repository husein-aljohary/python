import turtle


wind=turtle.Screen()
wind.title("Welcome to Ping Pong Game")
wind.bgcolor("orange")
wind.setup(width=800,height=600)
wind.tracer(0)

alex = turtle.Turtle()
alex.penup()
alex.hideturtle()
alex.speed(10)
alex.goto(-390,297)
alex.pendown()
alex.goto(390,297)
alex.goto(390,-297)
alex.goto(-390,-297)
alex.goto(-390,297) 


#stick1
stick1=turtle.Turtle()
stick1.speed(0)
stick1.shape("square")
stick1.color("black")
stick1.shapesize(stretch_wid=5,stretch_len=1)
stick1.penup()
stick1.goto(-350,0)

#stick2
stick2=turtle.Turtle()
stick2.speed(0)
stick2.shape("square")
stick2.color("red")
stick2.shapesize(stretch_wid=5,stretch_len=1)
stick2.penup()
stick2.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
#ball.shapesize(stretch_wid=5,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx=0.9
ball.dy=0.9
#########
l=0
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1: 0    player 2: 0",align="center",font=("courier",24,"normal"))
#######
level=1
lev=turtle.Turtle()
lev.speed(0)
lev.color("white")
lev.penup()
lev.hideturtle()
lev.goto(0,200)
lev.write("level-{}".format(level),align="center",font=("courier",24,"normal"))

#print("\n")
#score.write("\nr4444444444444444444",font=("courier",24,"normal"))
#score.write("level{}".format(level),align="center",font=("courier",24,"normal"))


#########
def stick1_up():
    y=stick1.ycor()
    y+=15
    stick1.sety(y)

def stick1_down():
    y=stick1.ycor()
    y-=15
    stick1.sety(y)
###
def stick2_up():
    y=stick2.ycor()
    y+=15
    stick2.sety(y)

def stick2_down():
    y=stick2.ycor()
    y-=15
    stick2.sety(y)

wind.listen()
wind.onkeypress(stick1_up,"w")       
wind.onkeypress(stick1_down,"s")

wind.onkeypress(stick2_up,"Up")       
wind.onkeypress(stick2_down,"Down")






while True:
    wind.update()

##################vertical bar
    if stick1.ycor()>250:
        stick1.sety(250)
    if stick1.ycor()<-250:
        stick1.sety(-250)

    if stick2.ycor()>250:
        stick2.sety(250)
    if stick2.ycor()<-250:
        stick2.sety(-250)

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1    
##########
    if ball.xcor()>370:
        ball.goto(0,0)
        ball.dx *=-1
        score1 +=1
        score.clear()

        if (score1%3)==0:
            level +=1
            lev.clear()


        score.write("player 1: {}    player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal"))
        lev.write("level-{}".format(level),align="center",font=("courier",24,"normal"))
        #score.write("level{}".format(level),align="center",font=("courier",24,"normal"))

    if ball.xcor()<-370:
        ball.goto(0,0)
        ball.dx *=-1
        score2 +=1
        score.clear()
        
        
        if (score2%3)==0:
            level +=1
            lev.clear()


        score.write("player 1: {}    player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal"))
        lev.write("level-{}".format(level),align="center",font=("courier",24,"normal"))
        #score.write("level{}".format(level),align="center",font=("courier",24,"normal"))


########reflective ball
    if (ball.xcor()>340 and ball.xcor()<350)and (ball.ycor()<stick2.ycor()+40 and ball.ycor()>stick2.ycor()-40):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor()<-340 and ball.xcor()<350)and (ball.ycor()<stick1.ycor()+40 and ball.ycor()>stick1.ycor()-40):
        ball.setx(-340)
        ball.dx *=-1