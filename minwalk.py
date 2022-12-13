
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
    
    for j in range(n):
        
        array[j]=(min( [Partialsums[i][j] for i in range(0,n)]))

    
    context={}
    context["matrix"]=Partialsums
    context["minwalk"]=array
    return context

rows=3
columns=3
array=np.random.randint(0, 10, (rows, columns))
print(array,"\n")

a=minWalk(array,3)

print(a["matrix"],"\n")
print(a["minwalk"],"\n")