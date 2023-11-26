class job:
    id: str
    start: int
    finish: int
    benefit: int

    def __init__(self, id, start, finish, benefit):
        self.id = id
        self.start = start
        self.finish = finish
        self.benefit = benefit

    def __lt__(self, next):
        if next.start > self.start:
            return True
        if next.start == self.start:
            return self.benefit < next.benefit
        return False

    def __gt__(self, next):
        if next.start < self.start:
            return True
        if next.start == self.start:
            return self.benefit > next.benefit
        return False

    def __str__(self):
        return f"ID: {self.id}\tBenefit: {self.benefit}\n{self.start}-{self.finish}"
