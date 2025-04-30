def powitanie():
    print('Hello World')

def linia():
    print("+" + "-" * 28 + "+") 


def menu():
    linia()
    print('| {:^26} |'.format('Witaj w mojej super grze'))
    linia()
    print('| {:^13}{:^13} |'.format('Nowa gra', 'Wyjśćie'))
    linia()
    print('| {:<8} {:>17} |'.format('Autor', 'Leon Krewetka'))
    linia()
    
    






powitanie()
powitanie()
powitanie()
powitanie()

menu()
