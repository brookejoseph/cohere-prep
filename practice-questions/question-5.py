import time 

class Benchmark:
    def __init__(self, name, runtime, status):
        self.name = name 
        self.runtime = runtime
        self.status = status

    def Running(self):
        self.status = "Running"
        time.sleep(self.runtime)
        self.status = "Completed"


class Operations(Benchmark):
    def __init__(self):
        self.benchmarks = [] #elements of type benchmark

    def add_benchmark(self, benchmark):
        self.benchmarks.append(benchmark)

    def list_benchmark(self):
        if(len(self.benchmarks) == 0):
            print("No benchmarks added")
            return
        
        for benchmark in self.benchmarks:
            print("benchmark",  benchmark.name, benchmark.runtime, benchmark.status)

    def run_benchmark(self, benchmark):
        Benchmark(benchmark.name, benchmark.runtime, benchmark.status).Running()
        print("the status of the benchmark is", benchmark.status)





