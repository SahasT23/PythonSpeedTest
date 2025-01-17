import numba 
import numpy as np

@numba.njit
def lcs(a, b):
  dp = np.zeros((len(a) + 1, len(b) + 1), dtype=np.int32)
  for i in range(1, len(a) + 1):
    for j in range(1, len(b)+ 1):
      if a[i - 1] == b[j -1]:
        dp[i, j] = dp[i - 1, j - 1] + 1
      else:
        dp[i, j] = max(dp[i - 1, j], dp[i, j - 1])
    return dp[-1, -1]
  
  # Have to be careful with the JIT compiler, only in certain scenarios