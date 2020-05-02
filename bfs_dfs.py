#Bactracking Basics so first we learn Breadth first search 
#and depth first search :
#backtracking is handy when we have to tell the no. of solutions to the particular problem :
#and hence to this questions 2 solutions are there : 
# 1).Bactracking / Recursion (DFS->base DS)
# 2).Branch and Bound / Recursion(BFS-> base DS)
#now when we require sol. there are certain constraints
#for those constraints we create a function (Bounding function)

#in this we first have to make the state space tree which is sol.
#BFS uses queue
#Dfs uses stack form
#implementation of BFS and DFS.

Nodes=["A","B","C","D","E","F","G"]
starting_node=Nodes[0]
#these are the nodes how to make a graph with this node :
'''
                         (A)
                       /     \
                      /       \

                     (B)       (C)
                    /   \      /  \
                   /     \    /    \
                  (D)     (E) (F)   (G)
 BFS - >  {A,B,C,D,E,F,G} level order in tree case
 DFS - >  {A,B,D,E,C,F,G} preorder in tree case
[
Adjancy matrix :
  A  B C D E F G
A [0,1,1,0,0,0,0],
B [1,0,0,1,1,0,0],
C [1,0,0,0,0,1,1],
D [0,1,0,0,1,0,0]
E [0,1,0,0,0,0,0],
F [0,0,1,0,0,0,0],
G [0,0,1,0,0,0,0]


]

'''
#queue
f,r=-1,-1
explored=[]
queue=[]

def insert_in_queue(val):
  global f,r,queue
  if f==-1:
    f=0
    r=0
  else:
    r=r+1
  queue.append("")  
  queue[r]=val

def delete_in_queue():
  global f,r,queue,explored
  if f==-1:
    #print("Underflow")
    return 0
  else:
    l=queue[f]
    
    if f==r:
      f=-1
      r=-1
    else:
      #print(f"{queue[f]} is deleted .")
      f=f+1
    return l

def tot_mem_Queue():
  return queue[f:r+1]
def connected_node(node,adj_mat):
  global Nodes
  lis=[]
  node_row=Nodes.index(node)
  for i in range(len(Nodes)):
    if adj_mat[node_row][i]==1:
      if Nodes[i] not in Bfs_result:
        lis.append(Nodes[i])
    
  return lis      
#bfs uses queue
Bfs_result=[]
#dfs uses satck
Dfs_result=[]
adj_mat=[
  [0,1,1,0,0,0,0],
  [1,0,0,1,1,0,0],
  [1,0,0,0,0,1,1],
  [0,1,0,0,1,0,0],
  [0,1,0,0,0,0,0],
  [0,0,1,0,0,0,0],
  [0,0,1,0,0,0,0]]
def bfs_traversal():
  global f,r,queue,Nodes
  global Bfs_result
  global starting_node
  global adj_mat
  #prepare adjancy matrix
  
  print("Important Info :")
  for i in range(len(Nodes)):
    for j in range(len(Nodes)):
      if adj_mat[i][j]==1:
        print(f"{Nodes[i]} is connected to {Nodes[j]}.")
  print(25*"~")
  insert_in_queue(starting_node)
  Bfs_result.append(starting_node)

  while queue!=[]:
    try:

      l=delete_in_queue()
      lis=connected_node(l,adj_mat)
      for i in lis:
        insert_in_queue(i)
        Bfs_result.append(i)
        
    except:
      return Bfs_result

  return Bfs_result

        
  
listu=bfs_traversal()
print("the BFS traversal is as follows : ",listu)
dfs_result=[]
def connected_node_a(node,adj_mat):
  global Nodes
  lis=[]
  node_row=Nodes.index(node)
  for i in range(len(Nodes)):
    if adj_mat[node_row][i]==1:
      if Nodes[i] not in dfs_result:
        lis.append(Nodes[i])
    
  return lis
#base ds is stack : 
def dfs_traversal():
  global Nodes
  global adj_mat
  stack=[]
  
  stack.append(Nodes[0])
  dfs_result.append(Nodes[0])
  while stack!=[]:
    top=stack.pop()
    if top not in dfs_result:
      dfs_result.append(top)
    lis=connected_node_a(top,adj_mat)
    for i in range(len(lis)-1,-1,-1):
      stack.append(lis[i])

      


  print("The Dfs Traversal is as follows : ",dfs_result) 

dfs_traversal()     






