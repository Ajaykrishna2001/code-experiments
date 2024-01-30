'''year=int(input())
if(((year%4==0) and ((year%400==0)or(year%100!=0))
    print("leap year")
else:
    print("notleap year")
double=lambda x:x*2
print(double(10))'''
 #reverse a string
'''
def reverse(str):
    str=str[::-1]
    return str
str=input("entr strng")
print(reverse(str))'''

#to reverse a sentence

def reverse_sentence(sentence):
    # Split the sentence into individual words
    words = sentence.split()
    
    # Reverse the order of the words
    reversed_words = words[::-1]
    
    # Join the reversed words back together
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# Example usage
sentence = "Hello, how are you today?"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)'''
# to find vowels and consonents
'''
sentence = input("entr the sentnc:")
string=sentence.lower()
print(string)
count =0
list1=["a","e","i","o","u"]
for char in string:
    if char in list1:
        count=count+1
print("vowels in sentnc:",count)'''

#to find duplicate numbers
'''
def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return duplicates

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 10, 11, 11, 13, 14, 15, 15]
duplicates = find_duplicates(numbers)
print(duplicates)'''
'''
#in index method
list1=["amul",1,2,2,4,5,6,5]
list2=[i for i in range(len(list1)) if list1[i]==5]
print(list2)'''

#to print common elemnt not present in secnd array
'''
x=[11,22,33,'_07']
y=['_07',33,22,45]
z=[]
for i in x:
    if i in y:
        z.append(i)
print("the common elemnt:",z)'''
'''
'''
#to reverse an array
def reverse_array(arr):
    # Initialize two pointers
    start = 0
    end = len(arr) - 1

    # Swap elements from start and end until they meet in the middle
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr
# Test the function
arr = [1, 2, 3, 4, 5]
reversed_arr = reverse_array(arr)
print(reversed_arr)'''
'''
#sort given array
def sort_array(arr):
    arr.sort()
    return arr
array=[4,2,1,3,5]
sorted_array=sort_array(array)
print(sorted_array)'''




