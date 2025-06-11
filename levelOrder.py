from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def levelOrder(self,root):
        if not root:
            return []
        
        result=[]
        queue=deque([root])

        while queue:
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
    
def buildTree(values):
    if not values or values[0] is None:
        return None
    
    root=TreeNode(values[0])
    queue=deque([root])
    i=1

    while queue and i<len(values):
        node=queue.popleft()
        if i < len(values):
            left_val=values[i]
            if left_val is not None:
                node.left=TreeNode(left_val)
                queue.append(node.right)
            i +=1

        if i<len(values):
            right_val=values[i]
            if right_val is not None:
                node.right=TreeNode(right_val)
                queue.append(node.right)
            i +=1
    return root


input=[3,9,20,None,None,15,7]
root=buildTree(input)

sol=Solution()
print(sol.levelOrder(root))



