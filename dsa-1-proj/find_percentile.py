# by Magomedov Rustam

from math import ceil
from time import time
from random import randint

def find_percentile(a:list, b:list, p:int) -> int:
    """
    Finds the p-th percentile of the combined sorted list of a and b.
    param a: list, a list of integers
    param b: list, a list of integers
    param p: int, a percentile between 0 and 100
    returns: int, the percentile of the sorted combined list. for p=50 returns the median rounded to the nearest lowest integer
    """
    c = []
    i = 0
    j = 0
    
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i < len(a):
        c.extend(a[i:])
    if j < len(b):
        c.extend(b[j:])

    rank = ceil(p/100 * len(c))

    # binary search
    left = 0
    right = len(c) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == rank - 1:
            return c[mid]
        elif mid < rank - 1:
            left = mid + 1
        else:
            right = mid - 1

def test_find_percentile(a, b, p, correct_answer):
    "Tests the find_percentile function"
    start_time = time()
    answer = find_percentile(a, b, p)
    end_time = time()
    if answer == correct_answer:
        print(f"Passed.\n \tExpected: {answer}\n\tGot: {correct_answer}")
    else:
        print(f"Wrong answer obtained: {answer}. The correct answer is {correct_answer}")
        raise AssertionError(f"Unit test failed. a={a}, b={b}, expected={correct_answer}, got {answer}")
    print(f"\tSolution runtime: {end_time - start_time}\n")

def run_unit_tests():
    "Runs unit tests for the find_percentile function"
    # test 1
    a = [1,2,7,8,10]
    b = [6,12]
    p = 50
    correct_answer = 7
    test_find_percentile(a, b, p, correct_answer)

    # test 2
    a = [1,2,7,8]
    b = [6,12]
    p = 50
    correct_answer = 6
    test_find_percentile(a, b, p, correct_answer)

    # test 3
    a = [15,20,35,40,50]
    b = []
    p = 30
    correct_answer = 20
    test_find_percentile(a, b, p, correct_answer)

    # test 4
    a = [15,20]
    b = [25,40,50]
    p = 40
    correct_answer = 20
    test_find_percentile(a, b, p, correct_answer)

    # test 5
    a = [15,20,35,40, 50]
    b = [10, 25, 30, 45, 55, 60, 65]
    p = 90
    correct_answer = 60
    test_find_percentile(a, b, p, correct_answer)

    # test 6
    a = [1,2,3]
    b = [5,6]
    p = 100
    correct_answer = 6
    test_find_percentile(a, b, p, correct_answer)

    # test 7
    a = [1,2,3]
    b = [5,6]
    p = 1
    correct_answer = 1
    test_find_percentile(a, b, p, correct_answer)

    # test 8
    a = [0]
    b = [1,2,3]
    p = 1
    correct_answer = 0
    test_find_percentile(a, b, p, correct_answer)

    # test 9
    a = [5, 50]
    b = [1, 100, 200]
    p = 100
    correct_answer = 200
    test_find_percentile(a, b, p, correct_answer)

def run_stress_test(seconds:int):
    "Runs a stress test for the specified number of seconds"
    start_time = time()
    while time() - start_time < seconds:
        a = sorted([randint(1, 1000) for _ in range(100)])
        b = sorted([randint(1, 1000) for _ in range(100)])
        p = randint(1, 100)
        c = sorted(a + b)
        correct_answer = c[ceil(p/100 * len(c)) - 1]
        test_find_percentile(a, b, p, correct_answer)

def run_max_test(size:int):
    "Runs a test with len(a)=len(b)=size"
    a = sorted([randint(1, 1000) for _ in range(size)])
    b = sorted([randint(1, 1000) for _ in range(size)])
    p = randint(1, 100)
    start_time = time()
    find_percentile(a,b,p)
    end_time = time()
    print(f"Max test passed.\n \tMax test runtime: {end_time - start_time}")

if __name__ == "__main__":
    run_unit_tests()
    run_stress_test(5)
    run_max_test(150000)