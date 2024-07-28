#trying with an object, instead of a list 
# accuracy, latency, throughput 

'''
class BenchmarkStore:
    def __init__(self, model_id, metric):
        self.benchmarks = {self.model_id, self.metric}

    def add_benchmark(self, model_id, metric):
        if self.model_id in self.benchmarks:
            print("benchmark already exists")
            return
        self.benchmarks[model_id] = metric
        return
    def get_benchmark(self, model_id, metric):
        if self.model_id in self.benchmarks:
            print("the metric for ${model_id} is", self.benchmarks.get(metric))
            return self.benchmarks[model_id]
        else:
            print("this model_id doesn't exist")
            return


benchmark = {}'''

from flask import Flask 
class BenchmarkStore:
    def __init__(self):
        self.benchmarks = {}

    def add_benchmark(self, model_id, metric):
        if model_id in self.benchmarks:
            print("Benchmark already exists for this model.")
            return
        self.benchmarks[model_id] = metric
        print(f"Added benchmark for model {model_id}: {metric}")

    def get_benchmark(self, model_id):
        if model_id in self.benchmarks:
            print(f"The metric for model {model_id} is {self.benchmarks[model_id]}")
            return self.benchmarks[model_id]
        else:
            print("This model_id doesn't exist")
            return None

# Example usage:
store = BenchmarkStore()
store.add_benchmark("model_1", {"accuracy": 0.95, "latency": 100})
store.add_benchmark("model_2", {"accuracy": 0.92, "latency": 110})
store.get_benchmark("model_1")
store.get_benchmark("model_2")
