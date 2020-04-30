

#KMP algorithm : 
#Sequence is given and a string tell whether string present or not :  
#we use hashing concepts :

def hash_function(string):

  length=len(string)
  sum=0
  for i in range(length-1,-1,-1):
    sum=sum+((ord(string[length-i-1])-64)*pow(13,i))

  return sum  

#test Hash function 
#result=hash_function("AAB")
#print(result)



def kmp_algo(sequence,string):
  up_cas_seq=sequence.upper()
  up_cas_str=string.upper()

  length=len(string)
  req=hash_function(string)
  i=0
  while i<len(sequence)-len(string)+1:
    get=hash_function(sequence[i:i+length])
    if req==get:
      return True

    i=i+1
  
  return False


#test case 1:
sequence="AAAB"
string="AAB"
boolean=kmp_algo(sequence,string)
if boolean:
  print(f"yeh this string {string} is present in sequence in same order : {sequence}")
else:
  print("string is not in the sequence : ")  

print("\n")  


#test case 2
#computer
#muter
sequence="computer"
string="muter"
boolean=kmp_algo(sequence,string)
if boolean:
  print(f"yeh this string {string} is present in sequence in same order : {sequence}")
else:
  print("string is not in the sequence : ")
