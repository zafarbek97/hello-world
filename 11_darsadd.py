from turtle import Turtle, Screen
oyna = Screen()
oyna.title("MyTurtleWindow")

chiziq = Turtle()
chiziq.color("lime")
chiziq.pensize(12)
chiziq.speed(2)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(200, 200)
chiziq.down()
chiziq.goto(200, -200)
chiziq.goto(-200,-200)
chiziq.goto(-200, 200)
chiziq.goto(200, 200)

chiziq1 = Turtle()
chiziq1.color("cyan")
chiziq1.pensize(14)
chiziq1.speed(3)
chiziq1.hideturtle()
chiziq1.up()
chiziq1.goto(220, 220)
chiziq1.down()
chiziq1.goto(220, -220)
chiziq1.goto(-220,-220)
chiziq1.goto(-220, 220)
chiziq1.goto(220, 220)

chiziq2 = Turtle()
chiziq2.color("blue")
chiziq2.pensize(24)
chiziq2.speed(4)
chiziq2.hideturtle()
chiziq2.up()
chiziq2.goto(240, 240)
chiziq2.down()
chiziq2.goto(240, -240)
chiziq2.goto(-240,-240)
chiziq2.goto(-240, 240)
chiziq2.goto(240, 240)

koptok = Turtle()
koptok.shape("circle")
koptok.up()
koptok.color("red")
koptok.goto(0,0)

step_x = 0.7
step_y = 0.9
while True:
	x,y = koptok.position()
	if x + step_x >= 190 or x + step_x <= -190:
		step_x = -step_x
	if y + step_y >= 190 or y + step_y <= -190:
		step_y = -step_y

	koptok.goto(x+step_x, y+step_y)

oyna.mainloop()