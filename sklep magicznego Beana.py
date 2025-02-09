print("Jestem Magiczny Bean. Witam cie w moim magicznym sklepie!")
zloto = int(input("Ile złota znajduje się w twojej sakiewce?: "))
zakup = None

if not zloto:
    print("Twoja sakiewka jest pusta. nic Ci nie sprzedam!")
else:
    if not zloto < 100: # zloto >= 100
        print("masz co najmniej 100 złota. Stać cię na koktajl rozsadzający")
        zakup = "koktajl rozsadzający"
    elif not zloto >= 25: # zloto < 25
        print("Masz mniej niż 25 złota. Morzesz kupić szałmac szpigiel")
        zakup = "szałmac szpigiel"
    else: # 25 <= zloto < 100
        print("Twoja sakiewka jest ciężka. Sprzedam ci skórzany pas")
        zakup = "skurzany pas"
    print("W twoim plecaku ląduje", zakup)
        
            
            
