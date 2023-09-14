def sliding_window(nums: list[int], k: int):

    window = sum(nums[:k])

    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k] 

sliding_window([1, 2, 3, 5, 7, 1], 3)
