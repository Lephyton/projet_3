



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
    for line in data :
        for element in line :
            print(element, end="")
        print()
    n_ligne = 0
    for ligne in data :
        if n_ligne == pos_perso[1]:
            print(ligne[0:pos_perso[0]] + perso + ligne[pos_perso[0]+1:])
        else :
            print(ligne)
        n_ligne = n_ligne +1
#Pour positionner notre personnage dans le labyrinthe, nous allons numéroter chaque 
# case en fonction de sa colonne et de sa ligne.



data = read_lab()
show_lab (data, "X", [1, 1])


