l=list(map(int,input('Enter the list').split()))
n=int(input('Enter the no'))
l.sort()
i=0
j=len(l)-1
while i<j:
    if l[i]+l[j]==n:
        print(l[i],l[j])
        break
    elif l[i]+l[j]<n:
        i+=1
    elif l[i]+l[j]>n:
        j-=1