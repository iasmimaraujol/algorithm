#2D input
m1 = [(-9, -9, -9, 1, 1, 1),
     (0, -9, 0, 4, 3, 2),
     (-9, -9, -9, 1, 2, 3),
      (0, 0, 8, 6, 6, 0),
      (0, 0, 0, -2, 0, 0),
      (0, 0, 1, 2, 4, 0)]
#output
lc = []
#number line and column to loop
L, C = 5, 5
for i in range(0, L - 1):
    for j in range(0, C - 1):
        soma = sum(m1[i][j: j + 3]) + m1[i+1][j+1] + sum(m1[i+2][j: j+3])
        lc.append(soma)

#show output
print(lc)
def mamim(array):
    max_ = 0
    L, C = len(array), len(array)
    for i in range(0, L - 1):
        for j in range(0, C - 1):
            soma = sum(m1[i][j: j + 3]) + m1[i+1][j+1] + sum(m1[i+2][j: j+3])
            if(soma > max_):
                max_ = soma
            


#find max value
max_ = 0
for lc1 in range(len(lc)):
    if(lc[lc1]> i):
        max_ = lc[lc1]

print(max_)

