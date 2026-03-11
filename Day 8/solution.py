##Hitchhiker's Guide 🪐

def minimum_components(components):
    target = 42
    
    # DP array
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    
    for num in components:
        for i in range(target, num - 1, -1):
            dp[i] = min(dp[i], dp[i - num] + 1)
    
    return dp[target] if dp[target] != float('inf') else -1
