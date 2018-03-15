y=input("Enter any String:")
a=[0]*256
maxi=-1
for x in y:
	a[ord(x)]+=1
for x in y:
	if maxi<a[ord(x)]:
		ans=x
print(ans)
