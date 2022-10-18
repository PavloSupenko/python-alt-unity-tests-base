from pprint import pprint
import yaml


def add_subtests_to_order_list(testData, testsList: list):
    testsList.append(f"{testData['test']}::test_enter")

    if 'subtests' in testData:
        subtests = testData['subtests']
        for subtest in subtests:
            add_subtests_to_order_list(subtest, testsList)

    testsList.append(f"{testData['test']}::test_exit")


def convert_tests_order_file_to_list(filename: str):
    with open(filename) as testsOrderFile:
        testsOrder = yaml.safe_load(testsOrderFile)

    testsList = []

    for test in testsOrder:
        add_subtests_to_order_list(test, testsList)

    return testsList


tests = convert_tests_order_file_to_list('tests.yml')
pprint(tests)
