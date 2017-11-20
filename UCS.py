from graph import Graph 

cities = "Arad Bucharest Craiova Dobreta Eforie Fagaras Giurgiu Hirsowa Lasi Lugoj Mehadia Neamt Oradea Pitesti Rimnicu-Vilcea Sibiu Timisoara Urziceni Vaslui Zerind".split()
romania = Graph(20,cities)
romania.add_edge('Sibiu', 'Arad', 140)
romania.add_edge('Zerind', 'Arad', 75)
romania.add_edge('Timisoara', 'Arad', 118)
romania.add_edge('Oradea', 'Zerind', 71)
romania.add_edge('Sibiu', 'Oradea', 151)
romania.add_edge('Lugoj', 'Timisoara', 111)
romania.add_edge('Mehadia', 'Lugoj', 70)
romania.add_edge('Dobreta', 'Mehadia', 75)
romania.add_edge('Craiova', 'Dobreta', 120)
romania.add_edge('Rimnicu-Vilcea', 'Craiova', 146)
romania.add_edge('Pitesti', 'Craiova', 138)
romania.add_edge('Sibiu', 'Rimnicu-Vilcea', 80)
romania.add_edge('Pitesti', 'Rimnicu-Vilcea', 97)
romania.add_edge('Bucharest', 'Pitesti', 101)
romania.add_edge('Fagaras', 'Sibiu', 99)
romania.add_edge('Bucharest', 'Fagaras', 211)
romania.add_edge('Giurgiu', 'Bucharest', 90)
romania.add_edge('Urziceni', 'Bucharest', 85)
romania.add_edge('Hirsowa', 'Urziceni', 98)
romania.add_edge('Vaslui', 'Urziceni', 142)
romania.add_edge('Eforie', 'Hirsowa', 86)
romania.add_edge('Lasi', 'Vaslui', 92)
romania.add_edge('Neamt', 'Lasi', 87)

def ucs(start='Arad',end='Bucharest',graph=romania):
	
	myQueue = [(0,start,[])] 
	visited = {}

	while myQueue:

		cost, node, path = myQueue.pop(0)

		if node in visited and visited[node] < cost:
			continue

		path = path+ [node]
		if node == end:
			return path

		adjacents = graph.get_adjacents(node)
		for adj in adjacents:
			if adj not in visited:
				myQueue.append((cost+graph.get_weight(node,adj),adj,path))
		visited[node] = cost
		myQueue.sort()
	# print(myQueue)
	# print(visited)
print(ucs())