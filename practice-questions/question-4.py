#creating a job 

class Job:
    def __init__(self, name, runtime, status):
        self.name = name
        self.runtime = runtime
        self.status = status

    def __repr__(self):
        return f"Job({self.name}, runtime={self.runtime}, status={self.status})"

class MergeSort:
    def __init__(self, jobs):
        self.jobs = jobs

    def merge_sort(self):
        if len(self.jobs) > 1:
            mid = len(self.jobs) // 2
            left_half = self.jobs[:mid]
            right_half = self.jobs[mid:]

            left_sorter = MergeSort(left_half)
            right_sorter = MergeSort(right_half)

            left_sorter.merge_sort()
            right_sorter.merge_sort()

            i = j = k = 0

            while i < len(left_sorter.jobs) and j < len(right_sorter.jobs):
                if left_sorter.jobs[i].runtime < right_sorter.jobs[j].runtime:
                    self.jobs[k] = left_sorter.jobs[i]
                    i += 1
                else:
                    self.jobs[k] = right_sorter.jobs[j]
                    j += 1
                k += 1

            while i < len(left_sorter.jobs):
                self.jobs[k] = left_sorter.jobs[i]
                i += 1
                k += 1

            while j < len(right_sorter.jobs):
                self.jobs[k] = right_sorter.jobs[j]
                j += 1
                k += 1

    def __repr__(self):
        return f"MergeSort({self.jobs})"


    


class Queue(Job):
    def __init__(self):
        self.jobs = []
    
    def enqueue(self, job):
        self.jobs.append(job)

    def dequeue(self):
        self.jobs.pop(0)
        return True
    
    def is_empty(self):
        return len(self.jobs) == 0
    
class Stack(Job):
    def __init__(self):
        self.jobs = []

    def push(self,job):
        self.insert(0,job)

    def pop(self):
        self.jobs.pop(0)
        return True
    
    def is_empty(self):
        if len(self.jobs) == 0:
            return True