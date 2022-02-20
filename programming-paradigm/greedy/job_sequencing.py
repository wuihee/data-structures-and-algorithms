"""
Job Sequencing Problem

Given a series of jobs which have deadlines and associated profits, find the
jobs to complete to give a maximum possible profit. Each job takes one unit
of time to complete. Deadlines refer to the number of days from 0 the job needs
to be completed by.
"""

from collections import namedtuple


def job_sequencing(deadlines, profits):
    """
    Select jobs to return the maximum possible profit.

    Paramters
    ---------
    deadlines : The ith job can be complete latest at deadlines[i].
    profits : profits[i] is the profit for the ith job.
    """

    # Initialize jobs[...(deadline, profit)...]
    # Sort by profit in descending order.
    n = len(deadlines)
    Job = namedtuple('Job', ['deadline', 'profit'])
    jobs = [Job(deadlines[i], profits[i]) for i in range(n)]
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Initialize a scheduler for the jobs.
    schedule = [None for _ in range(max(deadlines))]

    # Greedy Choice: Take the available job with the highest profit and
    # complete it as late as possible.
    for i in range(n):

        # If schedule is already filled, exit the loop.
        if all(schedule):
            break
    
        # -1 because of 0-based indexing.
        curr_job = jobs[i]
        latest_deadline = curr_job.deadline - 1

        # For all available deadlines if deadline is occupied keep moving down
        # until empty slot is found. If no slots are found, skip current job.
        for j in range(latest_deadline, -1, -1):
            if not schedule[j]:
                schedule[j] = curr_job
                break

    # Return maximum profit.
    return sum([j.profit for j in schedule])
