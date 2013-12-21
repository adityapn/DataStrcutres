import Queue
import math

class BST:

    class Node:
        left , right , key = None , None , None
        def __init__(self,num):
            self.left = None
            self.right = None
            self.key = num
    tree = None

    def add(self,number):
        self.tree = self.Value(self.tree,number)

    def Value(self,node, number):
        if node is None:
            node = self.Node(number)
            node.left = None
            node.right = None
        elif number < node.key:
            node.left = self.Value(node.left,number)
        else:
            node.right = self.Value(node.right,number)
        return node

    #Number of nodes in bst
    number = 0
    def numOfNodes(self):
        self.manyNodes(self.tree)
        return self.number

    def manyNodes(self,node):
        if node is not None:
            self.number = self.number + 1
            if node.left is not None:
                self.manyNodes(node.left)
            if node.right is not None:
                self.manyNodes(node.right)

    # test if give bst is same as other bst
    def clone(self,another):
        boole = self.TestIfTreeIsSameAsOther(self.tree,another)
        return boole

    def TestIfTreeIsSameAsOther(self,tree1,tree2):
        if tree1 is None and tree2 is None:
            return True
        if (tree1 is None and tree2 is not None) or  (tree1 is not None and tree2 is None):
            return False
        if tree1.key == tree2.key:
            return self.TestIfTreeIsSameAsOther(tree1.left,tree2.left) and self.TestIfTreeIsSameAsOther(tree1.right,tree2.right)

    # Height of a binary tree
    
    def height(self):

        def heightNew(node):
            if node is None:
                return 0
            left = heightNew(node.left)
            right = heightNew(node.right)

            end = 0
            if left > right:
                end = left + 1
            else:
                end = right + 1

            return end

        height = heightNew(self.tree)

        return height
            
   
    # Normal Traversals             
    def inorder(self):
        self.inorders(self.tree)       

    def preorder(self):
        self.preorders(self.tree)

    def preorders(self,node):
        if node is not None:
            print(node.key)
            self.preorders(node.left)
            self.preorders(node.right)    

    def inorders(self, node):        
        if node is not None:            
            self.inorders(node.left)
            print node.key
            self.inorders(node.right)

    def reverseInorder(self):
        def reverse(node):
            if node is None:
                return
            reverse(node.right)
            print node.key
            reverse(node.left)
        reverse(self.tree)

    def postorders(self,node):
        if node is not None:
            self.postorders(node.left)
            self.postorders(node.right)
            print(node.key)
    def postorder(self):
        self.postorders(self.tree)

    def LevelOrder(self):
        self.levelOrder(self.tree)
        return

    def reverseLevelorder(self):
        self.ReverseLevalOrder(self.tree)
        return

    def levelOrder(self,node):
        q = Queue.Queue()
        q.put(node)
        while q:
            try:
                temp = q.get_nowait()
            except Exception:
                break
            print(temp.key)
            if temp.left is not None:
                q.put(temp.left)
            if temp.right is not None:
                q.put(temp.right)

    def ReverseLevalOrder(self,node):
        q = Queue.Queue()
        stack = []
        q.put(node)
        stack.append(node)
        while q:
            try:
                temp = q.get_nowait()
            except Exception:
                break
            if temp.left is not None:
                q.put(temp.left)
                stack.append(temp.left)
            if temp.right is not None:
                q.put(temp.right)
                stack.append(temp.right)

        while stack:
            print(stack.pop().key)

    # Morris Traversal ( Traversal without using stack and recurssion ){Inorder}
    def MorrisTraversal(self):
        currentNode = self.tree
        prev = None
        while currentNode is not None:
            if currentNode.left is None:
                print currentNode.key
                currentNode = currentNode.right
            else:
                prev  = currentNode.left
                while prev.right is not None and prev.right is not currentNode:
                    prev = prev.right
                if prev is None:
                    prev.right = currentNode
                    currentNode = currentNode.left
                else:
                    prev.right = None
                    print currentNode.key
                    currentNode = currentNode.right


    # Maximum element in a tree
    def findMax(self):
        node = self.tree
        while node.right is not None:
            node = node.right

        print("Max is "+str(node.key))

    # Minimum element
    def findMin(self):
        node = self.tree
        while node.left is not None:
            node = node.left

        print("Minimum is "+str(node.key))

    # bt to sum bt ( node's key = sum of left and right sub tree values )
    def sumOfNodes(self):
        self.bstSum(self.tree)
        return

    def bstSum(self,node):
        if node is None:
            return
        self.bstSum(node.left)
        self.bstSum(node.right)
        if node.left is not None and node.right is not None:
            node.key = node.left.key + node.right.key

    # Tree to a list
    def treeToList(self):
        li = []
        li = self.formList(self.tree,li)
        return li

    def formList(self,node,li):
        if node is None:
            return
        self.formList(node.left,li)
        li.append(node.key)
        self.formList(node.right,li)

        return li

    #path from root to leafs
    def newPath(self,node,pathText=""):
        if node is None:
            return
        pathText = pathText + "  "+str(node.key)
        if node.left is not None:
            self.newPath(node.left,pathText)
        if node.right is not None:
            self.newPath(node.right,pathText)
        if node.left is None and node.right is None:
            print("Path "+pathText)

    def pathToLeaf(self):
        self.newPath(self.tree)

    # Lowest Common Ancestor of a Binary Search Tree (BST)
    def lca(self,root,leftNode,rightNode):
        if root is None:
            return
        if max(leftNode,rightNode) < root.key:
            return self.lca(root.left,leftNode,rightNode)
        elif min(leftNode,rightNode) > root.key:
            return self.lca(root.right,leftNode,rightNode)
        else:
            return root

    def findLca(self,valOne,valTwo):
        lcaNode = self.lca(self.tree,valOne,valTwo)
        print("lca node "+str(lcaNode.key))

# checking if the tree is balanced or not
    NodeNumber = 0
    def NodeHeight(self,node):
        self.NodeNumber  = 0
        def GivenNodeHeight(node):
            if node is not None:
                self.NodeNumber = self.NodeNumber + 1
                if node.left is not None:
                    GivenNodeHeight(node.left)
                if node.right is not None:
                    GivenNodeHeight(node.right)

        GivenNodeHeight(node)

        def findHeight():
            noOfNodes = self.NodeNumber
            n = noOfNodes/2
            for i in range(0,noOfNodes):
                if (int(math.pow(2,i)-1)) >= n:
                    return  i

        heightH = findHeight()
        return heightH

    def isBalanced(self):
        leftH = self.NodeHeight(self.tree.left)
        rightH = self.NodeHeight(self.tree.right)
        if leftH is None:
            leftH = 0
        if rightH is None:
            rightH = 0
        diff = max(leftH,rightH)-min(leftH,rightH)
        if diff <=1:
            return True

        return False

    # find if tree is complete binary tree

    def isComplete(self):        
        
        def complete(node):            
            if node.left is None and node.right is None:
                return
            if node.left is not None and node.right is not None:
                complete(node.left)
                complete(node.right)
            else:
                print "False"
                
        return complete(self.tree)
        
    # Find triplet [ Sum of 3 numbers = 0  ex: {-13, 6, 7}] in bst

    def Triplet(self):
        li = self.treeToList()
        tempOne = None
        count = 0
        SumZero = None
        tripLet = []
        for item in li:
            if item < 0:
                for second in li:
                    if second>0:
                        if tempOne is None:
                            tempOne = second
                        SumZero = -(tempOne + second)
                        if SumZero == item:
                            print "{"+str(item)+","+str(tempOne)+","+str(second)+"}"
                            return

    def removeOutsideTheRange(self,minE,maxE):
        minVal = minE
        maxVal = maxE
        def remove(node):
            if node.left is None and node.right is None:
               node = None
            elif node.left is None and node.right is not None:
                 # find max of right sub tree to replace
                 node.key = maxNode(node.right)
            elif node.left is not None and node.right is None:
                 # find max of left sub tree to replace the current node
                 node.key = maxNode(node.left)
            else:
                 # find max of right sub tree to delete
                 node.key = maxNode(node.right)

        def minNode(node):
            while node.left is not None:
                  node = node.left
            minValue = node.key
            node = None
            return minValue

        def maxNode(node):
            while node.right is not None:
                  node = node.right
            maxValue = node.key
            node = None
            return maxValue
        do = []
        def traverse(t,minE,maxE):
            if t is None:
               return
            traverse(t.left,minE,maxE)
            if t.key < minE or t.key > maxE:
               pass # remove the element 
            else:
                 print str(t.key)
            traverse(t.right,minE,maxE)

        traverse(self.tree,minVal,maxVal)


    # Find a pair with given sum in a Balanced BST
    def findPair(self,sum):
        inorderStack = []
        reverseInorderStack = []
        def inorderNumber(node):
            if node is None:
                return
            inorderNumber(node.left)
            inorderStack.append(node.key)
            inorderNumber(node.right)
        def reverseOrder(node):
            if node is None:
                return
            reverseOrder(node.right)
            reverseInorderStack.append(node.key)
            reverseOrder(node.left)
        reverseOrder(self.tree)
        inorderNumber(self.tree)

        first = 0
        last  = 0
        while True:
            if inorderStack and reverseInorderStack and first<len(inorderStack) and last < len(reverseInorderStack):
                inItem = inorderStack[first]
                reverseItem = reverseInorderStack[last]
                tempSum = inItem + reverseItem
                if tempSum == sum:
                    print "Pair for sum "+str(sum)+" is ("+str(inItem)+","+str(reverseItem)+")"
                if tempSum < sum:
                    first = first + 1
                else:
                    last = last + 1
            else:
                print "Not found"
                break

def main():
    tree = BST()
    li = [20,10,30,5,15,25,35,6]
    for i in li:
        tree.add(i)

    print("Inorder")
    tree.inorder()
    print("Preorder")
    tree.preorder()
    print("Post order")
    tree.postorder()
    print("There are "+str(tree.numOfNodes()))
    print("Level Order")
    tree.LevelOrder()
    tree.findMin()
    tree.findMax()
    print "Is it complete tree ?"
    tree.isComplete()

if __name__ == "__main__":main()
