def solution(N):
    nums = [True] * (N + 1)

    for i in range(2, len(nums) // 2 + 1):
        if nums[i]:
            for j in range(i + i, N + 1, i):
                nums[j] = False
    return len([i for i in range(2, N + 1) if nums[i]])