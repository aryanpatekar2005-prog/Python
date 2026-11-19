def right_shift_array(arr, K):
    n = len(arr)
    if K >= n:
        for i in range(n):
            arr[i] = 0
        return arr
    for i in range(n - 1, K - 1, -1):
        arr[i] = arr[i - K]

    for i in range(K):
        arr[i] = 0

    return arr

arr = [5, 10, 15, 20, 25]
K = 2
print(right_shift_array(arr, K))