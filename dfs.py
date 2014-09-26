#! /usr/bin/python2

# A depth-first search of graph for end

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

def dfs(graph, start=None, end=None, visited=None):

    if not visited:
	visited = list()

    visited.append(start)

    for adj in graph.get(start, []):
	visited = dfs(graph, adj, end, visited)

	if visited and visited[-1] == end:
	    return visited
	else:
	    visited.pop()

    return visited


if __name__ == '__main__':
    print dfs(graph2, start='1', end='8')

