#minwalk v1 

import numpy as np

def minWalk(array,n):
    
    #initialize the partialsum matrix
    rows = n+2
    cols = n
    size = rows*cols
    Partialsums = np.array([0]*size).reshape(rows,cols)
    

    #find matrix
    for i in range(0,n):
        Partialsums[0][i]=999
        Partialsums[n+1][i]=999
        Partialsums[i+1][0]=array[i][0]

    
    for j in range(1,n):
        for i in range(1,n+1):
        
            Partialsums[i,j]=array[i-1][j] + min(Partialsums[i-1,j-1],Partialsums[i,j-1],Partialsums[i+1,j-1])
    Partialsums = np.delete(Partialsums, (0), axis=0)
    Partialsums = np.delete(Partialsums, (n), axis=0)

    #find minwalk
    array=[0 for i in range(n)]
    
    
    minus=  min([Partialsums[i][n-1] for i in range(0,n)])
    
    mins_index=[]
    for i in range(0,n):
        if Partialsums[i][n-1]==minus:
            mins_index.append(i)
   
    print(f"minus:{minus}, indexes:{mins_index}")
    

    
    context={}
    context["matrix"]=Partialsums
    #context["minwalk"]=array
    return context

rows=10
columns=10
array=np.random.randint(0, 10, (rows, columns))
print(array,"\n")

a=minWalk(array,10)

print(a["matrix"],"\n")
#print(a["minwalk"],"\n")
