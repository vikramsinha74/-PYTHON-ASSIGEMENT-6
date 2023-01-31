# 1. Create a function to print your name using Python.

# def printName(name) :
#     print(f'My name is {name}')
# printName('Debopriya das')

##########################################################

# 2. Write a program to add two integers using function.

# def addTwo(x=0,y=0) :
#     return x+y
# print(addTwo(7,9))

##########################################################

# 3. Create a function to multiply two numbers and the numbers should pass as parameter
# and return the result.

# def Multiply(x=1,y=1) :
#     return x*y
# print(Multiply(4,8))

##########################################################

# 4. Write a Python program to access a function inside a function.

# def fun1() :
#     desc='This is Function 1'
#     def fun2() :
#         desc='This is Function 2'
#         return desc
#     return fun2()
# res = fun1()
# print(res)

# def test(a):
#     def add(b):
#         nonlocal a
#         return a+b
#     return add
# func= test(4)
# print(func(4))

##########################################################

# 5. Write a Python program to understand the use of and variables
# declared in a function.

# n=5
# def useVars() :
#     m=8
#     global n
#     n+=2
#     print(m)
#     print(n)
#     def inner() :
#         x=9
#         nonlocal m
#         m+=1
#         print(m)
#     inner()
# useVars()

##########################################################

# 6. Write a Python program to understand the use of asterisk(*) character declared in a
# function.

# def addAll(*nums) :
#     sum = 0
#     for i in nums :
#         sum+=i
#     return sum
# res=addAll(2,3,4,5)
# print(res)

##########################################################

# 7. Write a Python program to understand the use of double asterisk(*) character declared
# in a function.

# def getNameAge(**studs) :
#     for i in studs :
#         print(f'{i} is {studs[i]} years old')
# getNameAge(Aman=20,suman=30)

##########################################################

# 8. Create a function to calculate and return LCM of two numbers.

# def getLcm(x,y) :
#     if x>y :
#         higher = x
#     else :
#         higher = y
#     value=higher
#     while True :
#         if(higher % x)==0 and (higher % y)==0 :
#             return higher
#         else :
#             higher+=value
# res = getLcm(24,36)
# print(res)

##########################################################

# 9. Create a function to calculate and return HCF of two numbers.

# def getHcf(x,y) :    ##Euclid's algorithm
#     if y==0 :
#         return x
#     else :
#         return getHcf(y,x%y)

# print(getHcf(64,48))

##########################################################

# 10. Write a Python function to find the max of three numbers.

# 
def findMax(x,y,z) :
#     if x>y :
#         if x>z :
#             return x
#         else :
#             return z
#     else :
#         if y>z :
#             return y
#         else :
#             return z
# res=findMax(11,45,26)
# # print(res)

##########################################################

# 11. Write a Python function to sum all the numbers in a list.

# l=[10,20,30,40,50]
# def getSum(ls) :
#     sum=0
#     for i in ls :
#         sum+=i
#     return sum
# print(getSum(l))

##########################################################

# 12. Write a Python function to multiply all the numbers in a list

# l=[1,2,3,4,5]
# def getSum(ls) :
#     res=1
#     for i in ls :
#         res*=i
#     return res
# print(getSum(l))

##########################################################

# 13. Write a Python program to reverse a string.

# def getReverse(s) :
#     if s=='' :
#         return s
#     else :
#         return s[-1]+getReverse(s[:-1])
# print(getReverse('MCA'))

##########################################################

# 14. Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

# def getFact(n): 
#     if n==1 :
#         return 1
#     else :
#         return n*getFact(n-1)
# print(getFact(int(input('Enter a number: '))))

##########################################################

# 15. Write a Python function to check whether a number falls in a given range.

# def checkInRange(n) :
#     s=20
#     e=80
#     if n>=s and n<=e :
#         return True
#     else :
#         return False
# print('Range: 20 to 80')
# print(checkInRange(int(input('Enter a number: '))))

##########################################################

# 16. Write a Python function that accepts a string and calculate the number of upper case
# letters and lower case letters.

# def getCountOfUpperAndLower(s) :
#     upperCount=0
#     lowerCount=0
#     for i in s :
#         if ord(i) in range(65,91) :
#             upperCount+=1
#         elif ord(i) in range(97,123) :
#             lowerCount+=1
#     return upperCount,lowerCount
# print(getCountOfUpperAndLower('aAabcD'))

##########################################################

# 17. Write a Python function that takes a list and returns a new list with unique elements of
# the first list.

# def getUniqueValues(l) :
#     s = set(l)
#     nwl = list(s)
#     return nwl
# print(getUniqueValues([10,50,20,10]))

##########################################################

# 18. Write a Python function that takes a number as a parameter and check the number is
# prime or not.

# def checkPrime(n) :
#     for i in range(2,n):
#         if n%i==0 :
#             return False
#     else :
#         return True
# print(checkPrime(int(input('Enter a number: '))))

##########################################################

# 19. Write a Python program to print the even numbers from a given list.

# def printEvenNums(l) :
#     for i in l :
#         if i%2==0 :
#             print(i)
# printEvenNums([13,18,4,21])

##########################################################

# 20. Write a Python function to check whether a number is perfect or not.

# def checkPerfectNum(n) :
#     sum=0
#     i=1
#     while i<n :
#         if n%i==0 :
#             sum+=i
#         i+=1
#     else :
#         if sum==n :
#             return True
#         else : 
#             return False
# print(checkPerfectNum(int(input("Enter a number: "))))

##########################################################

# 21. Write a Python function that checks whether a passed string is palindrome or not.

# def checkPalindrome(s) :
#     if s=='' :
#         return True
#     else :
#         if s[0]==s[-1] :
#             return True and checkPalindrome(s[1:-1])
#         else :
#             return False
# print(checkPalindrome('abcba'))

##########################################################

# 22. Write a Python function to create and print a list where the values are square of
# numbers between 1 and 30 (both included)

# def printSquares() :
#     nwl=[]
#     for i in range(1,31) :
#         nwl.append(i**2)
#     return nwl
# res=printSquares()
# print(res)

