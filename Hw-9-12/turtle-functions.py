print("It can be used multipule tiems")

import turtle

def square(t,x,y,w,color,sidelen):
    """
    Draw a suare using the turtlepassed into t
    
    Parameters:
        t - a turtle
        x,y - location
        w - width of sidelen
        color - colorcolor to draw in
        sidelen - lengthof eacgh side
    Returns:
        nothing
    """
    #set the location,color,andf width
    t.penup()
    t.goto(x,y)
    t.width()
    t.color(color)
    t.pendown()
    #draw a square
    for i in range(6):
        t.forward(sidelen)
        t.right(60)
        
#def triangle(fill in these):
#    #code to draw the triangle

#def hexagon(fill in these):
#    #code to draw the hexagon
    
#def ngon(t,numsides,x,y,color,width,sidelen):
#    #code to draw the ngon

wn = turtle.Screen() 

crush = turtle.Turtle()

square(crush,0,0,1,"green",100)

squirt = turtle.Turtle()
square(squirt,100,100,5,"red",80)
square(crush,-50,30,3,"yellow",100)
crush.setheading(45)
square(crush,150,30,2,"blue",60)


wn.exitonclick()
wm.mainloop()
