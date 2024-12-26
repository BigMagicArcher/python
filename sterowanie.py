import turtle
t = turtle.Pen()
t.speed (0)

kolor = (0.2, 0.5, 1)
t.color (kolor)
turtle.bgcolor("black")

for i in range (50) :
    ruch = input("Co chcesz teraz zrobić: ")
    if ruch == "przód" or ruch == "tył":
        droga = int (input("Jaką drgę chcesz pokonać: "))

        if ruch == "przód":
            t.forward(droga)
        else:
            t.bckward(droga)
    elif ruch == "lewo" or ruch == "prawo":
      kat = int(input("o jaki kąt chcesz zakręcić: "))
       
      if ruch == "lewo":
             t.left(kat)   
    elif ruch == "koło":
        promien = int(input("podaj promień koła: "))
        t.circle(promien)
    else:
        print("Nie poprawny ruch")
