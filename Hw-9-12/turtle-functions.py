import turtle
    
def square(t,x,y,w,color,sidelen):
    """
    Draw a square using the turtle passed into t
    Parameters:
      t       - a turtle
      x,y     - location
      w       - width of side
      color   - color to draw in
      sidelen - length of each side
    Returns:
      nothing
    """
    # set the location, color, and width
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    # draw a square
    for i in range(4):
        t.forward(sidelen)
        t.right(90)

def triangle(t,x,y,w,color,sidelen):
    """
    Draw a triangle using the turtle passed into t
    Parameters:
      t       - a turtle
      x,y     - location
      w       - width of side
      color   - color to draw in
      sidelen - length of each side
    Returns:
      nothing
    """
    # set the location, color, and width
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    # draw a square
    for i in range(3):
        t.forward(sidelen)
        t.right(120)


#def hexagon(fill in these):
#    #code to draw the hexagon
    
#def ngon(t,numsides,x,y,color,width,sidelen):
#    #code to draw the ngon
        
def hexogon(t,x,y,w,color,sidelen):
    t.penup()
    t.goto(x,y)
    t.width()
    t.color(color)
    t.pendown()
    
    for i in range(6):
        t.forward(sidelen)
        t.right(60)
        
def ngon(t,x,y,w,color,sidelen):
    t.penup()
    t.goto(x,y)
    t.width()
    t.color(color)
    t.pendown()
    
    for i in range(9):
        t.forward(sidelen)
        t.right(45)
        
#def triangle(fill in these):
#    #code to draw the triangle

#def hexagon(fill in these):
#    #code to draw the hexagon
    
#def ngon(t,numsides,x,y,color,width,sidelen):
#    #code to draw the ngon

wn = turtle.Screen() 

crush = turtle.Turtle()

square(crush,0,0,1,"green",50)

squirt = turtle.Turtle()
square(squirt,100,100,5,"red",80)
square(crush,-50,30,3,"yellow",100)
crush.setheading(45)
square(crush,150,30,2,"blue",60)
triangle(squirt,100,100,5,"red",80)
triangle(crush,-50,30,3,"yellow",100)
crush.setheading(45)
triangle(crush,150,30,2,"blue",60)
hexogon(crush,0,0,1,"green",50)
hexogon(crush,100,30,2,"pink",50)
hexogon(crush,-50,30,3,"yellow",40)
hexogon(crush,100,30,2,"black",60)
ngon(crush,0,0,1,"green",50)
ngon(crush,100,30,2,"pink",50)
ngon(crush,-50,30,3,"yellow",40)
ngon(crush,100,30,2,"black",60)


wn.exitonclick()
wm.mainloop()
