def comptePoints(mot,points):
    valeur=0
    print(points["J"])
    for lettre in mot:
        valeur+=points[lettre]
    return valeur


def nbr_Consonnes(mot,points):
    cptVoy=0
    cptCons=0
    valVoy=0
    valCons=0
    voyelles=["A","E","I","O","U","Y"]
    for lettre in mot:
        if lettre in voyelles:
            valVoy+=points[lettre]
            cptVoy+=1
        else:
            valCons+=points[lettre]
            cptCons+=1
    print("Nombre de voyelles:",cptVoy,"\nNombre de points des voyelles:",valVoy,"\nNombre de consonnes:",cptCons,"\nNombre de points des consonnes:",valCons)
    return cptVoy,cptCons,valCons,valVoy


def main():
    points_lettres={"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":10,"L":1,"M":2,"N":1,"O":1,"P":3,"Q":8,"R":1,"S":1,"T":1,"U":1,"V":4,"W":10,"X":10,"Y":10,"Z":10}
    motUser=input("Entrez un mot\n")
    motUser_MAJ=motUser.upper()
    score=comptePoints(motUser_MAJ,points_lettres)
    print("Nombre de point de",motUser_MAJ,":",score)
    detail=nbr_Consonnes(motUser_MAJ,points_lettres)



main()