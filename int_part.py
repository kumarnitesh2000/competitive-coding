

#return the no. of ways that no. can be partitioned .
def integer_partition(number):
  number+=1

  #create a matrix for dynamic programming 
  #as like db.
  mat=[[0] * number for i in range(number)]

  #now first column is always one as in 0 only one way.
  for i in range(number):
    mat[i][0]=1

  #rows is the summand means : (1+1+1) 1 is summand  
  #column is the sum : 
  for i in range(1,number):
    for j in range(1,number):

      if i>j:
        mat[i][j]=mat[i-1][j]
      else:
        #now adding mat[i-1][j]+mat[i][j-i]
        comb_summond=mat[i-1][j]
        comb_without_summond=mat[i][j-i]

        mat[i][j]=comb_summond+comb_without_summond
  number=number-1

  return mat

number=4
matrix=integer_partition(number)
print("dynamic programming : table -> \n")
for i in range(number+1):
  print(matrix[i])

print("\n")
print("total ways are  : ",matrix[number][number])





