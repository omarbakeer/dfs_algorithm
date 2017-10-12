import numpy as np
import pandas as pd


def initializeRomania():
    cities = "Arad Bucharest Craiova Dobreta Eforie Fagaras Giurgiu Hirsowa Lasi Lugoj Mehadia Neamt Oradea Pitesti Rimnicu-Vilcea Sibiu Timisoara Urziceni Vaslui Zerind".split()

    romania = pd.DataFrame(np.zeros(400).reshape(20, 20), cities, cities)

    romania.loc['Arad', 'Sibiu'] = romania.loc['Sibiu', 'Arad'] = 140
    romania.loc['Arad', 'Zerind'] = romania.loc['Zerind', 'Arad'] = 75
    romania.loc['Arad', 'Timisoara'] = romania.loc['Timisoara', 'Arad'] = 118
    romania.loc['Zerind', 'Oradea'] = romania.loc['Oradea', 'Zerind'] = 71
    romania.loc['Oradea', 'Sibiu'] = romania.loc['Sibiu', 'Oradea'] = 151
    romania.loc['Timisoara', 'Lugoj'] = romania.loc['Lugoj', 'Timisoara'] = 111
    romania.loc['Lugoj', 'Mehadia'] = romania.loc['Mehadia', 'Lugoj'] = 70
    romania.loc['Mehadia', 'Dobreta'] = romania.loc['Dobreta', 'Mehadia'] = 75
    romania.loc['Dobreta', 'Craiova'] = romania.loc['Craiova', 'Dobreta'] = 120
    romania.loc['Craiova', 'Rimnicu-Vilcea'] = romania.loc['Rimnicu-Vilcea', 'Craiova'] = 146
    romania.loc['Craiova', 'Pitesti'] = romania.loc['Pitesti', 'Craiova'] = 138
    romania.loc['Rimnicu-Vilcea', 'Sibiu'] = romania.loc['Sibiu', 'Rimnicu-Vilcea'] = 80
    romania.loc['Rimnicu-Vilcea', 'Pitesti'] = romania.loc['Pitesti', 'Rimnicu-Vilcea'] = 97
    romania.loc['Pitesti', 'Bucharest'] = romania.loc['Bucharest', 'Pitesti'] = 101
    romania.loc['Sibiu', 'Fagaras'] = romania.loc['Fagaras', 'Sibiu'] = 99
    romania.loc['Fagaras', 'Bucharest'] = romania.loc['Bucharest', 'Fagaras'] = 211
    romania.loc['Bucharest', 'Giurgiu'] = romania.loc['Giurgiu', 'Bucharest'] = 90
    romania.loc['Bucharest', 'Urziceni'] = romania.loc['Urziceni', 'Bucharest'] = 85
    romania.loc['Urziceni', 'Hirsowa'] = romania.loc['Hirsowa', 'Urziceni'] = 98
    romania.loc['Urziceni', 'Vaslui'] = romania.loc['Vaslui', 'Urziceni'] = 142
    romania.loc['Hirsowa', 'Eforie'] = romania.loc['Eforie', 'Hirsowa'] = 86
    romania.loc['Vaslui', 'Lasi'] = romania.loc['Lasi', 'Vaslui'] = 92
    romania.loc['Lasi', 'Neamt'] = romania.loc['Neamt', 'Lasi'] = 87
    return romania


def romanias_paths(country,start,destination):
    actions = []
    st = [(start, [start])]
    while st:
        (node, path) = st.pop()
        for next in set(romania.columns[(romania.loc[node] > 0)]) - set(path):
            if next == destination:
                print("Possible path:",(path + [next]),"\n")
            else:
                st.append((next, path + [next]))

romania = initializeRomania()
source = input("Enter your start point:")
destination = input("Enter your end point:")

print(romania) # print the DataFrame
romanias_paths(romania,source,destination)
