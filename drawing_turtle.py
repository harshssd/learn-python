import turtle

def draw_square(turtle_instance):
    for i in range(1, 5):
        turtle_instance.forward(100)
        turtle_instance.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    
    tommy = turtle.Turtle()
    tommy.shape("turtle")
    tommy.color("white")
    tommy.speed(2)
    for i in  range(1, 37):
        draw_square(tommy)
        tommy.right(10)

    jackie = turtle.Turtle()
    jackie.circle(100)

    window.exitonclick()
    
draw_art()
