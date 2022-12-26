from typing import List

from test_framework import generic_test, test_utils


def q1003(input_set: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
    return []


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "q1003.py", "q1003.tsv", q1003, test_utils.unordered_compare
        )
    )
