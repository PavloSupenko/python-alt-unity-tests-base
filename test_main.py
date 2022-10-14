from datetime import datetime

testsOrderFile = open("tests.txt", "r")
testNames = testsOrderFile.read().split('\n')

print('Test names found:')
testNumber = 1
for testName in testNames:
    print(f"{testNumber}.{testName}")
    testNumber += 1

current_time = datetime.now().strftime("[%H:%M:%S]")
print("Current Time =", current_time)
