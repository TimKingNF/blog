import random

big_list = []
for i in range(0, 1000000):
    j = random.randint(0, 10)
    big_list += [i] * j

print("len big_list ", len(big_list))


class Solution:
    @profile
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        i = 1
        max_id = 0
        max_val = nums[max_id]
        while i < length:
            if nums[i] > max_val:
                max_id += 1
                max_val = nums[i]
                nums[max_id] = nums[i]
            i += 1
        return max_id + 1


print(len(big_list[:Solution().removeDuplicates(big_list)]))
