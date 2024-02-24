def findOrder(matrix):
    result=[0]*(n*m)
    result[0] = matrix[-1][-1]
    k=1
    i=j=0
    while(k<n*m):
        while i>=1 and j<n-1:
            i-=1
            j+=1
            result[k] = matrix[i][j]
            k+=1
        if j<n-1:
            j+=1
            result[k] = matrix[i][j]
            k+=1
        elif i<m-1:
            i+=1
            result[k] = matrix[i][j]
            k+=1
        while i<m-1 and j>=1:
            i+=1
            j-=1
            result[k] = matrix[i][j]
            k+=1
        if i<m-1:
            i+=1;
            result[k] = matrix[i][j]
            k+=1
        elif j<n-1:
            j+=1
            result[k] = matrix[i][j]
            k+=1
    return result  
          
arr=[[1,2,3],[4,5,6],[7,8,9]]
n=m=3
ans=findOrder(arr)   
for num in ans:
    print(num, end=' ')