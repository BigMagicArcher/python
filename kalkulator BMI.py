import re 
while True:
    zadanie=input("Podaj działanie matematyczne lub wpisz exit aby wyjść: ")
    if zadanie == "exit":
        print("Do widzenia")
        break
    sprawdzenie = re.match(r"[a-z]", zadanie)
    
    if sprawdzenie is None:
        print("{} = {}".format(zadanie, eval(zadanie)))
    else:
        print("Żle napisane działanie!")
    
         
