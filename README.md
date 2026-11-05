# Island Counter

A beginner graph project that counts connected groups of land in a grid. Each cell is a vertex; orthogonally adjacent land cells are connected by edges. The program uses breadth-first search (BFS) to find each island and reports each island's size and the largest island. Diagonal cells do not connect.

## Run

```bash
python island_counter.py
```

The sample grid is printed in the terminal and saved as `island_map.png`. `#` means land and `.` means water.

## Optional visualization dependency

```bash
python -m pip install matplotlib
```

Without Matplotlib, the island count still works; only the image is skipped.

## Tests

```bash
python -m unittest test_island_counter.py
```

## Complexity

BFS visits each grid cell at most once, so the running time is O(R × C), where R and C are the number of rows and columns. The visited array and queue use O(R × C) space in the worst case.
