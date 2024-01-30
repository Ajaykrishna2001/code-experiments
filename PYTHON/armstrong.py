'''
n=int(input())
m=n
ans=0#153
while(n>0):
    n1=int(n%10) #3,15%10=5
    ans=n1*n1*n1+ans#125+27=153
    n=int(n/10)#1
print(m,ans)
if(m==ans):
    print("armstrong")
else:
    print("not")'''
'''
date=input("enter date")
given_date=date.replace("/","")
reversed_date=given_date[::-1]
if given_date==reversed_date:
    print(date,"is palindrome")
else:
    print(date,"is not palindrome")'''


day=input("entr date")
month=input("entr month")
year=input("entr year")

givendate=day+month+year
reversedate=givendate[::-1]
if reversedate==givendate:
    print("palindrome")
else:
    print("not palindrome")