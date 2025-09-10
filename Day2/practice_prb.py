
# prg 1

import itertools
numbers=[1,2,3]
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            print(numbers[i],numbers[j],numbers[k])
        print()

# prg-2
# print even index

str=input('enter a string')
print(str[::2])

# prg 3
# count of each element

str=intput('enter a str ')
for i in str:
    print(str.count(i))
