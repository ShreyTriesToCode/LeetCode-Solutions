def validateBST(root):
    def helper(node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True
        val = node.val
        if val <= min_val or val >= max_val:
            return False
        return (helper(node.left, min_val, val) and 
                helper(node.right, val, max_val))

    return helper(root)