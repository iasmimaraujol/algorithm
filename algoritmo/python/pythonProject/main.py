l1 = [2,5,5,5]
l2 = [2,2,3,5,5,7]
def iguals(l3,l4):
    l = []
    cont = 0
    dim1 = len(l3)
    dim2 = len(l4)
    for i in range(dim1):
        a = 0
        for j in range(dim2):
            if(l3[i]==l4[j]):
                cont += 1
                a = 1
                aux = l3[i]
        if a == 1:
            l.append(aux)
    return l
print(iguals(l1,l2))

