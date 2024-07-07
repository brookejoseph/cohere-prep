#definition of a job
class Job:
    def __init__(self, name, runtime, status):
        self.name = name
        self.runtime = runtime
        self.status = status



# defining a benchmark class 
class Benchmark(Job):
    def __init__(self):
        self.jobs = []

    def add_job(self):
        self.jobs.append(Job)
        return True
    
    def remove_job(self):
        self.jobs.pop()
        return True


        


