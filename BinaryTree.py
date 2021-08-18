# -*- coding: utf-8 -*-
'''Implementation of Binary tree node from Common Sense Guide
to Data Structures and Algorithms
'''
class TreeNode:
    
    # Node Constructor
    def __init__(self, value_, left = None, right = None):
        self.value = value_
        self.leftChild = left
        self.rightChild = right


class BinaryTree:
    def __init__(self, root_value = None):
        if root_value is None:
            self.root = None
        else:
            self.root = TreeNode(root_value)
    
    def search(self, value, node):
        # Base Case: Value is found or doesn't exist in Tree
        if node is None or node.value == value:
            return node
        
        elif value < node.value:
            # value is less than current node so search left
            return self.search(value, node.leftChild)
        else: #value > node.value so search right
            return self.search(value, node.rightChild)

    def insert(self, value, node):
        if value < node.value:
            # if left child is nonexistant then insert there
            if node.leftChild is None:
                node.leftChild = TreeNode(value)
            else:
                self.insert(value, node.leftChild)
        elif value > node.value:
            # if right child doesn't exist, insert there
            if node.rightChild is None:
                node.rightChild = TreeNode(value)
            else:
                self.insert(value, node.rightChild)
    
    def delete(self,valueToDelete, node):
        # base case is when we've hit the bottom of the tree
        # and the parent node has no children
        if node is None:
            return None
        
            # if vaue we're deleting is less or greater than the 
            # current node, set left or right child to be return
            # of recursive call of this method on current node's 
            # left or right sub tree
        elif valueToDelete < node.value:
            node.leftChild = self.delete(valueToDelete, node.leftChild)
            
            # return the current node (and it's subtree) to be used
            # as new node of it's parent's left or right child
            return node
        elif valueToDelete > node.value:
            node.rightChild = self.delete(valueToDelete, node.rightChild)
            return node
        
        elif valueToDelete == node.value:
            # this is the node we want to delete
            if node.leftChild is None:
                # left child is empty so just make right child the successor
                return node.rightChild
            elif node.rightChild is None:
                # right child is empty, so left is successor
                return node.leftChild
                # if both are empty then None is returned in first line
            
            else:
                node.rightChild = self.lift(node.rightChild, node)
                return node
            
        
    def lift(self, node, nodeToDelete):
        # if current node has left child, recursively call this
        # function to conditnue down the left subtree to 
        # find successor node
        if node.leftChild:
            node.leftChild = self.lift(node.leftChild, nodeToDelete)
            return node
        else:
            # if current node has no left child that means
            # the current node is the successor, and we make it's
            # value the value of the node we are deleting
            return node.rightChild
        
        
    def traverse_and_print(self, node):
        # print out tree
        if node is None:
            return
        self.traverse_and_print(node.leftChild)
        print(node.value)
        self.traverse_and_print(node.rightChild)
        
        


def main():
    vals = [50,25,75,10,33,56,89,4,11,30,40,52,61,82,95]
    bt = BinaryTree(vals[0])
    for val in vals:
        bt.insert(val,bt.root)
    print('Original Treee')
    bt.traverse_and_print(bt.root)
    
    print('Insert 73')
    bt.insert(73,bt.root)
    bt.traverse_and_print(bt.root)
    
    print('Delete 73')
    bt.delete(73, bt.root)
    
    print('Delete 52')
    bt.delete(52,bt.root)
    
    bt.traverse_and_print(bt.root)
    
    print('Find 10')
    print(bt.search(10,bt.root).value)
    
    
        
if __name__ == "__main__":
    # execute only if run as a script
    main()   
        
        
        