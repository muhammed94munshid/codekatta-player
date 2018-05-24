x=input()
y=input()
l1=list(x)
l2=list(y)
k=len(l1)
m=len(l2)
if(m!=k):
    print("")
elif(k==m)and (l1[0:k-1]==l2[0:m-1]):
    print("yes")
else:
    print("no")
    
    
