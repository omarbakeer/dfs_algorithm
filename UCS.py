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

visited = []
not_visited = []
node = 'Arad'
total_cost = 0
temp_cost = {node: total_cost}
end = 'Bucharest'
while node is not end:
	node = min(temp_cost,key=temp_cost.get)
	
	try:
		total_cost = temp_cost.pop(node)
	except:
		print("queue is empty")
		quit()
	if node is end:
		break
	adjacents = romania.get_adjacents(node)
	for adj in adjacents:
		if (adj not in visited):
			temp_cost[adj] = total_cost+romania.get_weight(node,adj)
		
		else: # adj in not_visited:
			try:
				if temp_cost[adj] > total_cost+romania.get_weight(node,adj) & adj not in visited:
					temp_cost[adj] = total_cost+romania.get_weight(node,adj)
			except:
				# print("adjacent is not an option to revisit")
				continue
			
	visited.append(node)
	print(temp_cost)
	print(visited)
# min_adj_cost,next_node = temp_cost.pop(0)
# if total_cost < min_adj[0]
# node = min_adj[1]
