def left_shift_array(arr, n, k):
    if k >= n:
        for i in range(n):
            arr[i] = 0
        return arr
    for i in range(n - k):
        arr[i] = arr[i + k]
    for i in range(n - k, n):
        arr[i] = 0

    return arr
N = 5
K = 2
arr = [10, 20, 30, 40, 50]

result = left_shift_array(arr, N, K)
print(result)