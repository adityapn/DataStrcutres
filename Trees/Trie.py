
class Trie:

    class Node:
        keys = None
        value = None
        isEnd = None

        def __init__(self,val):
            self.value = val
            self.keys = dict()
            self.isEnd = False
        def getChildren(self):
            return self.keys
        
        def isEnd(self):
            return self.isEnd

        def setEnd(self,status):
            self.isEnd = status

        def getValue(self):
            return self.value

    root = None
    def __init__(self):
        self.root = self.Node(str(0))

    def insert(self,word):
        length = len(word)
        crawl = self.root
        for i in range(0,length):
            childs = crawl.getChildren()
            char = word[i]
            if childs.get(char):
                crawl = childs.get(char)
            else:
                new_node = self.Node(char)
                childs[char] = new_node
                crawl = new_node
        crawl.isEnd = (True)

    def preMatchingPrefix(self,input_word):
        result = ""
        length = len(input_word)
        level = 0
        prefixMatch = 0
        crawl = self.root
        for i in range(0,length):
            childs = crawl.getChildren()
            char = input_word[i]
            if childs.get(char):
                result = result + char                
                crawl = childs[char]                
                if crawl.isEnd:
                    prefixMatch = i + 1
        if not crawl.isEnd:
            return result[0:prefixMatch]
        else:
            return result


trie = Trie()
trie.insert("are")
trie.insert("area")
trie.insert("base")
trie.insert("cat")
trie.insert("cater")
trie.insert("basement")

strings = ["caterer","basement","are","arex","basemexz","xyz"]
for string in strings:
    print "String is "+string+" prefix is "+trie.preMatchingPrefix(string)
