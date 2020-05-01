

#find the length of the string wchich is common is str1 and str2
def longest_common_sub(str1,str2):
  len1=len(str1)+1
  len2=len(str2)+1
  print("len1 is ",len1)
  print("len2 is ",len2)
  mat=[[0] * len1 for i in range(len2)]
  #print(mat)
  for i in range(1,len2):
    for j in range(1,len1):
      if str2[i-1]==str1[j-1]:
        mat[i][j]=mat[i-1][j-1]+1
      else:
        mat[i][j]=max(mat[i-1][j],mat[i][j-1])


  #test 
  #mat[len2-1][len1-1]=1      

      

  return mat    



#test case : 
str1="AGGTAB"
str2="GXTXAYB"
matrix=longest_common_sub(str1,str2)
print("dynamic programming : table -> \n")
for i in range(len(str2)+1):
  print(matrix[i])

print("\n")
print("length of longest common substring are : ",matrix[len(str2)][len(str1)])