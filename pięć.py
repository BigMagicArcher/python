liczba = int(input("Podaj liczbe z przedziału liczbę od 1 do 10: "))

if liczba >= 1 and liczba <= 10:
    if liczba < 5:
        print("Twoja liczba jest mniejsza od 5")
    elif liczba > 5:
        print("Twoja liczba jest większa od 5")
    else:
        print("Twoja liczba jest rórna 5")
else:
    print("Nie podane liczby od zakresu od 1 do 10")
