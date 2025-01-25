# -------- Min Heap methods : ----------

import heapq
minheap = []
heapq.heappush(minheap,23)
heapq.heappush(minheap,12)
heapq.heappush(minheap,9)
heapq.heappush(minheap,2)
heapq.heappush(minheap,10)
heapq.heappush(minheap,6)
print('heappush = ',minheap)
print(minheap[0])
print(heapq.heappop(minheap))
print(minheap[0])


# convert list to heap
nums = [6,56,75,12,4,90]
heapq.heapify(nums)
print(nums)
heapq.heapreplace(nums,33)
print(nums)


# Arranging tasks in order - using minheap :

tasks = []
heapq.heappush(tasks,(7,"task1"))
heapq.heappush(tasks,(5,"task2"))
heapq.heappush(tasks,(2,"task3"))
print("tasks = ",tasks)

while tasks:
    p,t = heapq.heappop(tasks)
    print(f"priority = ",p,", tasks = ",t)
    