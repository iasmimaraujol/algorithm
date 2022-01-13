def comparison(arr):
    cont_ = len(arr)
    countt = []
    S = []
    for i in range(0, cont_):
        countt.append(0)
    print(countt)
    for i in range(0,cont_ - 2):    
        for j in range(i + 1, cont_ - 1):
            if arr[i] < arr[j]:
                countt[j] = countt[j] + 1
            else:
                countt[i] = countt[i] + 1
    print(arr)
    print(countt)
    for i in range(0, cont_):
        atual = countt[i]
        
        S[atual] = arr[i]
    return S

arr = [60, 35, 81, 98, 14, 47]
print(comparison(arr))