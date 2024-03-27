import os

fileDir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) # Using os construct file path
raw_maze = open(r'%s/test_maze1.txt' % fileDir).read().split('\n') # Locate and open the file as read, whilst splitting the file into rows by the new line character [r prefix as it is a raw string]
# String formatting, variable into string with %s operator 

maze = [] # Construct maze as a list
for row in raw_maze:
    maze.append(row.split(', ')) # Split each row into a list at every comma, hence constructing a 2d list

def findStart(maze):
    for row_index, row in enumerate(maze): # Enumerates row indexes
        for col_index, column in enumerate(row): # Enumerate column indexes
            if column == '5': # Checks for starting point, if value = 5
                return col_index, row_index # Returns column and row index

start = findStart(maze) # Start node coordinates
max_col = len(maze[0])-1 # Maxium domain of all column indexes (Minus 1 as indexing starts with 0)
max_row = len(maze)-1 # Maximum range of all row indexes (Minus 1 as indexing starts with 0)
visited = [] # Create database that holds all visited points
queue = [[start]] # Place starting node to be processed first in the queue
# FIFO, First In First Out required to perform a Breadth First Search on the maze

# Sequentially iterating over the elements in the directions list up, down, left, right
directions = [
    [-1, 0], # Move up, decreasing the row index by 1
    [1, 0], # Move down, increasing the row index by 1
    [0, -1], # Move left, decreasing the column index by 1
    [0, 1]  # Move right, increasing the column index by 1
]

# Refering to each coordinate/point as nodes
# Each data point is a node
def findPath(maze, start):
    while len(queue) > 0: # While function to create each layer of the BFS search, given the condition that it will end when it has gone over all possible paths
        path = queue.pop(0) # Pop removing the first element of the queue which is the first path waiting in the queue
        node = path[-1] # Retrieve the end of the path as this node will be combined with a direction vector to find valid adjacent nodes
        if node not in visited: # Checks if node has been visited so that it does not proceed backwards hence to prevent an infinite loop
            # Finds all valid adjacent paths
            for direction in directions:
                moved_row = node[1] + direction[0] # Node[1] // Row Index + Direction Vector
                moved_col = node[0] + direction[1] # Node[0] // Column Index + Direction Vector
                # Testing validity of the new node
                # Range of Row is between 0 and max_row length
                # Domain of Col is between 0 and max_col length
                # Tests if new node is equal to 1 which is a wall / invalid node
                if 0 <= moved_row <= max_row and 0 <= moved_col <= max_col and maze[moved_row][moved_col] != '1':
                    new_path = path.copy() # Construct new path by copying old path
                    new_path.append((moved_col, moved_row)) # Hence New path = old path + new valid node 
                    queue.append(new_path) # Append new path back into the queue so it may be iterated again
                    if maze[moved_row][moved_col] == '3': # Checks if current node is the end 
                        return new_path # If that is validated, the function & loop is broken immediately thus returning the first valid (shortest) path 
                visited.append(node) # Mark the node as visited

# For every (col, row) coordinate in the path except the finish (last node) to be changed to 5 // Constructing a path of 5s
for col, row in findPath(maze, start)[:-1]:
    maze[row][col] = "5"

# Output shortest maze path in a grid style
# Evaluating each row of the list into a string hence then being able to remove commas, square brackets and quotation marks
for row in maze:
    print(str(row).replace("'", '').replace(',', '').strip('[').strip(']'))