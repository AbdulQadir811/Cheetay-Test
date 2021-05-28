
def merge(arr, l, m, r):
    Largest_Number = ""
    n1 = m - l + 1
    n2 = r- m
  

    L = [0] * (n1)
    R = [0] * (n2)
  

    for i in range(0 , n1):
        L[i] = arr[l + i]
  
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
  
    i = 0     
    j = 0    
    k = l     
  
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            Largest_Number = Largest_Number + str(L[i]) 
            arr[k] = L[i]
            i += 1
        else:
            Largest_Number = Largest_Number + str(R[j]) 
            arr[k] = R[j]
            j += 1
        k += 1
  
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
  
    
    while j < n2:
        Largest_Number = Largest_Number + str(R[j]) 
        arr[k] = R[j]
        j += 1
        k += 1
   
    return Largest_Number

def mergeSort(arr,l,r):
    if l < r:
  
        
        m = (l+(r-1))//2
  
        
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        Largest_Number =  merge(arr, l, m, r)
        return Largest_Number
  

def printLargest(arr):
    arr = map(int,arr)
    arr =list(arr)
    result =mergeSort(arr,0,len(arr)-1)
    return result[::-1]
