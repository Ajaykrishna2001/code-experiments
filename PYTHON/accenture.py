m=int(input("ENTER THE START VALUE"))
n=int(input("ENTER THE START VALUE"))
sums=0
for i in range(m,n+1):
    if i%3==0 and i%5==0:
        sums=sums+i
        print(i)
print(sums)
'''n=int(input("ENTER THE NUMBER"))
sums=0
for i in range(1,11):
    a=n*i
    sums=sums+a
print(sums)'''
# to avoid duplicate values
'''list=[1,2,3,3,4,4,5,6,6,7,7]
result=[]
for i in list:
    if i not in result:
        result.append(i)
print(result)'''

















