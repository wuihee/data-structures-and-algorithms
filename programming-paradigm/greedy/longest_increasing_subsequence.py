"""
Find the longest increasing subsequence in an array.
Algorithm uses greedy approach and binary search.

Algorithm
    1. Loop through the array.
    2. If the stack is empty, or the current element is greater than the top
       most element, append to stack.
    3a. Greedy Move: Otherwise, find the index of the smallest element in the
        stack which is larger than the current element and replace it with
        current element.
    3b. This is done via binary search.
    4. The final length of the stack is the length of the LIS.

Time Complexity: O(nlog n)
"""

import bisect


def longest_increasing_subsequence(A: list[int]) -> int:
    stack = []
    for element in A:
        if not stack or stack[-1] < element:
            stack.append(element)
        else:
            idx = bisect.bisect_right(stack, element)
            stack[idx] = element

    return len(stack)


print(longest_increasing_subsequence([1, 7, 6, 2, 3, 9, 4, 6, 5]))
