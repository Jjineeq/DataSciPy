import turtle

t = turtle.Turtle()

t.speed(0)
t.width(3)

length = 10	            

while length < 500:
    t.forward(length) 
    t.right(50)         
    length += 5	        
turtle.done()