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

        elif data[pos_ligne][pos_col] != " " :
            return None
        else :
        return [pos_col, pos_ligne]
