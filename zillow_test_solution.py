class Node(object):  # Please do not remove or rename any of this code
    """Represents a single node in the Ternary Search Tree"""
    def __init__(self, val, parent=None):
        self.val = val
        self.left = None
        self.mid = None
        self.right = None
        self.parent = parent
    
    def is_root(self):
        return not self.parent
    
    def is_lc(self):
        '''is node a left child'''
        return self.parent and self.parent.left == self
    
    def is_rc(self):
        '''is node a right child'''
        return self.parent and self.parent.right == self
    
    def is_mc(self):
        '''is node a mid child'''
        return self.parent and self.parent.mid == self
    
    def num_of_child(self):
        '''how many child does node have'''
        n_c = 0
        if self.left:
            n_c += 1
        if self.right:
            n_c += 1
        if self.mid:
            n_c += 1
        return n_c
    

    
class Tree(object):  # Please do not remove or rename any of this code
    """The Ternary Search Tree"""
    def __init__(self):
        self.root = None
        self.size = 0

    # Please complete this method.
    """Inserts val into the tree. There is no need to rebalance the tree."""
    def insert(self, val):
        self.size += 1
        if self.root: 
            # call _insert() recursively
            self._insert(val, self.root)
        else: # empty tree
            self.root = Node(val)
    
    def _insert(self, val, current):
        if val < current.val: # go to left
            if current.left:
                self._insert(val, current.left)
            else:
                current.left = Node(val, parent=current)
        elif val == current.val: # go to mid
            if current.mid:
                self._insert(val, current.mid)
            else:
                current.mid = Node(val, parent=current)
        else: # go to right
            if current.right:
                self._insert(val, current.right)
            else:
                current.right = Node(val, parent=current)

                
    
    def _search(self, val, current):
        '''locate one instance of val'''
        if not current:
            return None
        if current.val == val:
            return current
        elif val < current.val:
            return self._search(val, current.left)
        else:
            return self._search(val, current.right)
        
        
    # Please complete this method.
    """Deletes only one instance of val from the tree.
       If val does not exist in the tree, do nothing.
       There is no need to rebalance the tree."""
    def delete(self, val):
        '''
        delete an instance of val in the tree
        there are four major scenarios, the node to be removed:
        I. has 0 child
        II. has 1 child
        III. has 2 children, this is the trickiest part
        IV. has 3 children
        
        Each scenarios can be furthuer divided into several cases
        '''
        if not self.root: # empty tree
            return
        
        if self.size == 1: # tree only has a root
            if self.root.val == val:
                self.root = None
                self.size = 0
            else:
                return
        
        node_to_delete = self._search(val, self.root)        
        if node_to_delete: # if there is an instance of val, then delete
            self.remove(node_to_delete)
            self.size -= 1
        else:
            return
        
    
    def remove(self, node):
        '''
        remove a node from the tree
        pay attention to cases where node is the root
        '''
        # Case I, leaf node
        # simply remove the node from the tree and update node relations
        if node.num_of_child() == 0:
            if node.is_lc(): # sub case, node is a left chid
                node.parent.left = None
            else: # node is a right child
                node.parent.right = None
        
        # Case II, node to removed has one child
        elif node.num_of_child() == 1:
            if node.left: # II.1 node has a left child
                if node.is_lc(): # II.1.1 node is a left child
                    node.parent.left = node.left
                    node.left.parent = node.parent
                elif node.is_rc(): # II.1.2 node is a right child. note that under our _search scheme
                     # node won't be a mid child. other cases are similar
                    node.parent.right = node.left
                    node.left.parent = node.parent
                else: # II.2.3 node is the root
                    self.root = node.left
                    self.root.parent = None
                    
                    
            elif node.mid: # II.2 node has a mid child
                if node.is_lc(): # II.2.1 node is a left child
                    node.parent.left = node.mid
                    node.mid.parent = node.parent
                elif node.is_rc(): # II.2.2 node is a right child
                    node.parent.right = node.mid
                    node.mid.parent = node.parent
                else: # II.2.3 node is the root
                    self.root = node.mid
                    self.root.parent = None
                    
            else: # II.3 node has a right child
                if node.is_lc(): # II.3.1 node is a left child
                    node.parent.left = node.right
                    node.right.parent = node.parent
                elif node.is_rc(): # II.3.2 node is a right child
                    node.parent.right = node.right
                    node.right.parent = node.parent
                else: # II.3.3 node is the root
                    self.root = node.right
                    self.root.parent = None
            
        
        
        # Case III, node to removed has two children
        elif node.num_of_child() == 2:
            if node.left and node.mid: # III.1 node has left and mid children
                if node.is_lc(): # III.1.1 node is a left child
                    node.parent.left = node.mid
                    node.mid.parent = node.parent
                    node.mid.left = node.left
                    node.left.parent = node.mid
                elif node.is_rc(): # III.1.2 node is a right child
                    node.parent.right = node.mid
                    node.mid.parent = node.parent
                    node.mid.left = node.left
                    node.left.parent = node.mid
                else: # III.1.3 node is the root
                    self.root = node.mid
                    self.root.parent = None
                    self.root.left = node.left
                    node.left.parent = self.root


            elif node.right and node.mid: # III.2 node has right and mid children
                if node.is_lc(): # III.2.1 node is a left child
                    node.parent.left = node.mid
                    node.mid.parent = node.parent
                    node.mid.right = node.right
                    node.right.parent = node.mid
                elif node.is_rc(): # III.2.2 node is a right child
                    node.parent.right = node.mid
                    node.mid.parent = node.parent
                    node.mid.right = node.right
                    node.right.parent = node.mid
                else: # III.2.3 node is the root
                    self.root = node.mid
                    self.root.parent = None
                    self.root.right = node.right
                    node.right.parent = self.root

            else: # III.3 node has left and right children, the most challenging part
                  # replace the node with the minimum node in the right subtree, also delete 
                # the minimum node from the right subtree
                m_val = self.find_and_kill(node)
                node.val = m_val
        

        # Case IV, node to be removed has three children
        # remove node and promote its mid child to its place
        else:
            if node.is_lc(): # node is a left child
                node.parent.left = node.mid
                node.mid.parent = node.parent
                node.mid.left = node.left
                node.left.parent = node.mid
                node.mid.right = node.right
                node.right.parent = node.mid
            elif node.is_rc(): # node is a right child
                node.parent.right = node.mid
                node.mid.parent = node.parent
                node.mid.left = node.left
                node.left.parent = node.mid
                node.mid.right = node.right
                node.right.parent = node.mid
            else: # node is the root
                self.root = node.mid
                self.root.parent = None
                self.root.left = node.left
                node.left.parent = self.root
                self.root.right = node.right
                node.right.parent = self.root
                
            
        
    
    def find_and_kill(self, node):
        '''find the minimum node in the right subtree of node, return its val and 
        remove it from the right subtree'''
        target = node.right
        while target.left:
            target = target.left

        val = target.val

        # remove target from the tree
        # I. target has no child
        if target.num_of_child() == 0:
            if target.is_lc(): # I.1 target is a left child
                target.parent.left = None
            else: # I.2 target is a right child
                target.parent.right = None

        # II. target has one child
        elif target.num_of_child() == 1:
            if target.right: # II.1 target has a right child
                if target.is_lc(): # II.1.1 target is a left child
                    target.parent.left = target.right
                    target.right.parent = target.parent
                else: # II.1.2 target is a right child
                    target.parent.right = target.right
                    target.right.parent = target.parent

            else: # II.2 target has a mid child
                if target.is_lc(): # II.2.1 target is a left child
                    target.parent.left = target.mid
                    target.mid.parent = target.parent
                else: # II.2.2 target is a right child
                    target.parent.right = target.mid
                    target.mid.parent = target.parent

        # III. target has two children, must be mid and right child
        else:
            if target.is_lc(): # III.1 target is a left child
                target.parent.left = target.mid
                target.mid.parent = target.parent
                target.mid.right = target.right
                target.right.parent = target.mid
            else: # III.2 target is a right child
                target.parent.right = target.mid
                target.mid.parent = target.parent
                target.mid.right = target.right
                target.right.parent = target.mid

        return val

    

#the following codes are for testing

    def traversal(self):
        '''traversal of the tree'''
        self._inorder(self.root)
    
    def _inorder(self, current):
        '''asc order'''
        if current:
            self._inorder(current.left)
            self._inorder(current.mid)
            print(current.val)
            self._inorder(current.right)

import numpy as np

for t in range(100): # test 100 * 101 times
    toy = Tree()
    
    test_data = np.random.choice(range(t, t+30), 100) # 100 > 30 ensures test data contains 								#repeated numbers
                                                      # foecing some nodes in tree have three 								#children
    for x in test_data:
        toy.insert(x)
        
    for y in range(0, 101): # from no deletion to completely deletion
        del_data = np.random.choice(test_data, y)
        for x in del_data:
            toy.delete(x)
            
        toy.traversal()
