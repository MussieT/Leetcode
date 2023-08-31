def sliding_window(nums: list[int], k: int):

    result = []
    window = sum(nums[:k])

    print("window is: ", window)
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k] 
        # print("window: ", window)
        print("i: ", nums[i])
        print(nums[i - k])

sliding_window([1, 2, 3, 5, 7, 1], 3)
