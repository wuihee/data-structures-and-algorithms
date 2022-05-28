"""
494. Target Sum

You are given an integer array nums and an integer target. You want to build
an expression out of nums by adding one of the symbols '+' and '-' before each
integer in nums and then concatenate all the integers. Return the number of
different expressions that you can build, which evaluates to target.
"""

from functools import cache


def target_sum(nums, target):
    """
    Memoize backtracking approach.

    Paramters
    ---------
    nums : List of numbers to be considered.
    target : Sum that must be reached.
    """
    
    @cache
    def aux(total, i):
        """Return the number of ways to reach target."""

        n = len(nums)
        
        # Base case
        if i == n:
            if total == target:
                return 1
            else:
                return 0

        plus = aux(total + nums[i], i + 1)
        minus = aux(total - nums[i], i + 1)
            
        return plus + minus
    
    return aux(0, 0)
