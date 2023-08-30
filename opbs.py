def optimal_bst(keys, freq):
    n = len(keys)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(n):
        dp[i][i+1] = freq[i]
    
    for length in range(2, n+1):
        for i in range(n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + sum(freq[i:j]))
    
    return dp[0][n]

def main():
    keys = input("Enter keys separated by spaces: ").split()
    freq = list(map(float, input("Enter corresponding probabilities: ").split()))

    if len(keys) != len(freq):
        print("Number of keys and probabilities must be the same.")
        return

    cost = optimal_bst(keys, freq)
    print("Minimum average search time:", cost)

if __name__ == "__main__":
    main()