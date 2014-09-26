#! /usr/bin/python2


def levenshtein_distance(string1, string2):

    if len(string1) > len(string2):
	string1, string2 = string2, string1

    if len(string2) == 0:
	return len(string1)

    string1_len = len(string1) + 1
    string2_len = len(string2) + 1
    matrix = [[0] * string2_len for x in range(string1_len)]

    for i in range(string1_len):
	matrix[i][0] = i
    for j in range(string2_len):
	matrix[0][j] = j

    for i in xrange(1, string1_len):
	for j in xrange(1, string2_len):
	    deletion = matrix[i-1][j] + 1
	    insertion = matrix[i][j-1] + 1
	    substitution = matrix[i-1][j-1]

	    if string1[i-1] != string2[j-1]:
		substitution += 2

	    matrix[i][j] = min(insertion, deletion, substitution)

    return matrix, matrix[string1_len - 1][string2_len - 1]


def find_path(matrix):

    path = list()

    i = len(matrix) - 1
    j = len(matrix[0]) - 1

    path.append(matrix[i][j])

    while i != 0:

	up = matrix[i-1][j]
	left = matrix[i][j-1]
	diagonal = matrix[i-1][j-1]

	next_tile = min(up, left, diagonal) 
	path.append(next_tile)

	if next_tile == up:
	    i -= 1
	elif next_tile == left:
	    j -= 1
	elif next_tile == diagonal:
	    i -= 1
	    j -= 1

    path.reverse()
    return path


if __name__ == '__main__':
    matrix, distance = levenshtein_distance('run', 'tummy')
    print find_path(matrix)
    print distance

