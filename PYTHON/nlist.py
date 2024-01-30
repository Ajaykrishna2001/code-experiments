'''n_list =[ "Happy",[2,0,1,5]]
print(n_list[0][4])
print(n_list[1][3])
print(n_list[4.1])'''

'''my_list=['a','e','i','o','u']
print(my_list[-1])
print(my_list[-5])

my_list=['p','e','d','r','o','p','m']
my_list.remove('p')
print(my_list)
print(my_list.pop(1))
print(my_list)
my_list.clear()
print(my_list)'''

'''for name in (1,2,3,4,5,6):
    print('HELLOW',name)'''

'''a=int(input())
for i in range (0,a):
    for j in range (i+1):
        print('$' ,end="")
    print("\n")
for i in range (a+1,0,-1):
    for j in range(i-1):
        print("#",end="")
    print("\n")'''

def pypart2(n):
    k=2*n-2
    for i in range (0,n):
        for j in range(0,k):
            print(end="")
        k=k-2
        for j in range(0,i+1):
            print("&",end="")
        print("\r")
n=5
pypart2(n)

