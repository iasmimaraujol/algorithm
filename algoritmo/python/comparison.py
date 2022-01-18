"""def countSort(arr):
 
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]
 
    # Create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for i in range(256)]
 
    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]
 
    # Store count of each character
    for i in arr:
        count[ord(i)] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]
 
    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans"""
def countSort(array_):
    #take the max. elemnt
    max_ = max(array_)
    #inicializate an array with max + 1
    cont = []
    #output array
    out = []
    for i in range(max_ + 1):
        cont.append(0)
        out.append(0)

    #print(max_, cont)
    #store the count of each element
    for i in range(max_ + 1):
        cont[i] = i + cont[i - 1]
    #print(cont)
    for i in array_:
        aux = int(i)        
        aux2 = cont[aux]     
        aux3 = aux2 - 1
        print(aux, aux2, aux3)
        out[aux3] = i
    #print(out)
    print(cont)
    return array_
l1 = [60,35,81,98,14,87]
print(countSort(l1))