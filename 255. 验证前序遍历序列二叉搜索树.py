class Solution:
    def verifyPreorder(self, preorder) -> bool:
        if not preorder:
            return True
        stack, root = [], float("-inf")
        for i in range(len(preorder)):
            if preorder[i] < root:
                return False
            while (stack and preorder[i] > stack[-1]):
                root = stack.pop()
            stack.append(preorder[i])
        return True


# 给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。
# 你可以假定该序列中的数都是不相同的。
# 示例 1：
# 输入: [5,2,6,1,3]
# 输出: false
