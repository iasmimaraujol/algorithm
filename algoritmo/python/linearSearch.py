toFind = 0
vect = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
string = " "
i = 0
while toFind != vect[i]:
    i = i + 1
    if(i == (len(vect))):
        string = "not find"
        break

if string == " ":
    string = str(i)

print(string)
