import sys

from bisect import bisect_right # using python library


def find_latest_non_conflict(jobs):

    # uses binary search to find latest job index with no conflicts


    start_times = [job[1] for job in jobs]  # sort by ending time

    p = []


    for i in range(len(jobs)):


        idx = bisect_right(start_times, jobs[i][0]) - 1

        p.append(idx if idx < i else -1)

   

    return p



def schedule(jobs):

    # max weight computing

    jobs.sort(key=lambda x: x[1])  # Sort jobs by end time to process them in order

    p = find_latest_non_conflict(jobs)

    

    n = len(jobs)


    dp = [0] * (n + 1) # dp array, where each entry is the the max weight of a series of jobs up till index n

    

    for i in range(1, n + 1):

        # dichotomy of whether to include or exclude job

        include = jobs[i - 1][2] + (dp[p[i - 1] + 1] if p[i - 1] != -1 else 0) 

        exclude = dp[i - 1]

        dp[i] = max(include, exclude)

    

    return dp[n]



def main():


    numInstances = int(input())


    results = []


    for _ in range(numInstances):


        jobs = []

        numJobs = int(input())

        for i in range(numJobs):

            job_list = input().split(" ")

            job_int_tup = tuple(int(job.strip()) for job in job_list)

            jobs.append(job_int_tup)


        # print(jobs)

        results.append((str) (schedule(jobs)))

    

    for result in results:

        print(result)



if __name__ == "__main__":

    main()
