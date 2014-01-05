#!/usr/bin/python
# coding: latin-1

class LinkedList:

    class Node:
        nextPtr , number = None , None
                
    linked = None 
    def append(self,data):
        if self.linked is None:
            self.linked = self.Node()
            self.linked.nextPtr = None
            self.linked.number = data
            return
        loop = self.Node()
        loop = self.linked
        while loop.nextPtr is not None:
            loop = loop.nextPtr

        loop.nextPtr = self.Node()
        loop.nextPtr.number = data
        loop.nextPtr.nextPtr = None        
        return

    def add_first(self,data):
        temp = self.Node()
        temp.nextPtr = self.linked
        temp.number = data
        self.linked  = temp
        return

    def add_after(self,after,data):
        loop = self.linked
        for i in range(0,after):
            if loop is None:
                print "Less elements "
                return
            loop = loop.nextPtr
        t = self.Node()
        t.nextPtr = loop.nextPtr
        t.number = data
        loop.nextPtr = t
        return
    
    def count(self):
        loop = self.linked
        count = 0
        while loop:
            count = count + 1
            loop = loop.nextPtr

        return count
        
    def prints(self):
        temp = self.linked
        while temp:
            if temp is None:
                break
            print temp.number
            temp = temp.nextPtr
        return

    # reverse using iterative way    
    def reverse(self):
        current = self.linked
        nextNode = None
        prevNode = None
        while current is not None:
            nextNode = current.nextPtr
            current.nextPtr = prevNode
            prevNode = current
            current = nextNode
            
        self.linked = prevNode
        return

    # Reverse using recurssion
    def reverse_recussion(self):
        def reverse(node):
            if node.nextPtr == None:
                self.linked = node
                return
            reverse(node.nextPtr)
            next = node.nextPtr
            next.nextPtr = node
            node.nextPtr = None
        reverse(self.linked)

    
    # Revese only first k nodes of the list
    def reverse_only_k(self,count):
        def reverse(node,count):
            current = self.linked
            prev = None
            next = None
            for i in range(0,count):
                next = current.nextPtr
                current.nextPtr = prev
                prev = current
                current = next
            self.linked.nextPtr = current
        
            while current:
                current = current.nextPtr

            if current:
                current.nextPtr = reverse(current.nextPtr,count)

            return prev
        self.linked = reverse(self.linked,count)

    # Reverse pair of node example : 1->2->3->4->5->6 then the
    # function should change it to 2->1->4->3->6->5

    def reverse_pairs(self):
        if self.linked is None or self.linked.nextPtr is None:
            return
        prev = self.linked
        current  = self.linked.nextPtr
        self.linked = current
        while True:
            next = current.nextPtr
            current.nextPtr = prev

            if next is None or next.nextPtr is None:
                prev.nextPtr = next
                break
            prev.nextPtr = next.nextPtr
            prev = next
            current = prev.nextPtr
   
    # if linked list is a plaindrome
    def isPalindrome(self):
        fast = self.linked
        slow = self.linked
        i = 0
        stack = []
        while fast:            
            if i%2 == 1:                
                stack.append(slow.number)              
                slow = slow.nextPtr                
            i = i + 1            
            fast = fast.nextPtr
        middle = 0
        if i%2 == 0 :
            middle = i/2
        else:
            middle = (i/2)+1
        k = 0
        temp = self.linked # for checking again
        while temp:
            if k >= middle:
                if stack.pop() != temp.number:
                    return False
            k = k + 1
            temp = temp.nextPtr

        return True        
        
        
    def Bubble_Sort(self):
        one , two = self.linked , None
        while one is not None:
            two = one # because after first 2nd loop two comes to end 
            while two is not None:
                if two.number < one.number:
                    temp = one.number
                    one.number = two.number
                    two.number = temp                   
                two = two.nextPtr                                    
            one = one.nextPtr

    def CyclicOrNot(self):
        fastPtr = self.linked
        slowPtr = self.linked
        i = 1 
        while True:
            fastPtr = fastPtr.nextPtr
            if i%2 == 0:
                slowPtr = slowPtr.nextPtr
            if fastPtr is None:
                return "ACyclic"
            if fastPtr == slowPtr:
                return "Cyclic"
            i = i +1

    #Merge Sort 
    def sort(self):
        self.Merge_Sort(self.linked)
        
    def getMiddle(self,node):
        if node is None:
            return node

        slow = node
        fast = node
        while fast.nextPtr is not None and fast.nextPtr.nextPtr is not None:
            slow = slow.nextPtr
            fast = fast.nextPtr.nextPtr
        return slow

    def Merge_Sort(self,node):
        if node.nextPtr is None or node is None:
            return node
        middle = self.getMiddle(node)
        half = middle.nextPtr
        middle.nextPtr = None

        return self.merge(self.Merge_Sort(node),self.Merge_Sort(half))

    def merge(self,a,b):
        dumbNode = self.Node()
        current = None
        current = dumbNode
        while a is not None and b is not None:
            if a.number <= b.number:
                current.nextPtr = a
                a = a.nextPtr
            else:
                current.nextPtr = b
                b = b.nextPtr
            current = current.nextPtr
        if a is None:
            current.nextPtr = b;
        else:
            current.nextPtr = a

        return dumbNode.nextPtr

    #   A singly link list and a number ‘K’, swap the Kth node from the start with the Kth node from the last.
    #  Check all the edge cases.
    # Sample Input: 1->2->3->4->5->6->7->8 and K = 3
    # Sample Output : 1->2->6->4->5->3->7->8
    
    def swap(self,node,position):
        len = self.count()
        first = position
        last =  len-position
        if node is None:
            return "Empty list"
        if last < 0:
            return "List is smaller"
        initial = 0
        alter,temp = None,None
        temp = node
        tempNode = None
        second = None
        while temp is not None:
            if initial == first: # or initial == last
                alter = temp.number
                tempNode = temp
            if initial == last:
                second = temp.number
                temp.number = alter
                tempNode.number = second                
                
            temp = temp.nextPtr        
            initial = initial + 1

    def swapDiff(self,position):
        self.swap(self.linked,position)
        self.prints()


def main():
    li = LinkedList()
    li.append(1)    
    li.append(2)
    li.append(3)
    li.append(4)
    li.append(5)
    li.append(6)
    li.append(7)
    li.prints()
    print "after"
    li.reverse_only_k(3)
    li.prints()
   
if __name__ == "__main__":main()

