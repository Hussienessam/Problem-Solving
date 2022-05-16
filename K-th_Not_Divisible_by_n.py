testcases_count = int(input())
testcases = []
for i in range(testcases_count):
    testcase = input()
    testcases.append(testcase)
results = []
for testcase in testcases:
    n = int(testcase.split(' ')[0])
    k = int(testcase.split(' ')[1])
    i = 0
    counter = 0
    result = 0
    while True:
        if i % n != 0:
            counter += 1
            result = i
        if counter == k:
            results.append(result)
            break
        i += 1
for result in results:
    print(result)
