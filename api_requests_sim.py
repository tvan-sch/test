import numpy as np
import random

random.seed(10)
nr_of_new_api_requests = 10


def generate_api_requests(n):
    new_api_requests = np.array([])
    for i in range(n):
        y = random.randint(1,100)
        new_api_requests = np.append(new_api_requests, y)

    return new_api_requests


def brute_force_get_api_requests(api_requests: np.ndarray):
    highest_priority_api_request = np.argwhere(api_requests == api_requests.min())[0]
    api_requests = np.delete(api_requests, highest_priority_api_request)
    return api_requests

