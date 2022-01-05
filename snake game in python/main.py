import random
import time
import turtle

# score
score = 0
high_score = 0

# delay
delay = 0.1

# Screen
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.title("Snake Game in Python")
wn.bgcolor("light blue")
wn.tracer(0)

# head
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.shape("circle")
food.color("white")
food.speed(0)
food.penup()
food.goto(0, 100)

# pen
pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0  High Score : 0", align="center", font=("Courier", 24, "normal"))

# Segments list
segments = []

# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for collision
    if head.ycor() > 290 or head.ycor() < -290 or head.xcor() > 290 or head.xcor() < -290:
        head.direction = "stop"
        time.sleep(1)
        head.goto(0, 0)

        # reset the delay
        delay = 0.1

        # reset the score
        score = 0

        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
        # reset the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

    # Check collision with the food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # reduce the delay
        delay -= 0.001

        # increase the score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.speed(0)
        new_segment.penup()
        segments.append(new_segment)

        # Bring the head to the first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check collision with the body
    for segment in segments:
        if head.distance(segment) < 20:
            head.direction = "stop"
            time.sleep(1)
            head.goto(0, 0)

            # reset the delay
            delay = 0.1

            # reset the score
            score = 0

            pen.clear()
            pen.write("Score : {}  High Score : {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            
            # reset the segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

    time.sleep(delay)

wn.mainloop()
