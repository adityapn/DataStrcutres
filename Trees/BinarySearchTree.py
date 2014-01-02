import Queue
import math

class BinarySearchTree:
    
    class Node:
        left , right , value  = None , None , None
        def __init__(self,data):
            self.value = data
    root = None

    def add(self,data):        
        def add_into(node,data):
            if node is None:
                node = self.Node(data)
                node.left = None
                node.right = None            
            elif data <= node.value:
               node.left = add_into(node.left,data)
            else:
                node.right = add_into(node.right,data)
            return node
        self.root = add_into(self.root,data)
        
    def inorder(self):
        def inorder_trav(node):
            if node is not None:
                inorder_trav(node.left)
                print(node.value)
                inorder_trav(node.right)
        inorder_trav(self.root)

    def toList(self):
        items = []
        def getList(node):
            if node is not None:                
                getList(node.left)
                items.append(node.value)
                getList(node.right)
        getList(self.root)
        return items
        
        
    def preorder(self):
        def pre(node):
            if node is not None:
                print(node.value)
                pre(node.left)
                pre(node.right)
        pre(self.root)
        
    def postorder(self):
        li = []
        def post(node,li):
            if node is not None:
                post(node.left,li)
                post(node.right,li)
                li.append(node.value)
        post(self.root,li)
        print li

    def levelorder(self):
        queue = Queue.Queue()
        queue.put(self.root)
        while queue:
            try:
                temp = queue.get_nowait()
            except Exception:
                break
            print(temp.value)
            if temp.left is not None:
                queue.put(temp.left)
            if temp.right is not None:
                queue.put(temp.right)
                
    def reverseorder(self):
        queue = Queue.Queue()
        stack = []
        queue.put(self.root)
        while queue:
            try:
                temp = queue.get_nowait()
            except Exception:
                break
            stack.append(temp.value)
            if temp.left is not None:
                queue.put(temp.left)
            if temp.right is not None:
                queue.put(temp.right)
        while stack:
            print(stack.pop())


    def size(self):        
        def find_size(node,count):
            if node is None:
                return count
            count = count + 1                       
            count = find_size(node.left,count)                
            count = find_size(node.right,count)           
            return count
        return find_size(self.root,0)

    def height(self,node=root):
        def depth(node):
            if node is None:
                return 0
            return 1 + max(depth(node.left),depth(node.right))
        return depth(node)

    # Deepest left sub tree
    def left_deep(self):
        deep_left = self.height(self.root.left)
        return deep_left

    def minNode(self,Findnode=root):
       node = Findnode
       while node.left is not None:
           node = node.left
       return node.value

    def maxNode(self,Findnode=root):        
        node = Findnode
        while node.right is not None:
            node = node.right
        return node.value

    def isBalanced(self):
        if self.root.left is not None:
            left = self.height(self.root.left)
        if self.root.right is not None:
            right = self.height(self.root.right)
        if math.fabs(left-right) < 2:
            return True
        return False

    # Path from root to leafs
    def allPaths(self):
        def paths(node,path=""):
            if node is None:
                return
            if node.left is not None and node.right is not None:                
                path = path + str(node.value) + " -> "
            else:
                path = path + " -> "+str(node.value)
            if node.left is not None:
                paths(node.left,path)
            if node.right is not None:
                paths(node.right,path)

            if node.left is None and node.right is None:
                print path
        paths(self.root,"")

    # Sum of the path

    def findPathSum(self,findsum):
        def find(node,findsum,tempSum=0,path=""):
            if node is None:
                return
            
            tempSum += node.value
            if node.left is not None and node.right is not None:                
                path = path + str(node.value) + " -> "
            else:
                path = path +str(node.value)
            if tempSum == findsum:
                print "Found it with "+path
                return
            if node.left is not None:
                find(node.left,findsum,tempSum,path)
            if node.right is not None:
                find(node.right,findsum,tempSum,path)

        find(self.root,findsum)
        
    # Least / Lowest Common Ansistor
    def lca(self,left,right):
        def find_lca(node,leftVal,rightVal):
            if node is None:
                return
            if node.left is not None and node.right is not None:
                    if leftVal <= node.value and rightVal <= node.value:
                        return find_lca(node.left,leftVal,rightVal)
                    elif leftVal > node.value and rightVal > node.value:
                        return find_lca(node.right,leftVal,rightVal)
                    else:
                        return node.value
        value = find_lca(self.root,left,right)
        if value:
            print value
        else:
            print("Not found")

    def elementsThatFormSum(self,result):
        def get_elements(node,li=[]):
            if node is not None:
                get_elements(node.left)
                li.append(node.value)
                get_elements(node.right)
            return li
        elements = get_elements(self.root)
        start = 0
        end = len(elements)-1
        while start < end:
            Sum = elements[start]+elements[end]
            if Sum == result:
                print "Left "+str(elements[start])+" Right "+str(elements[end])
                break
            if Sum < result:
                start = start + 1
            elif Sum > result:
                end = end - 1
    # Longest path in the tree                
    def diameter(self):
        that = self
        def find_diameter(node):
            if node is None:
                return
            left = that.height(node.left)
            right = that.height(node.right)

            ldiameter = find_diameter(node.left)
            rdiameter = find_diameter(node.right)
            # left+right+1 passes through root and
            # ldiameter , rdiamter gives the one without passes through root
            return max((left+right+1),max(ldiameter,rdiameter))
        return find_diameter(self.root)

    def isBst(self):
        valid = True
        def isbst(node):
            if node is None:
                return
            if node.left.value <= node.value:
                isbst(node.left)
            else:
                valid = False
                return valid
            if node.right.value > node.value:
                isbst(node.right)
            else:
                valid = False
                return valid        
        try:
            return isbst(self.root)            
        except Exception:
            return True

    def findElement(self,number):
        def find(node,num):
            if node is None:
                return
            if num < node.value:
                find(node.left,num)
            elif num > node.value:
                find(node.right,num)
            else:
                print "Found"

        find(self.root,number)

    # Convers bst to Double linked list
    # Do bfs of the tree and add it to list to form double ll

    def bstToDoubleLL(self):
        queue = Queue.Queue()
        queue.put(self.root)
        doublell = [] # Consider as double linked list
        while queue:
            try:
                node = queue.get_nowait()
                doublell.append(node.value)
            except Exception:
                break
            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)
        print doublell

    # Binary Search Tree Successor for a given node
    # The immediete bigger value to the perticular node value is
    # it's successor , so which every is smaller value in the right sub tree is
    # successor , if there is no right sub tree then move towards ancestors for which
    # our node is left sub tree 
    # OR other way is do inorder and use binary search to find the elements
    # and next element will be successors
    
    def findSuccessor(self,nodeVal):
        parentNodes = []
        def findNode(node,nodeVal,final,parentNodes):
            if node is None:
                return None            
            if nodeVal == node.value:
                return node
            parentNodes.append(node.value)
            if nodeVal < node.value:                
                leftNode = findNode(node.left,nodeVal,final,parentNodes)
                if leftNode is not None:                    
                    final =  leftNode
                else:
                    parentNodes = []
            if nodeVal > node.value:
                right = findNode(node.right,nodeVal,final,parentNodes)
                if right is not None:                    
                    final =  right
                else:
                    parentNodes = []
            return final

        def minDifference(parents,value):
            minVal = None
            if len(parents) > 0 :
                minVal = parents[0]
                for val in parents:
                    diff = val-value
                    if diff > 0 and diff < minVal:
                        minVal = val
            return minVal
        node = findNode(self.root,nodeVal,None,parentNodes)
        
        successor = None
        if node.right is not None:
            successor =  self.minNode(node.right)
        else:
            if max(parentNodes) < nodeVal: # case when you are dealing with max element
                return False
            else:
               successor = minDifference(parentNodes,nodeVal)               
        return successor

    #For example, consider the following Binary Tree. Output for 2 is 6, 
    # output for 4 is 5. Output for 10, 6 and 5 is NULL.

    #             10
    #          /      \
    #        2         6
    #      /   \         \ 
    #    8      4          5
    
    def findRightBrother(self,node_val):
        queue = Queue.Queue()
        levels = Queue.Queue()
        level = 0
        crawl = self.root
        queue.put(crawl)
        levels.put(level)
        li = []
        temp = None
        while queue:
            try:
                temp = queue.get_nowait()
                level = levels.get_nowait()
                li.append(temp.value)
            except Exception:
                break
            if temp.left is not None:
                queue.put(temp.left)
                levels.put(level+1)
                
            if temp.right is not None:
                queue.put(temp.right)
                levels.put(level+1)
            
            if temp.value == node_val:
                if levels.get() == level:
                    next_node = queue.get().value
                    return next_node
                else:
                    return None

    # Biggest leaf to leaf path in binray tree
    def biggest_leafToleaf(self):
        def leaf_to_leaf(node,path,paths):
            if node is None:
                return
            path = path + 1
            if node.left is not None:
                leaf_to_leaf(node.left,path,paths)
            if node.right is not None:
                leaf_to_leaf(node.right,path,paths)
            if node.left is None and node.right is None:
                paths.append(path)
        leftpaths = []
        leaf_to_leaf(self.root.left,0,leftpaths)
        rightpaths = []
        leaf_to_leaf(self.root.right,0,rightpaths)
        max_path = max(leftpaths) + max(rightpaths) + 1
        print "Left max is "+str(max_path)

    # All traversals without using recurssion
    # Inorder without recurssion
    # For explanation http://bit.ly/IXQdq1
    def IterativeInorderTraversal(self):
        current = self.root
        stack = []        
        done = False
        while not done:
            if current is not None:
                stack.append(current)                
                current = current.left
            else:
                if stack:
                    current = stack.pop()
                    print current.value
                    current = current.right
                else:
                    done = True

    # Preorder without recurssion
    # For explanation http://bit.ly/18Tw7nk
    def IterativePreorderTraversal(self):
        current = self.root
        stack = []
        stack.append(current)
        while stack:
            temp_node = stack.pop()
            print temp_node.value
            if temp_node.right is not None:
                stack.append(temp_node.right)            
            if temp_node.left is not None:
                stack.append(temp_node.left)
    
    # Printing tree using Post order [Iterative Way]
    def IterativePostorderTraversal(self):
        temp_stack = []        
        temp_stack.append(self.root)
        post_order = []
        while temp_stack:
            temp = temp_stack.pop()
            post_order.append(temp.value)            
            if temp.left is not None:
                temp_stack.append(temp.left)
            if temp.right is not None:
                temp_stack.append(temp.right)
        while post_order:
            print post_order.pop()

    # Make node sum of its children [Sum Tree]
    def MakeSumOfChildren(self):

        def getSum(node,final_sum):
            if node is None:
                return
            final_sum = final_sum + node.value
            if node.left is not None:
                getSum(node.left,final_sum)
            if node.right is not None:
                getSum(node.right,final_sum)

            return final_sum
        
        def makeSum(node):
            if node is None:
                return
            final_sum = 0
            if node.left is not None:
                final_sum = final_sum + getSum(node.left,0)
                #print "Left sum "+str(final_sum)
            if node.right is not None:
                final_sum = final_sum + getSum(node.right,0)
                #print "Right sum "+str(final_sum)
            if node.left is not None and node.right is not None:
                node.value = final_sum
            makeSum(node.left)
            makeSum(node.right)
            
        makeSum(self.root)
    
    # Find path between any two nodes in a binary search tree
    def findPathBetweenNodes(self,node1_val,node2_val):

        def paths(node,val,path):
            path1 , path2 = "" , ""            
            if node is  None:
                return
            path = path +str(node.value)+" -> "
            if node.value == val:
                return path       
            if val < node.value:
                path1 = paths(node.left,val,path)
            if val > node.value:
                path2 = paths(node.right,val,path)
            return path1+ path2
        def find(node , val1 , val2,path=""):
            if node is None:
                return
            # If both the nodes are present right side of root 
            if val1 > node.value and val2 > node.value:
                find(node.right,val1,val2,path)

            # If both the nodes are present left side of root 
            if val1 < node.value and val2 < node.value:
                find(node.left,val1,val2,path)
            
           # If they are different sides of tree
            left_path = None
            right_path = None
            break_up_parent = str(node.value)
            if val1 < node.value and val2 > node.value:                
                left_path = paths(node.left,val1,"")
                right_path = paths(node.right,val2,"")                
            elif val1 > node.value and val2 < node.value:
                left_path = paths(node.left,val2,"")
                right_path = paths(node.right,val1,"")
            
            print str(left_path)+" "+break_up_parent+"  -> "+str(right_path)

        find(self.root,node1_val,node2_val)

    def triplet(self):
        # does an inorder traversal to ger numbers in sorted orders 
        numbers = self.toList()
        negative = []
        positive = []

        for number in numbers:
            if number < 0:
                negative.append(number)
            else:
                positive.append(number)

        # Code for triplet
        if len(negative) > 1:        
            counter = 0
            final = len(negative) - 1
            while counter < final:            
                tempSum = -(negative[counter] + negative[counter+1])            
                # if for the equivalent +ve sum in positive array
                found = None
                try:
                    found = positive.index(tempSum)
                except Exception:
                    found = None
                
                if found is not None:
                    print "Numbers are "+str(negative[counter])+","+str(negative[counter+1])+" and "+str(positive[found])
                    return
                counter += 1

        if len(positive) > 1:
            counter = 0
            final = len(positive) - 1
            while counter < final:            
                tempSum = -(positive[counter] + positive[counter+1])            
                # if for the equivalent +ve sum in positive array
                found = None
                try:
                    found = negative.index(tempSum)
                except Exception:
                    found = None            
                if found is not None:
                    print "Numbers are "+str(positive[counter])+","+str(positive[counter+1])+" and "+str(negative[found])
                    return
                counter += 1
                        
                
# Based on the given number of elements it tells how many bsts can be formed
def possibleBsts(number_of_elements):
    if number_of_elements == 0 or number_of_elements == 1:
        return 1
    else:
        elements_sum = 0
        left = 0
        right = 0
        for i in range(1,number_of_elements+1):
            left = possibleBsts(i-1)
            right = possibleBsts(number_of_elements-i)
            elements_sum = elements_sum + left * right
        
        return elements_sum

tree = BinarySearchTree()
items = [-15,40,20,80,10,5,60,100]
for item in items:
    tree.add(item)

tree.triplet()
