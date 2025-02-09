import random
import time
import sys
nick = input("Wybierz swój nick ale nie za długi: ")
if len(nick) > 20:
    print("Źle wpisany nick! Uruchom ponownie gre aby wpisać krótszy nick!")
    time.sleep(3)
    sys.exit()

zloto = 300
zycie = 100
sila = random.randint(10,17)
wiedza = random.randint(10,15)
def menu():
    print("-" * 30)
    print("| {:^26} |".format(nick))
    print("-" * 30)
    print("| {:<15} {:10} |".format("Złoto:", zloto))
    print("| {:<15} {:10} |".format("Życie:", zycie))
    print("| {:<15} {:10} |".format("Siła:", sila))
    print("| {:<15} {:10} |".format("Wiedza:", wiedza))
    print("-" * 30)
    time.sleep(1)
    print("Wybierz co chcesz zrobić")
    print("1 - sklep")
    print("2 - walka z hopgoblinami")
    print("3 - misje")
    print("4 - boss, odblokowóje się po 7 bitwach")
    wybór = input("Co chcesz zróbić")