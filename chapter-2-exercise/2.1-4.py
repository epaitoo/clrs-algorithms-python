def linear_search(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return None