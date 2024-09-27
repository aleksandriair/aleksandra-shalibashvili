# printing a Christmas tree

from turtle import *

setup(800,600)
bgcolor('lightgreen')
shape('turtle')

# draw the tree

fillcolor('forestgreen')

penup()
goto(-180,-180)
pendown()

begin_fill()
goto(0,220)
goto(180,-180)
goto(7,-180)
goto(7,-260)
goto(-7,-260)
goto(-7,-180)
goto(-180,-180)
end_fill()

# draw the star

fillcolor('yellow')

penup()
goto(0,260)
pendown()

begin_fill()
goto(11,230)
goto(40,230)
goto(16,211)
goto(26,181)
goto(0,200)
goto(-26,181)
goto(-16,211)
goto(-40,230)
goto(-11,230)
goto(0,260)
end_fill()

done()