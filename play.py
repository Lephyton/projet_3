



def read_lab ():
    """
    this function loads 
    labirynthe from the file lab.txt
    """
    fic = open('lab.txt', 'r') 
    data = fic.readlines()
    fic.close()
    for i in range(len(data)):
        data[i] = list(data[i].strip())
    return data 

def show_lab (data, perso, pos_perso):
    n_ligne = 0
    for ligne in data :
        print(" ".join(ligne)) 
        n_ligne = n_ligne +1

def verification_deplacement(data, pos_col, pos_ligne):
        
    n_cols = len(data[0])
    n_lignes = len(data)

    if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or pos_col > (n_cols -1) :
        return False
    elif data[pos_ligne][pos_col] != " " :
        return False
    else :
         return True

def choix_du_joueur ():
    choix = input("Entrer votre choix : H = haut, B = bas, G = gauche, J = droite")
    while len(choix)!= 1 or choix not in ["H", "B", "G", "J"] :
        print ("Vous n'avez pas fait un bon choix, faite un choix ")
        choix = input("Entrer à nouveau votre choix : H = haut, B = bas, G = gauche, J = droite")
    return choix


def deplacement_perso (data, pos_perso, choix):
    if choix == "H" :
        dep = verification_deplacement(data, pos_perso[0], pos_perso[1] -1)
    elif choix == "B" :
        dep = verification_deplacement(data, pos_perso[0], pos_perso[1] +1)
    elif choix == "G":
        dep = verification_deplacement(data, pos_perso[0] -1, pos_perso[1])
    elif choix == "J" :
        dep = verification_deplacement(data, pos_perso[0] +1, pos_perso[1])
    if dep == False:
        print("déplacement impossible")
    print(dep)



data = read_lab()
data[1][1] = "X"
show_lab (data, "X", [1, 1])
choix = choix_du_joueur ()
deplacement_perso(data, [1, 1], choix)




