# solution for River Sizes question from algoexpert.io


# for starting point with coords returns length of river in matrix
def get_len_of_river(coords, matrix, dims, visited, current_length):
    row, column = coords
    # mark as visited
    visited[row][column] = 1
    directions = [(row + 1, column),    # UP
                  (row, column + 1),    # RIGHT
                  (row, column - 1),    # LEFT
                  (row - 1, column)]    # DOWN

    # try to go to all directions
    for direction in directions:
        current_length += get_len_of_river(direction, matrix, dims, visited, 0)

    return current_length + 1


# returns whether the place was not visited, coords are valid and at coords is river(value 1)
def can_be_visited(coords, dims, matrix, visited):
    row, column = coords
    height, length = dims

    return row is not height and row is not -1 and \
            column is not length and column is not -1 and \
            matrix[row][column] is 1 and visited[row][column] is not 1


# returns list of lengths of rivers in matrix
def river_sizes_of(matrix):
    lenghts = []
    visited = []
    num_of_rows = len(matrix)
    num_of_columns = len(matrix[0])
    dims = (num_of_rows, num_of_columns)

    for i in range(num_of_rows):
        visited.append([])

    for i in range(num_of_rows):
        for j in range(num_of_columns):
            visited[i].append(0)

    for i in range(num_of_rows):
        for j in range(num_of_columns):
            if matrix[i][j] and not visited[i][j]:
                lenghts.append(get_len_of_river((i, j), matrix, dims, visited, 0))

    return lenghts


# by default runs a simple test
if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    ]
    print(river_sizes_of(matrix))
