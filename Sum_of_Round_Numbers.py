def is_round(number):
    if len(number) > 1:
        bin = ''
        for i in range(len(number) - 1):
            bin += '0'
        if number[1:] == bin:
            return True
        else:
            return False
    else:
        return False

testcases_count = int(input())
testcases = []
for i in range(testcases_count):
    testcase = input()
    testcases.append(testcase)
results = []

for testcase in testcases:
    result = ''
    counter = 0
    divider = '10'
    if is_round(testcase):
        results.append(1)
        results.append(testcase)
    else:
        for char in testcase:
            if char != '0':
                num = int(testcase) % int(divider)
                result += str(num) + ' ' 
                testcase = str(int(testcase) - num)
                counter += 1
            divider += '0'
        results.append(counter)
        results.append(result)
    
for result in results:
    print(result)
    