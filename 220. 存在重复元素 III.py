class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False

        dist = t + 1

        def get_bucket_id(num, dist=dist):
            return (num + 1) // dist - 1 if num < 0 else num // dist

        bucket = {}
        for i in range(n):
            num = nums[i]
            bucket_id = get_bucket_id(num)
            if bucket_id in bucket:
                return True
            if (bucket_id - 1) in bucket:
                if abs(bucket[bucket_id - 1] - num) <= t:
                    return True
            if (bucket_id + 1) in bucket:
                if abs(bucket[bucket_id + 1] - num) <= t:
                    return True
            bucket[bucket_id] = num
            if i >= k:
                del bucket[get_bucket_id(nums[i - k])]

        return False


# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

# 如果存在则返回 true，不存在返回 false。

# 示例 1：

# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true
# 示例 2：

# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true
# 示例 3：

# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false
