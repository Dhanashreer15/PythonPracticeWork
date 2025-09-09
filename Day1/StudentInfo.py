#challenge 1

'''
def details():
    print('Student Name:',name+',','Age:',age+',','Grade:',grade)

name=input('enter the name ')
age=int(input('enter the age '))
grade=input('enter the grade ')
details()

'''

# shopping cart

'''
item1=int(input('enter price of item1 '))
item2=int(input('enter price of item2 '))
item3=int(input('enter price of item3 '))
sum=item1+item2+item3
finalsum=sum
if(sum>100):
    discount=sum//10
    finalsum=sum-discount

print('Cart Total:',sum,'\n'+'Discount Applied:',discount,'\n'+'Final Total:',finalsum)

'''

# odd/even checker


'''
def checker(num):
    if(num%2==0):
        print('Number',num,'is even')
    else:
        print('Number',num,'is odd')

num=int(input('enter the value'))
checker(num)

'''

# Temperature Converter

'''
def c_to_f():
    F=temp1*(9/5)+32
    print(f"{temp1}*C = {F:.2f}*F")

def f_to_c():
    C=(temp2-32)*(5/9)
    print(f"{temp2}*F = {C:.2f}*C")

temp1=25
temp2=100
c_to_f()
f_to_c()


'''

# ch 5: calculator

'''
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    if(n1>n2):
        return n1-n2
    else:
        return n2-n1

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

n1=int(input('enter number1 :'))
n2=int(input('enter number2 :'))

print('Add:',add(n1,n2))
print('Subtract:',sub(n1,n2))
print('Multiply:',mul(n1,n2))
print('Divide:',div(n1,n2))

'''

# ch6 - bank acc simulation
'''

def deposit(amount):
    global balance
    balance=balance+amount
    print('Deposit',amount,'-> Balance:',balance)

def withdraw(amount):
    global balance
    if(balance>amount):
        balance=balance-amount
        print('Withdraw',amount,'-> Balance:',balance)
    else:
        print('Withdraw',amount,'-> Insufficient funds! Balance:',balance)


balance=1000
deposit(1000)
withdraw(500)
'''

# ch 7 

'''
n = int(input("Enter number1: "))
m = int(input("Enter number2: "))
product = n * m
i = 1
perfectsquare = False
while i * i <= product:
    if i * i == product:
        perfectsquare = True
        break
    i = i + 1
if perfectsquare:
    print("yes")
else:
    print("no")
 
'''

# ch 8

'''
num1=int(input('enter number1:'))
num2=int(input('enter number2:'))

sum=num1+num2
if(sum%2==0):
    print('even')
else:
    print('odd')

    

'''
# ch 10
    
'''

list1=list(map(int,input('enter list values').split()))[:10]
print(min(list1))

'''
# ch 11

'''

size=int(input('enter size'))
list1=list(map(int,input('enter list values ').split())) [:size]

min=min(list1)
max=max(list1)

for i in list1:
    if(i==min):
        print(i)
        

for i in list1:
    if(i==max):
        print(i)
    
'''
    

# ch 12

'''
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1==0 or n2==0:
    print(-1)
else:
    i=1
    gcd=1
    while i<=n1 and i<=n2:
        if n1%i ==0 and n2%i ==0:
            gcd=i
        i=i+1
    print(gcd)
 '''

#  ch 13
'''
num=int(input("Enter a number: "))
sum=0
i=1
while i<=num:
    sum=sum+i
    i=i+1
print(sum)
'''
 
 
 
#  ch 14
 
'''
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 > n2 and n1 < n3:
    print("yes")
else:
    print("no")
'''