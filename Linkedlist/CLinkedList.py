class CLinkedList:

    class Node:
        number , link = None , None


    clist = None

    def append(self,data):
        if self.clist is None:
            self.clist = self.Node()
            self.clist.number = data
            self.clist.link = None
            return
        temp = self.clist
        while temp.link and temp.link is not self.clist: # make sure it's not first node
            temp = temp.link

        one = self.Node()
        one.number = data
        one.link = self.clist
        temp.link = one

    def printList(self):
        temp = self.clist
        while temp and temp.link is not self.clist: # check if it's first node or not
            print temp.number
            temp = temp.link
        return
    
    def count(self):
        temp = self.clist
        c  = 0 
        while temp and temp.link is not self.clist:
            c = c+1
            temp = temp.link
            
        return c
            
    
    def add_after(self,after,data):
        temp = self.clist
        maxs = self.count()
        for i in range(0,maxs):
            if i == after:
                one = self.Node()
                one.number = data
                one.link = temp.link
                temp.link = one
                return
            temp = temp.link
            
        print "Not enough elements "
        
        return
            
    def CyclicOrNot(self):
        fastPtr = self.clist
        slowPtr = self.clist
        i = 1 # 0 directly returns True 
        while True:
            fastPtr = fastPtr.link
            if i%2 == 0:
                slowPtr = slowPtr.link
            if fastPtr is None:
                return False
            if fastPtr == slowPtr:
                return True


def main():
    li = CLinkedList()
    li.append(45)
    li.append(22)
    li.append(78)
    li.append(45)
    li.append(5)
    li.append(6)
    li.add_after(3,3)
    li.add_after(4,4)
    li.printList()

if __name__ == "__main__":main()
        
        
        
