"""Find the maximum sum of a subarray in an array."""


def max_subarray(A, low, high):
    """
    Paramters
    ---------
    A : Array of positive and negative integers.
    low : Index position of lower bound of array.
    high : Index position of upper bound of array.
    """

    # Base case.
    if low == high:
        return low, high, A[low]

    # Recursively find the maximum subarrays in the left and right halves.
    # Also find the maximum subarray across the midpoint in O(n).
    mid = low + (high - low) // 2
    left_low, left_high, left_sum = max_subarray(A, low, mid)
    right_low, right_high, right_sum = max_subarray(A, mid + 1, high)
    cross_low, cross_high, cross_sum = max_cross(A, low, mid, high)

    # Return the index bounds and maximum sum of either left, right, or cross.
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def max_cross(A, low, mid, high):
    """
    Find the maximum sum across the middle of the array.

    Paramters
    ---------
    A : Array of positive and negative integers.
    low : Index position of lower bound of array.
    mid : Index position of the middle of the array.
    high : Index position of upper bound of array.
    """

    # Find the largest sum on the left side from the middle to index 0.
    left_sum = -float('inf')
    total = 0
    for i in range(mid, low - 1, -1):
        total += A[i]
        if total >= left_sum:
            left_sum = total
            left_max = i

    # Find the largest sum on the right side from the middle to the end.
    right_sum = -float('inf')
    total = 0
    for j in range(mid + 1, high + 1):
        total += A[j]
        if total >= right_sum:
            right_sum = total
            right_max = j

    # Return left and right bounds and the total sum.
    return left_max, right_max, left_sum + right_sum
