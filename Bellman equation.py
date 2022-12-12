#code with love
#dynamic programming


lista=[3,-5,10,2,-3,1,4,-8,7,-6,-1]

def subVectorMax(array,n):

    #initialize array
    partialsums =[] 
    for i in range(n):
        partialsums.append(0)


    context={}
    minindex=0 
    maxindex=0 # it represents the higher el in partialsums
    partialsums[0]=array[0]
    

    for i in range(1,n):
        if partialsums[i-1] >=0:
            partialsums[i] = array[i]+partialsums[i-1]
        else:
            partialsums[i]=array[i]
            minindex=i
        if partialsums[maxindex]<partialsums[i]:
            maxindex=i
    context["array"]=array[minindex:maxindex+1] #last included
    context["sum"]=partialsums[maxindex]
    return context

print(subVectorMax(lista,len(lista)))