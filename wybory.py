print("Przed tobą najważniejsza walka!")
bron = input("Przygptuj odpowiednią broń: ")
obrażenia = 0

if bron == "miecz":
    print("Dobry wybór. Naucz się sztychów")
    obrażenia = 5
elif bron == "łuk":
    print("Pamiętaj o wzięciu strzał")
    obrażenia = 4
elif bron == "topór":
    print("Będziesz wbijał gwoździe czy przeciwników?")
    obrażenia = 7.5
else:
    print("Zatem walczysz gołymi rękami")
    bron = "gołe ręce"
    obrażenia = 2.5
print("Twoja bron to {} Zadajesz {} obrażeń".format(bron, obrażenia))
