class Solution:

    def traversal(self, root: TreeNode) -> List[int]:
        if node is not None:
            #--- state S0 ---#
            out.append(node.val)  # move this line to different state to get different order traversal
            traversal(node.left)
            #----------------#
			
            #--- state S1 ---#
            travelsal(node.right)
            #----------------#
			
            #--- state S2 ---#
            return
            #----------------#

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [(root, 'S0')]
        out = []
        while stack:
            node, state = stack.pop()
            if node is not None:
                if state == 'S0':  # initial state
                    out.append(node.val)
                    stack.append((node, 'S1'))
                    stack.append((node.left, 'S0'))
                if state == 'S1':
                    stack.append((node, 'S2'))
                    stack.append((node.right, 'S0'))
                if state == 'S2':
                    pass  # ending state
        return out

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [(root, 'S0')]
        out = []
        while stack:
            node, state = stack.pop()
            if node is not None:
                if state == 'S0':  # initial state
                    stack.append((node, 'S1'))
                    stack.append((node.left, 'S0'))
                if state == 'S1':
                    out.append(node.val)
                    stack.append((node, 'S2'))
                    stack.append((node.right, 'S0'))
                if state == 'S2':
                    pass  # ending state
        return out

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [(root, 'S0')]
        out = []
        while stack:
            node, state = stack.pop()
            if node is not None:
                if state == 'S0':
                    stack.append((node, 'S1'))
                    stack.append((node.left, 'S0'))
                if state == 'S1':
                    stack.append((node, 'S2'))
                    stack.append((node.right, 'S0'))
                if state == 'S2':
                    out.append(node.val)
        return out
