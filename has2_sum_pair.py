

# Given an array of integers, and an integer  ‘K’ , 
# find the count of pairs of elements in the array whose sum is equal # to 'K'.

# we will find hashing technique a better approach.
#so first we create strong hash functions prevents collision upto 90 percent  : 


def my_hash_map(arr):
  length=len(arr)

  index_lis=[x for x in range(length)]
  val_lis=[0 for i in range(length)]
  for i in range(len(arr)):
    index=arr[i]%length
    #print(index)
    if val_lis[index]==0:
      val_lis[index]=arr[i]
    else:
      val_lis[(index+1)%length]=arr[i]  
  return val_lis


'''
#test my_hash_map
lis=my_hash_map([43,23,24,21,51])
#search 22
status=True
search_x=21 
#print(lis)
i=((search_x%len(lis))+1)%len(lis)
count=0
while lis[i]!=search_x:
  i=(i+1)%len(lis)
  if count==len(lis):
    status=False
    break
  count=count+1

if status:
  print("hey the result is found : ",lis[i])
else:
  print("Not Found : ",search_x)  
'''



def num_pair_sum(arr,k):
  lis=my_hash_map(arr)
  
  for i in range(len(arr)):
    status=True
    if k>arr[i]:
      val=k-arr[i]
    else:
      val=arr[i]-k

    search_x=val
    j=0
    j=((search_x%len(lis))+1)%len(lis)
    count=0
    while lis[j]!=search_x:
      j=(j+1)%len(lis)
      if count==len(lis):
        status=False
        break
      count=count+1
  
    if status and val+arr[j]==k:
      print(val,arr[j])



#test case 1:
num_pair_sum([1,2,3,4],5)





