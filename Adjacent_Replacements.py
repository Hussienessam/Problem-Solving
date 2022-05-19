from cgi import test
from re import A


num = input()
input = input()
testcase_string = input.split(' ')
numbers = []

testcase = []
for i in testcase_string:
    testcase.append(int(i))
    
for i in testcase_string:
    if int(i) not in numbers:
        numbers.append(int(i))
    if int(i) % 2 == 0:
        if int(i) - 1 not in numbers:
            numbers.append(int(i) - 1)
    else: 
        if int(i) + 1 not in numbers:
            numbers.append(int(i) + 1)
   
numbers.sort()

for i in numbers:
    while i in testcase:
        index = testcase.index(i)
        if i % 2 == 0:
            testcase[index] = i - 1
        else: 
            testcase[index] = i + 1

for i in testcase:
    print(i)