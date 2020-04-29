#Balanced Brackets 

def brackets(bracket):
  #bracket is of string type
  if bracket=="}":
    return "{"
  if bracket=="]":
    return "["
  if bracket==")":
    return "("

#create a function to check whwther brackets are balanced or not .
#s={[)()]}
def check_balance(s):
  sn=[]
  for i in s:
    if i=="{" or i=="[" or i=="(":
      sn.append(i)
    elif i=="}" or i=="]" or i==")":
      if sn!=[]:
        sign=sn.pop()
        if sign==brackets(i):
          pass
        else:
          return False  
      else:
        return False  

  return True


boolean=check_balance(")[](}}")
if boolean:
  print("balance brackets")
else:
  print("Not balanced")  



    
