#1 write a program to check whether a number is even or odd.
num=int(input("enter a numbe:"))
if(num%2==0):
   print("num is even")
else:
    print("num is odd")
#2 create a list of 5 numbers.print the square of each number.
num=[3,4,6,7,8] 
square=[x**2 for x in num]
print(square)
#3 create a function that checks a string is pallindr0me or not.
str=input("enter a string")
rev=str[::-1]
if(str==rev):
    print("str is pallindrom")
else: 
    print("str is not pallindrom")
#4 use a loop to print first 10 natural number.
i=1
while i<=10:
    print(i)
    i +=1   
