import turtle

window = turtle.Screen()
window.bgcolor('green')
window.setup(500, 500)
window.title("Отражение мяча")

ball = turtle.Turtle('circle')
ball.turtlesize(2)
ball.hideturtle()
ball.color('gold')
ball.penup()

box = turtle.Turtle()
box.hideturtle()
box.pensize(20)
box.penup()
box.goto(-200, 200)
box.pendown()
box.color('white')

# рисуем рамку
for side in range(4):
    box.fd(400)
    box.right(90)

ball.goto(100, 100)
dx, dy = 1.3, 2.3
ballX, ballY = 50, 50
ball.speed('fastest')
ball.showturtle()

while True:
    ball.goto(ballX + dx, ballY + dy)
    ballX, ballY = ball.xcor(), ball.ycor()
    if ballX < -175 or ballX > 175:
        dx = dx * -1
    if ballY < -175 or ballY > 175:
        dy = dy * -1
