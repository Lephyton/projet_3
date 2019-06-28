



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

def show_lab (data):
    for line in data :
        for element in line :
            print(element, end="")
        print()


data = read_lab()
print(data[1][2])
show_lab (data)


