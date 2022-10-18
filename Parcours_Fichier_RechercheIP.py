import os,os.path,re,socket


print("Made by Genki, Files search")


def printligne():
    print("\n=============================\n")

def main():
    listeIP=[]
    listeIPTriee=[]
    chemin=input("Entrer le chemin que vous voulez explorer\n")
    printligne()
    ext_txt=r".txt"
    ext_jpg=r".jpg"
    Mon_IP=[ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0] 
    cheminJPG="PATH"
    for root,dirs,files in os.walk(chemin): 
        for filename in files:
            name,extension=os.path.splitext(filename)
            if extension.endswith(ext_jpg) or extension.endswith(ext_txt):
                if extension.endswith(ext_jpg):
                    print("Fichier JPG trouvé :  "+name)
                    destination=cheminJPG+"/"+filename 
                    source=root+ "/"+filename 
                    os.rename(source,destination) 
                if extension.endswith(ext_txt):
                    print("Fichier trouvé :  "+name,extension)
                    fichier=open(root+"/"+filename,"r") 
                    for ligne in fichier: 
                        print ("\nIp trouvée dans "+ filename+": "+ligne)
                        pattern_deMonIp=re.compile(r"(192.168.51.\d{1,3})")
                        pattern=re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
                        if pattern_deMonIp.match(ligne): 
                            listeIPTriee.append(pattern_deMonIp.search(ligne)[0]) 
                        listeIP.append(pattern.search(ligne)[0])
    print("Voici la liste des IP trouvées: " + str(listeIP))
    printligne()
    print("Voici la liste des IP du même LAN que mon IP: "+ str(listeIPTriee))
    printligne()
    print("Mon addresse IP est la suivante: "+Mon_IP)
    printligne()
    fichier.close()

main()
