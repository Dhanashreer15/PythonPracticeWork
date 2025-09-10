# prb 1
'''
num=int(input('enter the number'))
n1=num%100
n2=num//100
sum=n1+n2
if(sum*sum==num):
    print(num,'Tech number')
else:
    print(num,'Not a Tech Number')

'''

# prb 2

'''
import math

def is_peterson_number(num):
    # Convert number to string to loop through digits
    digits = str(num)
    
    # Calculate sum of factorials of each digit
    factorial_sum = 0
    for digit in digits:
        factorial_sum += math.factorial(int(digit))
    
    # Check if the sum equals the original number
    return factorial_sum == num

# Test the function with some numbers
test_numbers = [145, 2, 40585, 123]
for number in test_numbers:
    if is_peterson_number(number):
        print(f"{number} is a Peterson Number ✅")
    else:
        print(f"{number} is NOT a Peterson Number ❌")

'''

# prg 3 
# sunny number

import math
num=int(input('enter the number :'))
n=num+1
sqrt=math.sqrt(n)
if(sqrt.is_integer()):
    print(sqrt.is_integer())
    print(num,'is a sunny number')
else:
    print(num,'is not a sunny number')


# prg 4
# spy number


num=int(input('enter the number'))
sum=0
mul=1
while(num>0):
    n=num%10
    sum=sum+n
    mul=mul*n
    num=num//10
print(sum)
print(mul)
if(sum==mul):
    print('It is spy number')
else:
    print('it is not a spy number')


# prg 5
# Neon number

num=int(input('enter the number'))
square=num*num
temp=square
sum=0
while(temp>0):
    n=temp%10
    sum=sum+n
    temp=temp//10

if(sum==num):
    print('It is neon number')
else:
    print('It is not neon number')



# prg 5

# prg 6
# Emirp number

num=int(input('enter the number'))
reverse=int(str(num)[::-1])
print(reverse)

def prime(n):
    if(n<2):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True

if(prime(num) and prime(reverse)):
    print('it is Emirp number')
else:
    print('it is not Emirp number')


# prg 7
# buzz number

num=int(input('enter the number'))
if(num%10==7 or num%7==0):
    print('It is buzz number')
else:
    print('It is not a buzz number')


# prg 8 
# Duck number

num=input('enter the number')
if(num[::-1]=='0'):
    print('It is not Duck number')
elif '0' in num:
    print('It is Duck number')
























