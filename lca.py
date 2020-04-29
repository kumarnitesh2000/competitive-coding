

#least common ancestor
tree=["1","3","2","4","6","","","","","5"]
root=tree[0]
def stack_to_x(tree,x):
  arr=[]
  try:
    index_of_x=tree.index(x)
    arr.append(tree[index_of_x])
    while(index_of_x!=0):
      index_of_x=(index_of_x-1)//2
      arr.append(tree[index_of_x])
  except:
    print("Element not Found")
  return arr

def comparison(arr11,arr22):
  print(arr11)
  print(arr22)
  arr=[]
  for i in range(min(len(arr11),len(arr22))):
    elem1=arr11.pop()
    elem2=arr22.pop()
    if elem1==elem2:
      arr.append(elem1)
    else:
      pass
  return arr  

  

 
#now we have to find least common ancestor of 5 and 6 which is 4
arr1=stack_to_x(tree,"4")[:]

arr2=stack_to_x(tree,"5")[:]

final_arr=comparison(arr1,arr2)

print("Far common Ancestor is : ",final_arr[0])
print("Least Common Ancestor is : ",final_arr.pop())







  
    
    
