slowo = input("Podaj dowolne słowo: ")

if slowo:
    if "a" in slowo:
        print("W twoim słowie znajduje się litera a")
    elif "e" in slowo:
        print("W twoim słowie znajduje się e")
    else:
        print("W twoim słowie nie ma litery a ani e")
else:
    print("Nie podano żadnego słowa!")
