import time
import re
print("Witaj w kalkulatorze BMI (Body Mass Index)")
print("Nie dotyczy to dzieci!")
time.sleep(2)
while True:
    try:
        waga=input("Podaj swoją wagę w kilogramach lub wpisz exit aby wyjść: ")
        if waga == "exit":
            print("Do widzenia")
            break
        wzrost=input("Podaj swój wzrost w centymetrach: ")
        if wzrost == "exit":
            print("Do widzenia")
            break
        sprawdzenie = re.match(r"[a-z]", waga)
        sprawdzenie2 = re.match(r"[a-z]", wzrost)
        if sprawdzenie is None or sprawdzenie2 is None:
            int_waga = int(waga)
            int_wzrost = int(wzrost)
            int_wzrost = int_wzrost/100
            wynik = round(int_waga/int_wzrost**2, 1)
            print("Twoje BMI to {}".format(wynik))
            if wynik >= 50:
                print("Musisz zastosować dietę!")
            if wynik <= 10:
                print("Nawet mój ojciec nie jest taki chudy!")
        else:
            print("Źle podana wartość!")
        print()
    except ValueError:
        print("Błędna wartość!")
    
         
