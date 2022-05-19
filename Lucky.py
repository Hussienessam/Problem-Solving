testcases_count = int(input())
testcases = []
for i in range(testcases_count):
    testcase = input()
    testcases.append(testcase)
results = []

for testcase in testcases:
    first_part = int(testcase[0]) + int(testcase[1]) + int(testcase[2])
    second_part = int(testcase[3]) + int(testcase[4]) + int(testcase[5])
    if first_part == second_part:
        results.append('YES')
    else:
        results.append('NO')

for result in results:
    print(result)