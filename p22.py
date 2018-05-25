N=int(input())
K=int(input())
l=[]
m=[]
for i in range(1,N+1):
  if(N//i>=1):
    l.append(i)
    

for j in range(1,K+1):
  if(K//j>=1):
    m.append(j)
    

a=max(l)
b=max(m)
if(a in m):
  print(a)
elif(b in l):
  print(b)
else:
  print("error")
