""" # 1.Square

from turtle import*

speed("slowest")

fd(100)
lt(90)

fd(100)
lt(90)

fd(100)
lt(90)

fd(100)
lt(90)

mainloop()  # This line is needed to keep the window open   """











""" # 2.Hexagon without a loop

from turtle import*

speed("slowest")

angle = 360/6
fd(100)
rt(angle)

fd(100)
rt(angle)

fd(100)
rt(angle)

fd(100)
rt(angle)

fd(100)
rt(angle)

fd(100)
rt(angle)

hideturtle()
mainloop()  # This line is needed to keep the window open   """ 










""" # 3.Hexagon using a 'for' loop

from turtle import*

speed ('slowest')

distance=100
sides=6

for i in range(sides):
    fd(distance)
    rt(360/sides)
    
hideturtle()
mainloop()  """









""" # 4.Hexagon with a Nested Loop

 
from turtle import*

speed ('slowest')

distance=100
sides=6

for i in range(sides):
    pencolor('red')
    fd(distance)
    rt(360/sides)
    for i in range(sides):
        pencolor('green')
        fd(distance/2)
        rt(360/sides)
    
hideturtle()
mainloop()  """










""" # 5.Decagon(10 sides) using a loop

from turtle import*

speed("slowest")

angle = 360/10
for i in range(10):
    fd(100)
    rt(angle)
hideturtle()
mainloop()  """










""" # 6. Hexagon using a 'for' loop and write() function to return the values of 'i' throughtout the traversal.

from turtle import*

speed('fastest')

distance=100
sides=6

for i in range(sides):
    fd(distance)
    rt(360/sides)
    for i in range(sides):
        fd(distance/2)
        rt(360/sides)
        write(i)

hideturtle()
mainloop()  """










# 7. Few changes in the above program i.e. - (6)

from turtle import*

speed('fastest')

distance=100
sides=6

for i in range(sides):
    pencolor('green')
    fd(distance)
    rt(360/sides)
    circle(distance/2)
    for i in range(sides):
        pencolor('brown')
        fd(distance/2)
        rt(360/sides)
        dot(10)
        write(i)

hideturtle()
mainloop()  