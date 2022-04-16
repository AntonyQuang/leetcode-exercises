def two_sum(nums: list, target: int):
    output = []
    for i in range(len(nums)):
        new_nums = nums.copy()
        number_2 = target - nums[i]
        new_nums.remove(nums[i])
        if number_2 in new_nums:
            output.append(i)
    print(f"Answer: {output}")


two_sum(nums=[2, 7, 11, 15], target=9)

two_sum(nums=[3, 2, 4], target=6)

two_sum(nums=[3, 3], target=6)
