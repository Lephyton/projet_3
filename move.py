perso = "X"
pos_perso = [1, 1]
n_ligne = 0
for ligne in lab:
    if pos_perso[1] == n_ligne :
        
        print(ligne, "<- ligne du personnage")
    else :
        print(ligne)
  
    n_ligne = n_ligne +1
