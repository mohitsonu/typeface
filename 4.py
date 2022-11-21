matrix=[]
for i in range(int(input())):
    li=list(map(int,input().split()))
    matrix.append(li)
sr,er,sc,ec=0,len(matrix)-1,0,len(matrix[0])-1
while(sr<=er or sc<=ec):
    change=0
    ch=0
    for i in range(sc,ec):
        if(matrix[sr][i]==0):
            change=1
            break
    if(change==0):
        sr+=1
        ch=1
    change=0
    for i in range(sc,ec):
        if(matrix[er][i]==0):
            change=1
            break
    if(change==0):
        er-=1
        ch=1
    change=0
    for i in range(sr,er):
        if(matrix[i][sc]==0):
            change=1
            break
    if(change==0):
        sc+=1
        ch=1
    change=0
    for i in range(sr,er):
        if(matrix[i][ec]==0):
            change=1
            break
    if(change==0):
        ec-=1
        ch=1
    if(ch==1):
        break
print("("+str(sr)+","+str(sc)+")"",("+str(sr)+","+str(ec)+")"",("+str(er)+","+str(sc)+")"+",("+str(er)+","+str(ec)+")")