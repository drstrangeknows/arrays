# Python3 program to convert a given Binary Tree to Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    # A simple recursive function to convert a given
    # Binary tree to Doubly Linked List
    # root --> Root of Binary Tree
    # head --> Pointer to head node of created doubly linked list
    root, head = None, None

    def BToDll(self, root):
        if root is None:
            return

        # Recursively convert right subtree
        self.BToDll(root.right)

        if root is not None:
            print("Cur Root ->", root.data)

        if self.head is not None:
            print("Cur Head-> ", self.head.data)
        # Insert root into doubly linked list
        # As both right and left are done for a Node,
        # root changes to prev, so this line serves to
        # link the right pointer of the root to the just finished node
        # e.g. for 9 as both right and left finishes, root changes to 8
        # this line links right pointer of 8 to the head i.e. 9,
        # we are constructing the LL from end
        root.right = self.head

        # Change left pointer of previous head, this line links
        # left of the cur head to the root and thus establishes
        # doubly LL characteristic
        if self.head is not None:
            self.head.left = root

        # Change head of doubly linked list
        # once doubly LL is achieved then change
        # bhhi the head of LL
        self.head = root

        # Recursively convert left subtree
        self.BToDll(root.left)

    @staticmethod
    def print_list(head):
        print('Extracted Double Linked list is:')
        while head is not None:
            print(head.data, end=' ')
            head = head.right

        # Driver program to test above function


if __name__ == '__main__':
    """ 
    Constructing below tree 
          5 
        // \\ 
        3   6 
      // \\  \\ 
      1   4    8 
    // \\    // \\ 
    0   2    7   9 
    """
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(4)
    tree.root.right.right = Node(8)
    tree.root.left.left.left = Node(0)
    tree.root.left.left.right = Node(2)
    tree.root.right.right.left = Node(7)
    tree.root.right.right.right = Node(9)

    tree.BToDll(tree.root)
    tree.print_list(tree.head)

