import turtle
t = turtle.Pen()
t.speed(0)
t.shape("turtle")
turtle.bgcolor('black')

kolory = ['red', 'chocolate1', 'firebrick1', 'gold1', 'darkred', 'salmon']
promien = 20

for kolor in kolory:
    t. color(kolor)


    for i in range (18):
        t.circle(promien)
        t.left(20)

    promien += 20


