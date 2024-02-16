from api_requests_sim import *
import numpy as np
import time
import priority_queue
import heapq


def brute_force(sim_length=100000):
    """ Brute force implementation for finding the highest priority api request """
    global i, start, duration
    i = 0
    api_requests = np.array([])
    start = time.time()
    while i < sim_length:
        api_requests = np.append(api_requests, generate_api_requests(nr_of_new_api_requests))
        api_requests = brute_force_get_api_requests(api_requests)
        i += 1
    duration = time.time() - start
    print(f"brute force: {duration}")


def library_priority_queue(sim_length=100000):
    """
    Very optimized version of priority_queue (min-heap)
    """

    global start, i, nr_of_new_api_requests, p, duration
    start = time.time()
    i = 0
    api_requests_pq = []
    while i < sim_length:
        api_requests = generate_api_requests(nr_of_new_api_requests)
        for p in api_requests:
            heapq.heappush(api_requests_pq, p)
        heapq.heappop(api_requests_pq)

        i += 1
    duration = time.time() - start
    print(f"lib heapq  {duration}")


def student_priority_queue(sim_length=100000):
    """ This uses your own implementation of priority queue! """
    global start, i, nr_of_new_api_requests, p, duration
    start = time.time()
    i = 0
    api_requests_pq_custom = []
    while i < sim_length:
        api_requests = generate_api_requests(nr_of_new_api_requests)
        for p in api_requests:
            priority_queue.insert(api_requests_pq_custom, p)
        priority_queue.pop(api_requests_pq_custom)
        i += 1
    duration = time.time() - start
    print(f"custom min heap: {duration}")


sim_length = 1000
library_priority_queue(sim_length)

# Uncomment the line below to try your own minheap priority_queue implementation!
# student_priority_queue(sim_length)

brute_force(sim_length)

