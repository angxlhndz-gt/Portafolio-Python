from turtle import *
import math
import colorsys

# Agregar el texto en la cabecera
header_text = "Para la niña de las mariposas, me gustas :)"
color("white")  # Color del texto
penup()
goto(-180, 250)  # Posición del texto
pendown()
write(header_text, align="left", font=("Arial", 12, "normal"))

speed(20)
bgcolor("black")
h = 0

# Dibujar el tallo verde del girasol
penup()
goto(0, -100)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()

# Dibujar el girasol
penup()
goto(0, 0)
pendown()
for i in range(16):
    for j in range(18):
        color("yellow")  # Todos los pétalos son amarillos
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)



# Dibujar el centro con semillas en espiral
penup()
goto(0, -20)  # Centrar las semillas en la misma posición que el centro marrón
pendown()
speed(0)
bgcolor("black")
pencolor("black")
shape("triangle")
fillcolor("brown")
phi = 137.508 * (math.pi / 180.0)  # Ángulo para la espiral en radianes

# Dibujar las "semillas" en espiral
for i in range(180 + 40):
    r = 4 * math.sqrt(i)  # Ajuste de la distancia radial
    theta = i * phi  # Ángulo theta en espiral
    x = r * math.cos(theta)  # Coordenada x
    y = r * math.sin(theta)  # Coordenada y
    penup()
    goto(x, y - 20)  # Ajustar la posición vertical de las semillas
    setheading(i * 137.508)  # Ajustar la orientación de la semilla
    pendown()
    if i < 180:  # Limitar el número de "semillas"
        stamp()  # Sellar la forma de triángulo en cada posición

done()
