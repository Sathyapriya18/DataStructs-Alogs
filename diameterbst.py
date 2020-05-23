class Node :
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class Solution:
 def diameterOfBinaryTree(self,root):
    self.ans = 1

    def depth(node):
        if not node: return 0
        L = depth(node.left)
        R = depth(node.right)
        self.ans = max(self.ans, L + R + 1)
        return max(L, R) + 1

    depth(root)
    return self.ans - 1



root=Node(1)
print(Solution.diameterOfBinaryTree(Solution,root))




