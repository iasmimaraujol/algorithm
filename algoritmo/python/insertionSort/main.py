#project Iasmim Araujo december 10, 2021

array = [1,6,84,92,2,36,74,10,6]
new_array = []
i = 1
for i in range(len(array) ):
    if array[i] < array[i - 1]:
        print(array)
        while(array[i] < array[i - 1]):
            aux = array[i - 1]
            array[i - 1] = array[i]
            array[i] = aux


print(array)
