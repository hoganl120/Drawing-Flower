#Hogan Lee 
#this program will draw petals and leaves to the plygon on each of its vertexes

import turtle
def draw_arc(t, angle, num_segments, length):
    '''
    Draws an arc consisting of 10 segments, turning 4 degrees after each segment.
    The arc is oriented in the turtle's initial direction, and the 
    turtle faces the same direction at the end of the arc.
    '''
    start_turn = ((angle/num_segments) * (num_segments - 1))/2
    t.right(start_turn)        
    for count in range(num_segments):
        t.forward(length/num_segments)
        t.left(angle/num_segments)        
    
    # to straighten out so we're facing the same direction, we need to 
    # undo the last left turn, and then undo the initial 18 degree turn
    t.right(angle/num_segments)  
    t.right(start_turn) 


def draw_petal(t, angle, num_segments, length):
    '''
    Draws a filled pair of arcs.
    '''
    draw_arc(t, angle, num_segments, length)
    t.left(180)
    draw_arc(t, angle, num_segments, length)
    t.left(180)


def draw_squiggles(t, angle, num_segments, length, num_squiggles):
   #Draws the squiggles with 4 segments.

    for i in range(num_squiggles):
      draw_arc(t, angle, num_segments, length)
      draw_arc(t, -angle, num_segments, length)
     
     
def draw_leaf(t, angle, num_segments, length):
    #Makes a leaf within a leaf.
    t.fillcolor("light green")
    t.begin_fill()
    draw_petal(t, angle, num_segments, length)
    t.end_fill()
    t.fillcolor(t.pencolor())
    t.begin_fill()
    draw_petal(t, angle/2, num_segments, length/2)
    t.end_fill()
    
    


    
wn = turtle.Screen()        
alex = turtle.Turtle() 
alex.speed(0)

# number of sides
n = 10

# length of each side
size = 30

# code to draw a polygon
interior_angle = 180 * (n - 2) / n
turn_angle = 180 - interior_angle

for count in range(n):
    #makes the whole image
    alex.pencolor("dark green")
    alex.forward(size/2)
    x=alex.pos()
    alex.right(90)
    draw_squiggles(alex, 90, 10,40,2) 
    draw_leaf(alex, 90, 10, 100)
    alex.penup()
    alex.goto (x)
    alex.pendown()
    alex.left(90)   
    alex.forward(size/2)
    # warm-up problem: at each vertex, draw a line sticking out
    #petal_turn = interior_angle / 2
    #alex.right(petal_turn)        
    #alex.forward(50)
    #alex.backward(50)
    #alex.left(petal_turn)
    
    # at each vertex, draw a petal
    #establishes the pen colors
    petal_turn = interior_angle / 2
    alex.right(petal_turn)  
    alex.color("red")
    alex.fillcolor("yellow")
    alex.begin_fill()
    draw_petal(alex, 40, 10, 100)
    alex.end_fill()
    alex.left(petal_turn)

    # continue with the polygon
    alex.left(turn_angle)


wn.exitonclick()