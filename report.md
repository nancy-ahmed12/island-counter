# Island Counter — Project Report

## Problem and graph model
This project counts islands in a grid of land (1) and water (0). Each land cell is a graph vertex. An edge connects two land cells that share a side (up, down, left, or right). Diagonal contact does not connect islands.

## Method
I used breadth-first search (BFS). The program scans the grid. Whenever it finds an unvisited land cell, it starts a BFS, marks all reachable land cells as visited, and records the number of cells in that island. It reports the total island count, the size of each island, and the largest island. It also prints and visualizes the sample grid.

## Complexity analysis
For a grid with R rows and C columns, each cell is checked and visited at most once. Therefore, the running time is O(R × C). The visited matrix and BFS queue require O(R × C) extra space in the worst case.

## Experiment and results
For the included sample grid, the program should find 6 islands with sizes 4, 2, 2, 3, 2, and 2 cells. The largest island contains 4 cells. The map uses `#` for land and `.` for water; the saved image is `island_map.png`.

## Conclusion and reflection
BFS is a suitable way to count connected components because it explores all cells reachable from each starting land cell and avoids counting them again. This project helped demonstrate how a grid can be represented as a graph. A useful extension would be to compare BFS with DFS or generate random grids with different land probabilities and plot how the island count changes.

