#definig what a run class is 
class Run:
    def __init__(self, name, accuracy, latency, throughput):
        self.name = name 
        self.accuracy = accuracy
        self.latency = latency
        self.throughput = throughput
        self.jobs = []

    def input(self):
        self.jobs.append({self.name, self.accuracy, self.latency, self.throughput})
    def remove(self):
        self.jobs.pop()


class Sort(Run):
    def __init__(self):
        self.jobs = []
    def merge_sort(self):
        if len(self.jobs) > 1:
            half = len(self.jobs) / 2
            first_half = self.jobs[:half]
            second_half = self.jobs[half:]

            self.merge_sort(first_half)
            self.merge_sort(second_half)

            k = 0 

            while i < len(first_half) and j < len(second_half):
                if first_half[i] < second_half[j]:
                    self.jobs[k] = first_half[i]
                    i += 1
                else:
                    self.jobs[k] = second_half[j]
                    j += 1
                k += 1
        return

    
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1