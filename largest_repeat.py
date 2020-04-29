#find the largest consecutive characters : 

#example "AABCDDBBBEA" return {'B':3}
#using Traversing Algorithm
#in c you can make structures : 
Info_dict={
'current':'',
'max_count':0,
'max_char':'',
'prev_char':'',
'count':0
}

def large_cons_str(s):
  global Info_dict
  for i in s:
    Info_dict['current']=i
    if i==Info_dict['prev_char']:
      Info_dict['count']+=1
    else:
      Info_dict['count']=1
    if Info_dict['count']>Info_dict['max_count']:
      Info_dict['max_count']=Info_dict['count']
      Info_dict['max_char']=Info_dict['current']

    Info_dict['prev_char']=Info_dict['current']
  return {Info_dict['max_char']:  Info_dict['max_count']}

ans=large_cons_str("AABCDDBBEEEA")
print(ans)


