arr = [1,2,0,2,1,0]
dic = {}
for i in range(len(arr)):
    if arr[i] in dic:
        dic[arr[i]]+=1
    else:
        dic[arr[i]]=1
print(dic)
k=0
for i in range(dic[0]):
    arr[k]=0
    k+=1
for i in range(dic[1]):
    arr[k]=1
    k+=1
for i in range(dic[2]):
    arr[k]=2
    k+=1
print(arr)