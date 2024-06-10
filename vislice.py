import besede
import random

def all():
    MAX_POIZKUSI = 10
    poizkusi = []

    def main():
        štPoizkusov = MAX_POIZKUSI
        beseda = random.choice(besede.listBesed)
        #beseda = "avto"
        beseda = beseda.upper()
        while True:
            štNugotovljenihČrk = 0
            print("Preostalo število poizkusov je " + str(štPoizkusov) + ". ", end='')
            if poizkusi != []:
                print("poskusili se že: ", end='')
                for x in poizkusi:
                    u = x.upper()
                    print(u, end=' ')
                print('')
            print("\nBESEDA: ", end='')
            for x in beseda:
                if x in poizkusi:
                    u = x.upper()
                    print(u, end=' ')
                elif x == ' ':
                    print("_", end=' ')
                else:
                    štNugotovljenihČrk += 1
                    print('-', end=' ')
            print('')

            crkaUporabnika = input("Vnesite črko: ")
            crka = crkaUporabnika.upper()
            if crka not in beseda:
                štPoizkusov -= 1
            
            list.append(poizkusi, crka)
            
            if štPoizkusov <= 0:
                print("\n#######    #####   ##    ##  ######        ###\n    ##    ##   ##  ##    ##  ##   ##      ## ##\n   ##     ##       ##    ##  ######      ##   ##\n  ##      ##  ###  ##    ##  ##   ##    #########\n ##       ##   ##  ##    ##  ##   ##   ##       ##\n#######    #####    ######   ######   ##         ##\n")
                print("Beseda je: " + beseda + ".")
                input()
                print("\n\n\n\n\n\n\n\n\n\n")
                all()

            if štNugotovljenihČrk > 1:
                print("---------------------nadaljuj---------------------")
            else:
                print("\n#######   ###   ###       ###        #####        ###\n    ##    #########      ## ##      ##   ##      ## ##\n   ##     ##  #  ##     ##   ##     ##          ##   ##\n  ##      ##     ##    #########    ##  ###    #########\n ##       ##     ##   ##       ##   ##   ##   ##       ##\n#######   ##     ##  ##         ##   #####   ##         ##\n")
                input()
                print("\n\n\n\n\n\n\n\n\n\n")
                all()

    main()
all()