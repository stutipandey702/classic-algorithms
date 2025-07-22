#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name: scheduling problem - greedy
Author: Stuti Pandey

"""


# import statements
import sys


def schedule(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: x[1])

    num_scheduled = 0
    last_end = 0 # the latest end time

    for start, end in sorted_jobs:
        if start >= last_end:
            num_scheduled += 1
            last_end = end
            
    return num_scheduled


def main():
    
    numInstances = int(input())
    outputs = []
    for i in range (numInstances):
        jobs = []
        numJobs = int(input())
        for i in range(numJobs):
            job_list = input().split(" ")
            job_int_tup = tuple(int(job.strip()) for job in job_list)
            jobs.append(job_int_tup)
        outputs.append(schedule(jobs))
    
    for output in outputs:
        print(output)

    


if __name__ == "__main__":
    main()