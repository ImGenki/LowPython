def Demande():
    age=int(input("Veuillez entrer votre age \n"))
    poids=int(input("Veuillez entre votre poids (en kg) \n"))
    if poids > 100:
        print("U are fat boy")
    taille=int(input("Veuillez entre votre taille (en cm) \n"))
    sexe=(input("Veuillez entre votre sexe F/H \n"))
    
    print("Quel est votre niveau d'activité?\n")
    print("Sédentaire = 1")
    print("Très faible activité = 1.2")
    print("Activité légère = 1.4")
    print("Activité modérée = 1.6")
    print("Haute activité = 1.8")
    print("Activité extreme = 2")
    act=float(input())
    choix=input("Voulez vous maigrir ou grossir ? M ou G \n")

    return age,poids,taille,sexe,act,choix


def calc_BRM(age,poids,taille,sexe,act,choix):
    if sexe == "H":
        BRM=66+(13.7*poids)+(5*taille)-(6.8*age)
    if sexe == "F":
        BRM=655+(9.6*poids)+(1,7*taille)-(4.7*age)
    BRM_a=act * BRM
    if choix == "M":
        BRM_final=BRM_a*0.9
        return BRM_final
    if choix == "G":
        BRM_final=BRM_a*1.1
        return BRM_final
    else:
        print("Erreur")


def main():
    age,poids,taille,sexe,act,choix=Demande()
    BRM_final=calc_BRM(age,poids,taille,sexe,act,choix)
    print("Votre nb de calories par jour est de ",BRM_final)

main()