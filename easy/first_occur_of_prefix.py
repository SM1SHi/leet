
def first_occ(first, second):
    lst1 = list(first)
    lst2 = list(second)
    for i in range(len(lst1)):
        if lst1[i] in lst2:
            print(lst2.index(lst1[i]))
            break 
    print("finished.")
first_occ("xd","kuraaaaaaaaaaaaacxd")
