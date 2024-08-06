""" Test algorithms"""

from algorithms import find_coins_greedy, find_min_coins
import timeit

CHANGES = [0, 1, 3, 8, 12, 23, 57, 8000, 40023]
DELIM = f"\n{'-'*80}\n"
TEST_NUMBER = 100


def test_algoritms(change):
    """Print test results"""
    time_greedy = timeit.timeit(lambda: find_coins_greedy(change), number=TEST_NUMBER)
    time_dynamic = timeit.timeit(lambda: find_min_coins(change), number=TEST_NUMBER)

    res = DELIM
    res += f"For {change = }:\n"
    res += "\nResults:\n"
    res += f"Greedy algorithm:\t{find_coins_greedy(change)}\n"
    res += f"Dynamic programming:\t{find_min_coins(change)}\n"
    res += "\nTime:\n"
    res += f"Greedy algorithm:\t{time_greedy}\n"
    res += f"Dynamic programming:\t{time_dynamic}\n"
    res += f"Greedy / Dynamic:\t{round(time_greedy/time_dynamic,2)} / 1\n"
    res += DELIM
    return res


if __name__ == "__main__":
    for change in CHANGES:
        print(test_algoritms(change))
