def max_product(nums):
    if len(nums) < 2:
        return None

    nums.sort()

    return nums[-1] * nums[-2]

nums1 = [1, 2, 3, 4, 5]
print(max_product(nums1))

nums2 = [-1, -2, -3, -4, -5]
print(max_product(nums2))

nums3 = [-5, -4, 1, 2, 3]
print(max_product(nums3))