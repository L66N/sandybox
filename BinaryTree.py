#Find sum of the Binary tree
from itertools import count



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def theSum(self, root):
        if not root:
            return 0
        return root.val + self.theSum(root.left) + self.theSum(root.right)

#Find minimum node in tree

class TreeNode:
    def __init__(self, val):
        self.val = val

class Solution:
    def theMin(self, root):
        if not root:
            return min(min_left, min_right)
        else:

            min_left = self.theMin(root.left)
            min_right = self.theMin(root.right)
            return min(root.val, min_left, min_right)

#Tree is symmetric

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        def isMirror(self, t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False

            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        return isMirror(root.left, root.right)


#Count leaves on tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leaves(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return self.leaves(root.left) + self.leaves(root.right)

#Max depth of the tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
