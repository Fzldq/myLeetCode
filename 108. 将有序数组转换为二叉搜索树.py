class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def build(left, right):
            if left > right:
                return None
            mid = (left + right + 1) >> 1
            rootval = nums[mid]
            root = TreeNode(rootval)
            if left == right:
                return root
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        left, right = 0, len(nums) - 1
        return build(left, right)
