def aVeryBigSum(ar):
    sum_ = sum(ar)
    # Write your code here
  #  h, sum_ = len(ar), 0
   # x = ((10**h)**2)/10
    #print(x)
    #for i in range(h + 1):
    #    sum_ = sum_ + i
    #sum_ = sum_ + h*x
    return int(sum_)

n = [0, 1, 2, 4, 6, 5, 3]
#print(aVeryBigSum(n))

def findMedian(arr):
    # Write your code here
    i = int(len(arr)/2)
    ar = sorted(arr)
    return ar[i] 

#print(findMedian(n))

def insertionSort(arr):
    # Write your code here
    x = len(arr)
    cont_ = 0
    for i in range(x):
        a = i
        while a != 0:
            if(arr[a] < arr[a - 1]):
                cont_ += 1
                aux = arr[a - 1]
                arr[a - 1] = arr[a]
                arr[a] = aux        
                a -= 1    
    return cont_
n = [5]	
print(insertionSort(n))