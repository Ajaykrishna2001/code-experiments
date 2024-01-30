#palindrome in string
'''
string =input("Enter the string")
if(string==string[::-1]):
    print("It is palindrome")
    
else:
    print("It is not palindrome")'''
    
    
    
    
'''s=input("entr string")
if(s==s[::-1]):
    print("crct")
else:
    print("wrong")'''
 #to remove char
'''
def remove(string,char):
    return string.replace(char,"")
my_string="hello,world!"
charto_remove="l"
result=remove(my_string,charto_remove)
print(result)'''
'''
#count occurence
def count_occurrences(string, char):
    return string.count(char)

# Example usage:
my_string = "Hello, World!"
character_to_count = "l"
count = count_occurrences(my_string, character_to_count)
print(count)  # Output: 2'''
'''
#count occurence
def countchars(string):
    chars = {}
    for char in string:
        if char in chars:
            chars[char]+=1
        else:
            chars[char]=1
    return chars
string ="ethernet"
chars=countchars(string)
for char,count in countchars("ethernet").items():
    print(f"{char}:{count}")'''
    
#to print longest word
'''
def Longestwordlength(string):
    l=0
    w=''
    words = string.split()
    for word in words:
        if (len(word)>1):
            w=word
            l=len(word)
    return(w,l)
string = input("enter string:")
w,l=Longestwordlength(string)
print("longest word is:",w)
print("length of longest word is ",l)'''

#to reverse a string
'''
def reverse(string):
    reversed_string=""
    for i in string:
        reversed_string=i+reversed_string
    print("reversed",reversed_string)
string = input("enter a string:")
print("entered string",string)
reverse(string)'''
   



   
   
   
   
   
   
   
   
   
   
   
    
    
    
    
    
    
    