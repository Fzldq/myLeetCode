class Solution:
    def removeDuplicates(self, nums) -> int:
        cnt, cur = 1, 1
        nl = len(nums)
        for i in range(1, nl):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                nums[cur] = nums[i]
                cur += 1
        return cur


# 给定一个排序数组，你需要在原地删除重复出现的元素，
# 使得每个元素最多出现两次，返回移除后数组的新长度。
# 不要使用额外的数组空间，
# 你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
