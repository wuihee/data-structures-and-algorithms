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

Loop Invariant: The stack always contains the LIS of A[:i]
    1. Initialization: At A[:0], stack is empty as there is not LIS.
    2. Maintenance: At each iteration, the element is either added to the stack
                    or it replaces the smallest element larger than it.
                    Assuming stack contains LIS for A[:i - 1], adding an
                    element at A[:i] will undoubtedly yield the LIS. However,
                    if an element in the stack is replaced instead,
    3. Termination: When the loop terminates, i becomes len(A) - 1. Thus, the
                    stack contains the LIS from [0:n].

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
