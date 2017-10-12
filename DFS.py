import numpy as np
import pandas as pd
import random
import util


def initializeRomania():
    cities = "Arad Bucharest Craiova Dobreta Eforie Fagaras Giurgiu Hirsowa Lasi Lugoj Mehadia Neamt Oradea Pitesti Rimnicu-Vilcea Sibiu Timisoara Urziceni Vaslui Zerind".split()

    df = pd.DataFrame(np.zeros(400).reshape(20, 20), cities, cities)

    # df = df.replace(0,df.replace([0],[None]))
    # df.replace(0,np.nan,inplace=True)
    df.loc['Arad', 'Sibiu'] = df.loc['Sibiu', 'Arad'] = 140
    df.loc['Arad', 'Zerind'] = df.loc['Zerind', 'Arad'] = 75
    df.loc['Arad', 'Timisoara'] = df.loc['Timisoara', 'Arad'] = 118
    df.loc['Zerind', 'Oradea'] = df.loc['Oradea', 'Zerind'] = 71
    df.loc['Oradea', 'Sibiu'] = df.loc['Sibiu', 'Oradea'] = 151
    df.loc['Timisoara', 'Lugoj'] = df.loc['Lugoj', 'Timisoara'] = 111
    df.loc['Lugoj', 'Mehadia'] = df.loc['Mehadia', 'Lugoj'] = 70
    df.loc['Mehadia', 'Dobreta'] = df.loc['Dobreta', 'Mehadia'] = 75
    df.loc['Dobreta', 'Craiova'] = df.loc['Craiova', 'Dobreta'] = 120
    df.loc['Craiova', 'Rimnicu-Vilcea'] = df.loc['Rimnicu-Vilcea', 'Craiova'] = 146
    df.loc['Craiova', 'Pitesti'] = df.loc['Pitesti', 'Craiova'] = 138
    df.loc['Rimnicu-Vilcea', 'Sibiu'] = df.loc['Sibiu', 'Rimnicu-Vilcea'] = 80
    df.loc['Rimnicu-Vilcea', 'Pitesti'] = df.loc['Pitesti', 'Rimnicu-Vilcea'] = 97
    df.loc['Pitesti', 'Bucharest'] = df.loc['Bucharest', 'Pitesti'] = 101
    df.loc['Sibiu', 'Fagaras'] = df.loc['Fagaras', 'Sibiu'] = 99
    df.loc['Fagaras', 'Bucharest'] = df.loc['Bucharest', 'Fagaras'] = 211
    df.loc['Bucharest', 'Giurgiu'] = df.loc['Giurgiu', 'Bucharest'] = 90
    df.loc['Bucharest', 'Urziceni'] = df.loc['Urziceni', 'Bucharest'] = 85
    df.loc['Urziceni', 'Hirsowa'] = df.loc['Hirsowa', 'Urziceni'] = 98
    df.loc['Urziceni', 'Vaslui'] = df.loc['Vaslui', 'Urziceni'] = 142
    df.loc['Hirsowa', 'Eforie'] = df.loc['Eforie', 'Hirsowa'] = 86
    df.loc['Vaslui', 'Lasi'] = df.loc['Lasi', 'Vaslui'] = 92
    df.loc['Lasi', 'Neamt'] = df.loc['Neamt', 'Lasi'] = 87
    return df

df = initializeRomania()
# print(df)
##############################################

actions = []

st = util.Stack()
source = "Arad"#input("Enter your start point:")
destination = "Bucharest"#input("Enter your end point:")

st.push(source)
while not st.isEmpty():
    node = st.pop()
    if node not in actions:
        actions.append(node)
        successors = df.columns[(df.loc[node]>0)]
        for each in successors:
            if each not in actions:
                st.push(each)
# print(actions)

###################################
source = "Arad"  # input("Enter your start point:")
destination = "Bucharest"  # input("Enter your end point:")

def dfs_paths(country):

    st = [(source, [source])]
    while st:
        (node, path) = st.pop()
        # print(node)
        for next in set(df.columns[(df.loc[node] > 0)]) - set(path):
            if next == destination:
                yield path + [next]
            else:
                st.append((next, path + [next]))

print(list(dfs_paths(df)))
