testcases_count = int(input())
testcases = []
for i in range(testcases_count):
    test_case_info = input()
    count = int(test_case_info.split(' ')[0])
    testcase = []
    for i in range(count):
        word = input()
        testcase.append(word)
    testcases.append(testcase)
results = []

def get_difference(chars):
    asciis = []
    sum = 0
    for char in chars:
        asciis.append(ord(char))
        sum += ord(char)
    middle = sum / len(asciis)
    middle = min(asciis, key=lambda x:abs(x-middle))
    sum_differences = 0
    for char in chars:
        if ord(char) >= middle:
            sum_differences += ord(char) - middle
        else:
            sum_differences += middle - ord(char)
    return sum_differences

for testcase in testcases:
    sum = 0
    outputs = []
    for i in range(0, len(testcase[0])):
        chars = []
        for word in testcase:
            chars.append(word[i])
        outputs.append(get_difference(chars))
        print(outputs)
    results.append(min(outputs))

for result in results:
    print(result)