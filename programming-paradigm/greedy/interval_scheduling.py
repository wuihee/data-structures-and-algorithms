"""
Interval Scheduling Problem

Given a list of jobs, where each job has a start and finish time, find the
maximum number of mutually compaitble jobs.
"""

from collections import namedtuple


def interval_scheduling(jobs: list) -> list:
    """
    Return an array which contains the max number of compaitble jobs.

    Parameters
    ----------
    jobs : An array of jobs which contain start and finish times.
    """

    # Give the attributes 'start' and 'finish' via namedtuple for every job.
    Job = namedtuple('Job', ['start', 'finish'])
    jobs = [Job(i[0], i[1]) for i in jobs]

    # Edge Cases: If number of jobs <= 1.
    n = len(jobs)
    if n <= 1:
        return jobs

    # Sort jobs by their finish time in ascending order.
    jobs.sort(key=lambda x: x.finish)

    # Start by choosing the first job which has the earliest finish time.
    prev_job = jobs[0]
    chosen_jobs = [jobs[0]]

    # Greedy Choice: Choose job with the earliest finish time that starts after
    # the previous job finishes. Repeat until no more jobs can be chosen.
    for i in range(1, n):
        curr_job = jobs[i]
        if curr_job.start >= prev_job.finish:
            chosen_jobs.append(curr_job)
            prev_job = curr_job

    return chosen_jobs
