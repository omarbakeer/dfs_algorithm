from graph import Graph

cities = "Arad Bucharest Craiova Dobreta Eforie Fagaras Giurgiu Hirsowa Lasi Lugoj Mehadia Neamt Oradea Pitesti Rimnicu-Vilcea Sibiu Timisoara Urziceni Vaslui Zerind".split()
g1 = Graph(20,index=cities)
g1.add_edge("Arad","Craiova",5)
g1.add_edge("Arad","Zerind")
g1.add_edge("Zerind","Rimnicu-Vilcea",100)
g1.add_edge("Sibiu","Bucharest",1000)

g1.display()

print(g1.get_adjacents("Arad"))
print(g1.get_adjacents("Zerind"))