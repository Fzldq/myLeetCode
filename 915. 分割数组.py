class Solution:
    def partitionDisjoint(self, A) -> int:
        left_max = cur_max = A[0]
        idx = 0
        for i in range(len(A)):
            if A[i] >= cur_max:
                cur_max = A[i]
            if A[i] < left_max:  # 比[0, idx]的最小值小
                idx = i  # 更新到当前位置
                left_max = cur_max
        return idx + 1


# 给定一个数组 A，将其划分为两个不相交（没有公共元素）的连续子数组 left 和 right， 使得：
# left 中的每个元素都小于或等于 right 中的每个元素。
# left 和 right 都是非空的。
# left 要尽可能小。
# 在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。

# 示例 1：

# 输入：[5, 0, 3, 8, 6]
# 输出：3
# 解释：left = [5, 0, 3]，right = [8, 6]
