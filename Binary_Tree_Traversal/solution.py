# Pre-order traversal
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(node):
    if node is None:
        return []

    result = [node.data]
    left_side = pre_order(node.left)
    right_side = pre_order(node.right)
    return result + left_side + right_side

    # In-order traversal
def in_order(node):
    if node is None:
        return []

    result = [node.data]
    left_side = in_order(node.left)
    right_side = in_order(node.right)
    return left_side + result + right_side

    # Post-order traversal
def post_order(node):
    if node is None:
        return []

    result = [node.data]
    left_side = post_order(node.left)
    right_side = post_order(node.right)
    return left_side + right_side + result
