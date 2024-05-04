from mark.Mark import Mark

class Node:
    def __init__(self, mark):
        self.mark = mark
        self.left = None
        self.right = None
        self.height = 1

class MarkBST:
    def insert_node(self, root, mark):
        if mark.score == None: 
            mark.score = -1
        if not root:
            return Node(mark)
        elif mark.score < root.mark.score:
            root.left = self.insert_node(root.left, mark)
        else:
            root.right = self.insert_node(root.right, mark)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balanceFactor = self.get_balance(root)
        if balanceFactor > 1:
            if mark.score < root.left.mark.score:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balanceFactor < -1:
            if mark.score > root.right.mark.score:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    def find_min(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current.mark

    def find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current.mark

    def inorder_traversal(self, root, reverse=False):
        if root:
            if reverse:
                self.inorder_traversal(root.right, reverse)
                if root.mark.score == -1:
                    root.mark.score = None
                if root.mark.score != None:
                    root.mark.print_score()
                self.inorder_traversal(root.left, reverse)
            else:
                self.inorder_traversal(root.left, reverse)
                if root.mark.score == -1:
                    root.mark.score = None
                if root.mark.score != None:
                    root.mark.print_score()
                self.inorder_traversal(root.right, reverse)

    def create_tree(self, mark_list):
        if not mark_list:
            return None
        
        root = None
        for (roll, subject), score in mark_list.items():
            mark = Mark(roll, subject, score)
            if root is None:
                root = Node(mark)
            else:
                root = self.insert_node(root, mark)
        return root
    
    def create_tree_student(self, roll, mark_list):
        if not mark_list:
            return None
        
        root = None
        for subject, score in mark_list.items():
            mark = Mark(roll, subject, score)
            if root is None:
                root = Node(mark)
            else:
                root = self.insert_node(root, mark)
        return root
    
    def create_tree_subject(self, subject, mark_list):
        if not mark_list:
            return None
        
        root = None
        for roll, score in mark_list.items():
            mark = Mark(roll, subject, score)
            if root is None:
                root = Node(mark)
            else:
                root = self.insert_node(root, mark)
        return root
