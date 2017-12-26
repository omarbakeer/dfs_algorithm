from graph import Graph 
import romania as RO

def ucs(graph, start='Arad', end='Bucharest'):
	''' A queue for the successor nodes to be explored with the format
	of [(cost, node's name, [path to this node])]				'''
	myQueue = [(0,start,[])] 
	# A dictionary with the visited nodes and their costs/values
	visited = {} 

	while myQueue:
		# Order the successors ascending
		myQueue.sort()
		# Visit the node of lowest cost (first node)
		cost, node, path = myQueue.pop(0)
		# Skip if the node you're visiting is already visited with a lower cost
		if node in visited and visited[node] < cost:
			continue
		# Set the new path
		path = path + [node]
		# Return path if you reached the destination
		if node == end:
			return path
		# Get the adjacents and loop through them
		for adj in graph.get_adjacents(node):
			''' Condition to prevent the graph to go inside loop 
			if you did Arad >> Sibiu you can't do Sibiu >> Arad '''
			if adj not in visited:
				myQueue.append((cost+graph.get_weight(node,adj),adj,path))

		# Mark this node as visited with it's new cost
		visited[node] = cost
		
romania = RO.romania_init()	
print(ucs(graph=romania))