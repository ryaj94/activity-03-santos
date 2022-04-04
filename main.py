import santos_script_1_ev as evsc
import santos_script_1_stat as statsc



def option_menu():
    opt = int(input("choose 1 to compute again 2 to exit "))
    if opt == 1:
        main()
    elif opt == 2:
        exit()
    else:
        print("Wrong Input")
        option_menu()

def main():

    base1 = int(input("Base: ")) 
    trap1 = 1
    while trap1 == 1:
        iv = int(input("Individual Value: "))
        if iv >= 0 and iv <=31:
            trap1=0
        else:
            print("Error Input")
        
    trap1 = 1
        
    while trap1 == 1:
        ev = int(input("Effort Values: "))
        if ev >= 0 and ev <=255:
            trap1=0
        else:
            print("Error Input")
            
    lvl = int(input("Level: "))
            
    trap1 = 1
    nature_input = int(input("(1)Benificial or (2)Hindering: "))
    if nature_input == 1:
        nature = 1.1
    else:
        nature = 0.9

   
    a = int(input("1 = Stat or 2 = EV Input: "))

    if a==1:
        
        hp = statsc.pokestats.statReturnHP(base1,iv,ev,lvl)
        ostat = statsc.pokestats.statReturnOtherStat(base1,iv,ev,lvl,nature)
        print("HP is ", hp)
        print("Other Stats is", ostat, '\n')

        option_menu()

    elif a==2:
        stats = int(input("Stats: "))
        d = evsc.pokeev.statReturnD(base1,iv,ev,lvl)
        print("Desired Stat Increase: ", d)
        evs = evsc.pokeev.statReturnEvs(stats,nature,d,lvl)  
        print("Evs needed ", evs, '\n')

        option_menu()
        
    else:
        print("Wrong input")

main()



