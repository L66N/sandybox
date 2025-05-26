from fontTools.misc.cython import returns

nums = [1,6,5,2,8,3]
n = len(nums)

for i in range(0, n-1):
    for j in range(0, n-1-i):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

print(nums)