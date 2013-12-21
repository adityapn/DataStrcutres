import Queue

class Graph:
	class Node:
		label = None
		visited = None
		def __init__(self,key):
			self.label = key
			self.visited = False

	rootNode = None
	nodes = []
	adjMatrix = [[0 for i in range(10)] for i in range(10)]

	def setRootNode(self,node):
		self.rootNode = node

	def getRootNode(self):
		return self.rootNode

	def addNode(self,node):
		self.nodes.append(node)

	def connectNodes(self,nodeA,nodeB):
		indexA = self.nodes.index(nodeA)
		indexB = self.nodes.index(nodeB)
		self.adjMatrix[indexA][indexB] = 1
		self.adjMatrix[indexB][indexA] = 1
		return

	def clearNodes(self):
		for node in self.nodes:
			node.visited = False

	def getUnvistedNodes(self,node):
		nodeIndex = self.nodes.index(node)
		length = len(self.nodes)
		i = 0
		while i < length:
			if self.adjMatrix[nodeIndex][i] == 1:
				if not self.nodes[i].visited:
					return self.nodes[i]
			i += 1		
		return None		

	def dfs(self):
		stack = []
		stack.append(self.rootNode)
		while stack is not None:
			try:
				vomit = stack.pop()
			except Exception:
				break
			child = None 			
			while True:
				child = self.getUnvistedNodes(vomit)
				if child:
					child.visited = True
					stack.append(child)
					print child.label
				else:
					break
		self.clearNodes()

	def bfs(self):
		queue = Queue.Queue()		
		queue.put(self.rootNode)		
		self.rootNode.visited = True
		print self.rootNode.label
		while queue:
			try:
				temp_node = queue.get_nowait()
			except Exception , error:
				break
			child_node = None
			while True:
				child_node = self.getUnvistedNodes(temp_node)
				if child_node:
					child_node.visited = True
					queue.put(child_node)					
					print child_node.label
				else:
					break
		self.clearNodes()

	def findPath(self,nodeA,nodeB):
		if nodeA is not None and nodeB is not None:			
			nodeA_index = self.nodes.index(nodeA)
			nodeB_index = self.nodes.index(nodeB)
			if self.adjMatrix[nodeA_index][nodeB_index] == 1 and self.adjMatrix[nodeB_index][nodeA_index] == 1:
					print "Both are directly connected"
			else:
				queue = Queue.Queue()
				self.rootNode.visited = True
				queue.put(self.rootNode)
				while queue:
					try:
						temp_node = queue.get_nowait()
					except Exception , error:
						break
					child_node = None
					while True:
						child_node = self.getUnvistedNodes(temp_node)
						if child_node:
							child_node.visited = True
							queue.put(child_node)							
						else:
							break
						if child_node == nodeB:
							print "Yes they are connected"
							return
				print "No path between them"


				
		else:
			print "One of the node does not exist"


g = Graph()
a = g.Node("A")
b = g.Node("B")
c = g.Node("C")
d = g.Node("D")
e = g.Node("E")
f = g.Node("F")
h = g.Node("H")
i = g.Node("I")

g.addNode(a)
g.addNode(b)
g.addNode(c)
g.addNode(d)
g.addNode(e)
g.addNode(f)
g.addNode(h)
g.addNode(i)
g.setRootNode(a)

g.connectNodes(a,b)
g.connectNodes(a,c)
g.connectNodes(a,d)
g.connectNodes(b,e)
g.connectNodes(b,f)
g.connectNodes(c,f)
g.connectNodes(b,c)
g.findPath(a,f)
print "DFS"
g.dfs()
print "BFS"
g.bfs()