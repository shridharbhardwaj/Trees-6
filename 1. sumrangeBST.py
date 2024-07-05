# Time and Space complexity:
# Time complexity: O(n)
# Space complexity: O(n) | worst: O(h)
# Approach: we check the range condition at the root only, if root > high, we will goto left subtree and vice-versa

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        # Initialize sum
        range_sum = 0

        # If the current node's value is within the range, add it to the sum
        if low <= root.val <= high:
            range_sum += root.val

        # Recursively check the left and right subtree
        if root.val > low:
            range_sum += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            range_sum += self.rangeSumBST(root.right, low, high)

        return range_sum

