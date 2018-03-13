x=input()
a=''
b=list(x)
for i in range(0,len(b),2):
    temp=b[i];
    b[i]=b[i+1]
    b[i+1]=temp
print(''.join(b)) 
