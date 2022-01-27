x = 0
while x < 50:
    print("!!!repl.it's resolution won't show full window so run this in visual studio or something!!!")
    x = x + 1
#-----import statements-----
import turtle
import random
import re
import math

#-----game configuration----
color = "green"
shape = "circle"
size = 3
score = 0
combo = 0
#-----initialize turtle-----
#turtle
travis = turtle.Turtle()
travis.fillcolor(color)
travis.shape(shape)
travis.shapesize(size)
travis.penup()
pos_x = random.randint(0, 300)
pos_y = random.randint(0, 300)
travis.goto(pos_x, pos_y)

#score
turtle_score = turtle.Turtle()
font_setup  = ("Arial", 20, "normal")
turtle_score.hideturtle()

#combo
turtle_combo = turtle.Turtle()
turtle_combo.hideturtle()

#accuracy
turtle_accuracy = turtle.Turtle()
turtle_accuracy.hideturtle()

#details
turtle_details = turtle.Turtle()
turtle_details.hideturtle()
turtle_details.penup()
turtle_details.goto(-50, -50)
turtle_details.pendown()
turtle_details.speed(100)
turtle_details.pensize(5)
turtle_details.forward(400)
turtle_details.left(90)
turtle_details.forward(400)
turtle_details.left(90)
turtle_details.forward(400)
turtle_details.left(90)
turtle_details.forward(400)


#-----game functions--------
def turtle_click(x, y):
  global score
  global combo
  print("#=======================================================#")
  print("location of click=", x,y)
  random_pos_x = random.randint(0, 300)
  random_pos_y = random.randint(0, 300)
  print("x_coords[%s] y_coords[%s]" % (random_pos_x, random_pos_y))
  x_pos_acc = x - random_pos_x
  y_pos_acc = y - random_pos_y
  print("x_acc[%s] y_acc[%s]" % (x_pos_acc, y_pos_acc))
  def overall_acc(x, y):
      output_acc = x % y
      acc_point = abs(output_acc)
      return(acc_point)


  print(overall_acc(x_pos_acc, y_pos_acc))
  travis.goto(random_pos_x, random_pos_y)
  def accuracy():
    if overall_acc(x_pos_acc, y_pos_acc) <= 35:
      return(300)
    elif overall_acc(x_pos_acc, y_pos_acc) <= 45:
      return(100)
    elif overall_acc(x_pos_acc, y_pos_acc) <= 55:
      return(50)
    elif overall_acc(x_pos_acc, y_pos_acc) > 56:
      return(0)
  
  turtle_accuracy.goto(random_pos_x, random_pos_y)
  turtle_accuracy.clear()
  turtle_accuracy.write(accuracy(), font=font_setup)

  if accuracy() == 0:
    combo = 0
  else:
    combo = combo + 1
  score = score + accuracy()
  def total():
    if combo == 0:
      total = score + accuracy()
      return(total)
    else:
      total = score * combo
      return(total)
  print("combo[%s] accuracy[%s] score[%s]" % (combo, accuracy(), total()))
  print("#=======================================================#")

  turtle_combo.goto(0, 0)
  turtle_combo.goto(random_pos_x, random_pos_y)
  turtle_combo.goto(0, 0)
  turtle_combo.clear()
  turtle_combo.write(combo, font=font_setup)  
  turtle_score.goto(random_pos_x, random_pos_y)
  turtle_score.goto(250, 300)
  turtle_score.clear()
  turtle_score.write(total(), font=font_setup)
#-----events----------------
wn = turtle.Screen()
wn.setup(width=1260, height=860, )
travis.onclick(turtle_click)


wn.mainloop()