import random 

num_ob = 2

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
    global num_ob
    n_cols = len(data[0])
    n_lignes = len(data)
    if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or pos_col > (n_cols -1) :
        return False
    elif data[pos_ligne][pos_col] == "A":
        data[pos_ligne][pos_col] = " "
        num_ob += 1
        return True  
    elif data[pos_ligne][pos_col] == "O":
        return True  

    elif data[pos_ligne][pos_col] != " " :
        return False
    else :
        return True

def choix_du_joueur ():
    choix = input("Entrer votre choix : H = haut, B = bas, G = gauche, J = droite : ")
    while len(choix)!= 1 or choix not in ["H", "B", "G", "J"] :
        print ("Vous n'avez pas fait un bon choix, faite un choix ")
        choix = input("Entrer à nouveau votre choix : H = haut, B = bas, G = gauche, J = droite :")
    return choix


def deplacement_perso (data, pos_perso, choix):
    new_pos = [pos_perso[0], pos_perso[1]]
    if choix == "H" :
       new_pos= [new_pos[0], new_pos[1] -1]
    elif choix == "B" :
       new_pos  = [ new_pos[0], new_pos[1] +1]
    elif choix == "G":
       new_pos =  [new_pos[0] -1, new_pos[1]]
    elif choix == "J" :
       new_pos =  [new_pos[0] +1, new_pos[1]]
    dep = verification_deplacement(data, new_pos[0], new_pos[1])
    if dep == False:
        print("déplacement impossible")
        return pos_perso
    return new_pos

def show_elemt():
    i = 0
    while i < 3:
        x_rand = random.randint(1, (len(data)-1))
        y_rand = random.randint(1, (len(data)-1))
        if data[y_rand ][x_rand] == " ":
            data[y_rand][x_rand] = "A"
            i +=1


def sortie (data, pos_col, pos_ligne):
    print(data[pos_col][pos_ligne])
    if data[pos_col][pos_ligne] == "O" :
        if num_ob == 3 :
            print("Bravoooo !!!! vous avez gagné et vous avez : " + str(num_ob )+ " objets")
            return True
        else:
            print("Désolé !!!! vous avez perdu et vous avez seulement : " + str(num_ob )+ " objets")
            return True
    return False
 
    







data = read_lab()
show_elemt()
data[1][1] = "X"
pos_perso = [1,1]
continuer = True
while continuer :
    show_lab (data, "X", pos_perso)
    choix = choix_du_joueur ()
    new_pos = deplacement_perso(data, pos_perso, choix)
    if sortie(data, new_pos[1], new_pos[0]):
        continuer = False
    data[pos_perso[1]][pos_perso[0]] = " "
    data[new_pos[1]][new_pos[0]] = "X"
    pos_perso = new_pos
    print(num_ob)


