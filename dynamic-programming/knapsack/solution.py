def Solution(tasks: list, A: int, B: int, priority: list) -> int:
    n = len(tasks)
    
    # Initialize the 3D DP array
    dp = [[[0 for _ in range(B+1)] for _ in range(A+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        ai = tasks[i-1][0]
        bi = tasks[i-1][1]
        pi = priority[i-1]
        
        for j in range(A+1):
            for k in range(B+1):
                # If the task can be accommodated
                if ai <= j and bi <= k:
                    dp[i][j][k] = max(dp[i-1][j][k], pi + dp[i-1][j-ai][k-bi])
                else:
                    dp[i][j][k] = dp[i-1][j][k]    
    return dp[n][A][B]


if __name__ == "__main__":
    tasks = [(1, 2), (3, 2), (4, 5), (3,3)]
    A = 6
    B = 8
    priority = [5,6,7,7]

    print(Solution(tasks, A, B, priority))  # This should output the maximum achievable priority.




