



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

def show_lab (data, pos_perso):
    for line in data :
        for element in line :
            print(element, end="")
        print()
    perso = "X"
    pos_perso = [1, 1]
    n_ligne = 0
    for ligne in data:
        if pos_perso[1] == n_ligne :
            
            print(ligne, "<- ligne du personnage")
        else :
            print(ligne)
    
        n_ligne = n_ligne + 1
#Pour positionner notre personnage dans le labyrinthe, nous allons numéroter chaque 
# case en fonction de sa colonne et de sa ligne.



data = read_lab()
show_lab (data)


