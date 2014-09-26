#! /usr/bin/python2

# Breadth-first search of graph from start to end


graph = {
	'1': ['2', '3', '4'],
	'2': ['5', '6'],
	'5': ['9', '10'],
	'4': ['7', '8'],
	'7': ['8', '11', '12'],
	'11': ['13', '14', '15'],
	'12': ['16']
	}

graph2 = {
	'1': ['2', '3', '4'],
	'2': ['5'],
	'4': ['6'],
	'5': ['6', '7'],
	'6': ['7', '8']
	}


def bfs(graph, start=None, end=None):

    visited = list()
    queue = list()

    visited.append(start)
    queue.append(start)

    while queue:

	for adj in graph.get(queue[0], []):

	    if adj in visited:
		pass

	    else:
		visited.append(adj)
		queue.append(adj)

	queue.pop(0)	    

    return visited


if __name__ == '__main__':
    print bfs(graph2, start='1', end='8')

