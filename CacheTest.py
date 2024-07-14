import time
import sys
sys.setrecursionlimit(10**9)

from functools import cache

@cache
def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
start = time.time()
print(fibonacci(35))
end = time.time()

print(end-start)

# recursive process right now
# made faster by becoming an iterative process
# but we can use caching instead, more memory is used, but it is very fast, can use LRU instead