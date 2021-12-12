toFind = 5
vect = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
rg = 0
string = ""
x = len(vect)
for a in range(x):
    if(toFind == vect[a]):
        rg = a

if string == "":
    string = str[rg]

print(string)