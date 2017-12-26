from graph import Graph 
import romania as RO

def dfs(graph, start='Arad', end='Bucharest'):
    count = 1
    ''' A stack for the successor nodes to be explored with the format
    of [(node's name, [path to this node])]               '''
    st = [(start, [start])]
    while st:
        # Visit the last node entered the stack 
        (node, path) = st.pop()
        # Get the adjacents and loop through them
        for next in set(graph.get_adjacents(node)) - set(path):
            # if the adjacent node is distination, print that path
            if next == end:
                print("Possible path",count,":",(path + [next]),"\n")
                count += 1
            # if the adjacent node is not distination, append it to the stack to be visisted later
            else:
                st.append((next, path + [next]))

romania = RO.romania_init()
dfs(romania)
