







def show_elemt():
    i = 0
    while i < 3:
        x_rand = random.randint(1, (len(data)-1))
        y_rand = random.randint(1, (len(data)-1))
        if data[y_rand ][x_rand] == " ":
            data[y_rand][x_rand] = "A"
            i +=1

        
perso = "X"
pos_perso = [1, 1]
n_ligne = 0
for ligne in lab:
    if pos_perso[1] == n_ligne :
        
        print(ligne, "<- ligne du personnage")
    else :
        print(ligne)
  
    n_ligne = n_ligne + 1




    def verification_deplacement(lab, pos_col, pos_ligne):
        
        n_cols = len(data[0])
        n_lignes = len(data)

        if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or pos_col > (n_cols -1) :
            return None

        elif lab[pos_ligne][pos_col] != " " :
        return None
        else :
        return [pos_col, pos_ligne]

n_ligne = 0
for ligne in data:
    for i in range(1, 4) :
        ligne = ligne.replace(str(i), tresor)
    if n_ligne == pos_perso[1]:
        print(ligne[0:pos_perso[0]] + perso + ligne[pos_perso[0]+1:]) 
    else :
        print(ligne)
n_ligne += 1










def deplacement_perso (data, pos_perso, choix):
    new_pos = [pos_perso[0], pos_perso[1]]
    if choix   == "H" :
       new_pos = [new_pos[0], new_pos[1] -1]
    elif choix == "B" :
       new_pos = [ new_pos[0], new_pos[1] +1]
    elif choix == "G":
       new_pos =  [new_pos[0] -1, new_pos[1]]
    elif choix == "J" :
       new_pos =  [new_pos[0] +1, new_pos[1]]
    dep = verification_deplacement(data, new_pos[0], new_pos[1])
    if dep == False:
        print("déplacement impossible")
        return pos_perso
    return new_pos


def sortie(data, pos_col, pos_ligne):
    global num_ob 

    if data[pos_ligne][pos_col] == "O" and num_ob == 3 :
        print("Bravoooo !!!! vous avez gagné et vous avez : " + num_ob + " objets")
    else:
        print("Désolé !!!! vous avez perdu et vous avez seulement : " + num_ob + " objets")

