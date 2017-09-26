class Node:
    def __init__(self,key):
        self.value=key
        self.left=None
        self.right=None
class BST:
    def __init__(self,key):
        self.head=Node(key)
    def insert(self,parent,node):
        if(parent.value>node.value):
            if(parent.left is None):
                parent.left = node
            else :
                self.insert(parent.left,node)
        else :
            if(parent.right is None):
                parent.right =node
            else:
                self.insert(parent.right,node)
    def inorder(self,parent):
        if parent:
            self.inorder(parent.left)
            print(parent.value)
            self.inorder(parent.right)
    def preorder(self,parent):
        if parent:
            print(parent.value)
            self.preorder(parent.left)
            self.preorder(parent.right)
    def postorder(self,parent):
        if parent:
            self.postorder(parent.left)
            self.postorder(parent.right)
            print(parent.value)
    def minimum(self,parent):
        while(parent.left is not None):
            parent=parent.left
        print(parent.value)
    def maximum(self,parent):
        while(parent.right is not None):
            parent=parent.right
        print(parent.value)
    def successor(self,parent):
        if(self.head.right is None):
            return None
        if(parent.right is None):
            return None
        if(parent.right.left is None):
            return(parent.right)
        else:
            y=parent.right
            while(y.left is not None):
                y=y.left
            return(y.value)
    def predecessor(self,parent):
        if(self.head.left is None):
            return None
        if(parent.left.right is None):
            print(parent.left)
        else:
            y=parent.left
            while(y.right is not None):
                y=y.right
            return(y.value)
    def search(self,parent,node):
        if(parent is None):
            return parent
        if(parent.value==node.value):
            return parent
        if(parent.value>node.value):
            return self.search(parent.left,node)
        else:
            return self.search(parent.right,node)
    def delete(self,parent,node):
        temp=self.search(self.head,node)
        if(self.search(self.head,node) is None):
            print("enter a valid Node to be deleted")
            return
        else:
            if(temp.left is None and temp.right is None):
                temp=None
                return
            if(temp.left is None and temp.right is not None):
                temp.value=temp.right.val
                temp.right=None
                return
            if(temp.left is not None and temp.right is None):
                temp.value=temp.left.val
                temp.left=None
                return
            if(temp.left is not None and temp.right is not None):
                y=self.successor(node)
                self.delete(self.head,Node(y))
                temp.value=y
                return


                
            
y=BST(10)
y.insert(y.head,Node(20))
y.insert(y.head,Node(5))
y.insert(y.head,Node(1))
y.insert(y.head,Node(6))

y.insert(y.head,Node(14))
y.insert(y.head,Node(15))
y.insert(y.head,Node(16))
y.insert(y.head,Node(13))
y.insert(y.head,Node(30))
y.insert(y.head,Node(7))


y.minimum(y.head)
y.maximum(y.head)
print(y.successor(y.head))
print(y.predecessor(y.head))
print(y.search(y.head,Node(14)))
y.delete(y.head,Node(5))
