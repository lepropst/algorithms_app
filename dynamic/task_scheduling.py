import datetime
from dateutil import parser

from utility.job import job


def schedule_jobs(jobs: list[job], machines=1):
    availableMachines = {}
    for mach in range(0, machines):
        availableMachines[mach] = []

    while jobs:
        jobs.sort(key=lambda x: x.start)
        current_job = jobs.pop(0)
        for idx, machine in enumerate(availableMachines):
            print(idx)
            print(machine)
            if machine[len(machine) - 1].finish < current_job.start:
                machine[len(machine) - 1].append(current_job)
                break
            else:
                if idx == len(availableMachines.keys()):
                    availableMachines[len(availableMachines.keys())] = [current_job]
                    break
                else:
                    continue
    for array in availableMachines:
        print(array)
