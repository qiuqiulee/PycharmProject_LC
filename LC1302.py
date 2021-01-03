# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        row = [root]
        while row:
            new_row = []
            for node in row:
                if node.left:
                    new_row.append(node.left)
                if node.right:
                    new_row.append(node.right)
            if new_row:
                row = new_row
            else:
                return sum([n.val for n in row])


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    import io
    # def readlines():
    #     for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
    #         yield line.strip('\n')

    # lines = readlines()
    # while True:
    #     try:
    #         line = next(lines)
    root = stringToTreeNode('[1,2,3,4,5,null,6,7,null,null,null,null,8]');

    ret = Solution().deepestLeavesSum(root)

    out = str(ret);
    print(out)
        # except StopIteration:
        #     break


if __name__ == '__main__':
    main()