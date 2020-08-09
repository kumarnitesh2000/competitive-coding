def solve(arr):
  maxi  = 0
  init = []
  for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
      init.append(i)
    else:
      init.append(-1)

  #print(init)        
  fin = []
  
  j=0
  
  while j<len(init):
    try:
      
      h=[]
      
      while j<len(init):

        if(init[j]!=-1):
          
          h.append(init[j])
          j=j+1
        else:
          break
          

      fin.append(h)
      j = j+1

    except:
      pass

  #print(fin)      
  c = 0
  for lis in fin:
    if lis==[]:
      pass
    else:
      mini = min(lis)
      maxi = max(lis)+1

      print(f'({mini} {maxi})',end=' ')
      
      c = 1
      
  if c==0:
    print()
    print("No Profit")    
    
    


             
            
#this is input format 
t = int(input())
n  = [0 for i in range(t)]
x = [[] for i in range(t)]

for i in range(t):
    n[i] = int(input())
    x[i] = list(map(int,input().split()))

for i in range(t):
    solve(x[i])
    




