"""
Sum of Subsets

Given a list of numbers and a given mumber m, find the subset of integers such
that the sum of the subset is exactly equal to m.
"""


def sum_of_subsets(numbers, m, pos, current_nums, remaining_sum):
    """
    Main recursive function to solve the sum of subsets problem.

    Parameters
    ----------
    numbers : List of numbers given by the problem.
    m : Number which subset must add up to.
    pos : The index which indicates the current number the current call is at.
    current_sum : The current sum of the subset so far.
    remaining sum : The remaining sum of all numbers that haven't been chosen. 
    """

    current_sum = sum(current_nums)

    # Base Case: Subset if found.
    if current_sum == m:
        return True

    # Base Case: Subset will not be found.
    if pos >= len(numbers) or current_sum + remaining_sum < m:
        return False

    # Try including the current number.
    remaining_sum -= numbers[pos]
    current_nums.append(numbers[pos])
    if sum_of_subsets(numbers, m, pos + 1, current_nums, remaining_sum):
        return current_nums

    # Backtrack: Don't include current number
    current_nums.pop()
    if sum_of_subsets(numbers, m, pos + 1, current_nums, remaining_sum):
        return current_nums

    return False


numbers = [5, 10, 12, 13, 15, 18]
m = 30
print(sum_of_subsets(numbers, m, 0, [], sum(numbers)))
