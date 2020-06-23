# Uses python3
import sys

def first(arr, low, high, x, n) : 
    if(high >= low) : 
        mid = low + (high - low) // 2
        if( ( mid == 0 or x > arr[mid - 1]) and arr[mid] == x) : 
            return mid 
        elif(x > arr[mid]) : 
            return first(arr, (mid + 1), high, x, n) 
        else : 
            return first(arr, low, (mid - 1), x, n) 
      
    return -1
 
def last(arr, low, high, x, n) : 
    if (high >= low) : 
        mid = low + (high - low) // 2
        if (( mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x) : 
            return mid 
        elif (x < arr[mid]) : 
            return last(arr, low, (mid - 1), x, n) 
        else : 
            return last(arr, (mid + 1), high, x, n) 
              
    return -1
def is_Maj(a,x):
    n=len(a)
    init_pos = first(a, 0, n - 1, x, n)  
    fin_pos  = last(a, 0, n - 1, x, n)
    #print(init_pos,fin_pos)
    
    if (fin_pos-init_pos+1) > n//2:
        return 1
    return 0    

def get_majority_element(a, left, right):
    a=sorted(a)
   
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
       
    for i in range(len(a)):
        l=is_Maj(a,a[i])
        if l:
            return 1
    return -1

if __name__ == '__main__':
    #input = sys.stdin.read()
    n, *a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
