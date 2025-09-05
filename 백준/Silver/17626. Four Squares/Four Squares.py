import sys
import math

def main():
    n = int(sys.stdin.readline())
    dp = [0] + [4] * n
    sqrs = [i * i for i in range(1, math.isqrt(n) + 1)]
    
    for i in range(1, n+1):
        for j in sqrs:
            if j > i:
                break
            else:
                dp[i] = min(dp[i], dp[i - j] + 1)
                
    sys.stdout.write(str(dp[n]))
    
if __name__ == '__main__':
    main()