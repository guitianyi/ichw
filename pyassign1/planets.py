import turtle
import math
h=(math.pi)
def distance(a,b,c,d):
    dis=((a-c)**2+(b-d)**2)**0.5
    return dis
def oval(t,n):
    r=50*n+50
    for m in range(100):
        t.left(360/100)
        angle1=m*h/50
        angel2=(m+1)*h/50
        f=distance(r*(math.sin(angle1)),r*0.75*(math.cos(angle1)),r*(math.sin(angle2)),r*0.75*(math.cos(angle2)))
        t.forward(f)
wn=turtle.Screen()
colors=['blue','green','red','black','brown','sea green']
sun=turtle.Turtle()
sun.shape('circle')
sun.color('yellow')
for k in range(6):
    planet=turtle.Turtle()
    planet.color(colors[k%6])
    planet.shape('circle')
    rad=50*k+50
    planet.penup()
    planet.goto(rad,0)
    planet.pendown()
    planet.left(90)
    oval(planet,k)  
