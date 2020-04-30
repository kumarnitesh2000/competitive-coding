

#largest are under histogram usin stack
height_arr=[6,1,4,3,4,1]
def cal_largest_area(height_arr):
  stack_index=[]
  area=[]
  i=0
  while i<len(height_arr):

    if stack_index==[] or height_arr[i]>=height_arr[stack_index[len(stack_index)-1]]:


      stack_index.append(i)
      i=i+1

    else:
      top=stack_index.pop()

      if stack_index==[]:
        area.append(height_arr[top]*i)
      else:
        area.append(height_arr[top]*(i-stack_index[len(stack_index)-1]-1))


  while stack_index!=[]:

    top=stack_index.pop()

    if stack_index==[]:
      area.append(height_arr[top]*(len(height_arr)))
    else:
        area.append(height_arr[top]*(len(height_arr)-stack_index[len(stack_index)-1]-1))  

  return area

#test case : 

area=cal_largest_area(height_arr)[:]
print("Area list is : ",area)
print("max area is ",max(area))

