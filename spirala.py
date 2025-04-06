import turtle
t = turtle.Pen()
t.speed(0)
t.shape('turtle')
turtle.bgcolor('black')

kolory = ['chartreuse', 'deepskyblue', 'red', 'orchid', 'yellow']

imie = turtle.textinput('Pobieranie imienia', 'Jak masz na imię?')

for i in range(100):
    t.color(kolory[i % 5])
    t.up()
    t.forward(i * 5)
    t.down()
    t.write(imie, font=('Verdana', int((i + 5) /5), 'italic'))
    t.left(75)
    


