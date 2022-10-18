import random


def jeu(nb1,nb2):
    cpt=1
    while(nb1 != nb2):
        if nb1<nb2:
            print("C'est plus\n")
        elif nb1>nb2:
            print("C'est moins\n")
        nb1=int(input("Entrez un nouveau nombre\n"))
        if cpt>10:
            print("Ton niveau frérot ... c'est sad")
        cpt+=1
    print("Vous avez win en ",cpt,"coups")



def main():
    nbMax=int(input("Entrez le nombre maximum voulu\n"))
    nbalea=random.randint(1,nbMax)
    nb=int(input("Entrez un nombre\n"))
    jeu(nb,nbalea)

main()