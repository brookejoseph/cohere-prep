#sorting various benchmarks by a given metric 

#sort by time submitted

def sort_jobs_by_status(jobs):
    status_order = {"submitted": 0, "in-progress": 1, "completed": 2, "failed": 3}
    
    def get_status_order(job):
        return status_order[job["status"]]
    
    sorted_jobs = sorted(jobs, key=get_status_order)
    return sorted_jobs
jobs = [
    {"id": 1, "status": "completed"},
    {"id": 2, "status": "submitted"},
    {"id": 3, "status": "failed"},
    {"id": 4, "status": "in-progress"},
    {"id": 5, "status": "submitted"}
]

sorted_jobs = sort_jobs_by_status(jobs)

print(sorted_jobs)