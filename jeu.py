

my_list_1 = []
while len(my_list_1) < 21 :
    my_list = []
    while len(my_list)< 21 :
        my_list.append("x")
    my_list_1.append(my_list)
print(my_list_1)


    


lab_1 =   [ "+--------------------------+",
            "|                          |",
            "|                          |",
            "|                          |",
            "|                          |",
            "|                         0|",
            "+--------------------------+", ]







def show_lab (lab):
    for line in lab_1 :
        print(line)

show_lab(lab_1)





def show_lab_border(size_lab):
    print("+{}+".format("-"*(size_lab - 2)))
    for i in range(size_lab - 2) :
        print("|{}|".format(" " * (size_lab - 2)))
    print("+{}+".format("-"*(size_lab - 2)))

show_lab_border(40)
    