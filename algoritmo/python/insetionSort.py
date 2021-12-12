#project Iasmim Araujo december 10, 2021

array = [1,6,84,92,2,36,74,10,6]
new_array = []

for i in range(len(array) - 1):
    while(array[i + 1] < array[i]):
        aux = array[i + 1]
        array[i + 1] = array[i]
        array[i] = aux
        i = i - 1
print(array)