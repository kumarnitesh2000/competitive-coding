


#find the triplet that whose sum is equal to given sum

#complexity O(n^2)
def triplet(arr,given_sum):
  arr.sort()
  for i in range(len(arr)):
    current=arr[i]
    left=i+1
    right=len(arr)-1

    while left<right:
      if (arr[left]+arr[right]+current)==given_sum:
        print("found : ",arr[left],arr[right],current)
        left+=1
        right-=1
      elif (arr[left]+arr[right]+current)<given_sum:
        left+=1
      else:
        right-=1



triplet([4,2,3,1,9],13)

