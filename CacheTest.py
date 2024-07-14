# recursive process right now
# made faster by becoming an iterative process
# but we can use caching instead, more memory is used, but it is very fast, can use LRU instead

import time
import sys
import tracemalloc
from functools import cache

sys.setrecursionlimit(10**9)

@cache
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Start tracing memory allocations
tracemalloc.start()

start = time.time()
result = fibonacci(35)
end = time.time()

# Get memory usage information
current, peak = tracemalloc.get_traced_memory()

# Stop tracing memory allocations
tracemalloc.stop()

print(f"Result: {result}")
print(f"Time taken: {end - start:.12f} seconds")
print(f"Current memory usage: {current / 10**6:.6f} MB")
print(f"Peak memory usage: {peak / 10**6:.6f} MB")
