#struct defining a job 
class Job:
    def __initit__(self, name):
        self.name = name
        self.time = 0
        self.status = "Not Started"



#struct for benchmarking 
class benchmark:
    def  __initit__(self, Job):
        self.job = Job
        self.time = 0
        self.status = "Not Started"
        self.result = "Not Available"

