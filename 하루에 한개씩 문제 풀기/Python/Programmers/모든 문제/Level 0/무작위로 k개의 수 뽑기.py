def solution(arr, k):
    unique_nums = set()
    result = []

    for num in arr:
        if num not in unique_nums:
            unique_nums.add(num)
            result.append(num)

        if len(result) == k:
            break

    while len(result) < k:
        result.append(-1)

    return result
