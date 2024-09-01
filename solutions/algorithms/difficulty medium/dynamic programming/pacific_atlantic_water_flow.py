"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west 
    if the neighboring cell's height is less than or equal to the current cell's height. 
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""

"""
Input: 
TOP AND LEFT -> PACIFIC OCEAN
RIGHT AND BOTTOM -> ATLANTIC OCEAN
heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]
           
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
"""

from collections import deque
from typing import List

class Solution:
    # dynamic programming
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # heights has at least 1 item of at least length 1
        dp_pacific = [[False for index in range(len(heights[0]))] for index in range(len(heights))]
        dp_atlantic = [[False for index in range(len(heights[0]))] for index in range(len(heights))]

        # process pacific paths -------------
        # queue should contain new positions newly marked as True
        queue = deque() # queue to process each position
        
        # process top row
        for index_x, height in enumerate(heights[0]):
            dp_pacific[0][index_x] = True # top row can reach pacific
            queue.append((0, index_x)) # append to queue
        
        # process left column
        for index_y, height_list in enumerate(heights):
            dp_pacific[index_y][0] = True # left column can reach pacific
            if (index_y, 0) not in queue:
                queue.append((index_y, 0)) # append to queue
        
        # process queue
        while queue:
            pos = queue.pop() # (y, x) coordinate
            
            # check down side
            if pos[0]+1 < len(heights) and heights[pos[0]][pos[1]] <= heights[pos[0]+1][pos[1]]:
                if not dp_pacific[pos[0]+1][pos[1]]:
                    # new position to mark as True
                    dp_pacific[pos[0]+1][pos[1]] = True
                    queue.append((pos[0]+1, pos[1]))

            # check right side
            if pos[1]+1 < len(heights[0]) and heights[pos[0]][pos[1]] <= heights[pos[0]][pos[1]+1]:
                if not dp_pacific[pos[0]][pos[1]+1]:
                    # new position to mark as True
                    dp_pacific[pos[0]][pos[1]+1] = True
                    queue.append((pos[0], pos[1]+1))

            # check top side
            if pos[0]-1 >= 0 and heights[pos[0]][pos[1]] <= heights[pos[0]-1][pos[1]]:
                if not dp_pacific[pos[0]-1][pos[1]]:
                    # new position to mark as True
                    dp_pacific[pos[0]-1][pos[1]] = True
                    queue.append((pos[0]-1, pos[1]))

            # check left side
            if pos[1]-1 >= 0 and heights[pos[0]][pos[1]] <= heights[pos[0]][pos[1]-1]:
                if not dp_pacific[pos[0]][pos[1]-1]:
                    # new position to mark as True
                    dp_pacific[pos[0]][pos[1]-1] = True
                    queue.append((pos[0], pos[1]-1))

        # process atlantic paths -------------
        queue = deque() # refresh queue
        
        # process bottom row
        for index_x, height in enumerate(heights[len(heights)-1]):
            # len(heights)-1 -> last index
            dp_atlantic[len(heights)-1][index_x] = True # bottom row can reach atlantic
            queue.append((len(heights)-1, index_x)) # append to queue
        
        # process right column
        for index_y, height_list in enumerate(heights):
            # len(heights)-1 -> last index
            dp_atlantic[index_y][len(heights[0])-1] = True # right column can reach atlantic
            if (index_y, len(heights[0])-1) not in queue:
                queue.append((index_y, len(heights[0])-1)) # append to queue
        
        # process queue
        while queue:
            pos = queue.pop() # (y, x) coordinate
            
            # check top side
            if pos[0]-1 >= 0 and heights[pos[0]][pos[1]] <= heights[pos[0]-1][pos[1]]:
                if not dp_atlantic[pos[0]-1][pos[1]]:
                    # new position to mark as True
                    dp_atlantic[pos[0]-1][pos[1]] = True
                    queue.append((pos[0]-1, pos[1]))

            # check left side
            if pos[1]-1 >= 0 and heights[pos[0]][pos[1]] <= heights[pos[0]][pos[1]-1]:
                if not dp_atlantic[pos[0]][pos[1]-1]:
                    # new position to mark as True
                    dp_atlantic[pos[0]][pos[1]-1] = True
                    queue.append((pos[0], pos[1]-1))

            # check down side
            if pos[0]+1 < len(heights) and heights[pos[0]][pos[1]] <= heights[pos[0]+1][pos[1]]:
                if not dp_atlantic[pos[0]+1][pos[1]]:
                    # new position to mark as True
                    dp_atlantic[pos[0]+1][pos[1]] = True
                    queue.append((pos[0]+1, pos[1]))

            # check right side
            if pos[1]+1 < len(heights[0]) and heights[pos[0]][pos[1]] <= heights[pos[0]][pos[1]+1]:
                if not dp_atlantic[pos[0]][pos[1]+1]:
                    # new position to mark as True
                    dp_atlantic[pos[0]][pos[1]+1] = True
                    queue.append((pos[0], pos[1]+1))
        
        # check positions with both dp as True
        result = []
        for y_pos in range(len(heights)):
            for x_pos in range(len(heights[0])):
                if dp_pacific[y_pos][x_pos] and dp_atlantic[y_pos][x_pos]:
                    result.append([y_pos, x_pos])

        return result