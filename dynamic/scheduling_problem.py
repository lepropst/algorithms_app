import pandas as pd
from utility.job import job


def get_predecessor(job, l: list[job]):
    if len(l) > l.index(job) - 1:
        return l[l.index(job) - 1]
    return None


def schedule_jobs(jobs: pd.DataFrame, machines=8):
    machines = [[]]
    availableMachines = pd.DataFrame(data=machines, columns=["machines"])
    print(availableMachines)
    print(jobs)
