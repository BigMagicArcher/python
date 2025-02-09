print("Znajdujesz się w ciemnym pokoju z dwoma drzwiami. Które wybierasz?")
drzwi = input("> ")
if drzwi == "1":
    print("Widzisz tutaj wielkiego tygrysa, który je krakersy.")
    print("Co robisz?")
    print("1. Walczysz z tygrysem>")
    print("2. Zabierasz mu krakersy")
    print("3. Przechodzisz przez następne dzwi")
    print("4. Nadeptujesz tygrysowi na ogon")
    tygrys = input("> ")

    if tygrys == "1" or tygrys == "4":
        print("To był kiepski pomysł. Zostajesz zjedzony!")
    elif tygrys == "2":
        print("Tygrys nie był zadowolony.")
        print("Najpierw zjadł ciebie, a potem krakersy")
    elif tygrys == "3":
        print("Spotykasz kupca który chce ci sprzedać niespodziankę")
        print("Czym mu zapłacisz?")
        print("1 .Złotem")
        print("2. Srebrem")
        print("3. Krakersami")
        kupiec = input("> ")

        if kupiec == "1":
            print("Kupiec sprzedaje ci szarlotkę. Mniam!")
        elif kupiec == "2":
            print("Kupiec nie lubi srebra sprzedaje ci zgniłe jajo!")
        elif kupiec == "3":
            print("Nie masz kaakersów . Wracasz do tygrysa żeby je odebrać")
            print("Tygrys nie jest zadowolony. Przegrywasz")
        else:
            print("Kupiec nie jest zadowolony odchodzi z łzami w oczach")
    else:
        print("Zła odpowiedź. Przegrywasz")
elif drzwi == "2":
    print("Za drzwiami stoi posąg rycerza!")
    print("Giniesz!")
    
    
