s1 = input()
s2 = input()
count=0
i=0
while(i<len(s1)):
    if(s1[i]==s2[len(s2)-1]):
        count+=1
    i+=1
print(count)