import sys

def get_min(numbers):
    min = sys.maxsize
    for number in numbers:
        if int(number) < min:
            min = int(number)
    return min

testcases_count = int(input())
testcases = []
for i in range(testcases_count):
    number = input()
    testcase = input()
    testcases.append(testcase)
results = []

for testcase in testcases:
    numbers = testcase.split(' ')
    min_number = get_min(numbers)
    sum = 0
    for number in numbers:
        if int(number) != min_number:
            sum += int(number) - int(min_number)
    results.append(sum)
        
for result in results:
    print(result)