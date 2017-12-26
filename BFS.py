from graph import Graph 
import romania as RO

def bfs(graph, start='Arad', end='Bucharest'):
    count = 1
    ''' A queue for the successor nodes to be explored with the format
    of [(node's name, [path to this node])]                        '''
    Queue = [(start, [start])]
    while Queue:
        # Visit the last node entered the queue 
        (node, path) = Queue.pop(0)
        # Get the adjacents and loop through them
        for next in set(graph.get_adjacents(node)) - set(path):
            # if the adjacent node is distination, print that path
            if next == end:
                print("Possible path",count,":",(path + [next]),"\n")
                count += 1
            # if the adjacent node is not distination, append it to the queue to be visisted later
            else:
                Queue.append((next, path + [next]))

romania = RO.romania_init()
print("\n***** click return if you want the default (Arad,Bucharest) *****")
startN = input("Enter start node:")
if len(startN) < 1 : startN = "Arad"
endN = input("Enter end node:")
if len(endN) < 1 : endN = "Bucharest"
bfs(romania,startN,endN)
