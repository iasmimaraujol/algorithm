def gradingStudents(grades):
    # Write your code here
    for i in grades:
        aux = int(i)
        while(aux%5 != 0):
            aux += 1
        if aux < 40:
            print(i)
        else:
            if(abs(aux - int(i)) < 3):
                print(aux)
            if(abs(aux - int(i)) >= 3):
                print(i)  



g = [75, 67, 40, 33]
gradingStudents(g)