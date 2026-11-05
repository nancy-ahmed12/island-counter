from collections import deque
import random

# 1 represents land; 0 represents water.
SAMPLE_GRID = [
    [1, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1],
]


def island_sizes(grid):
    """Return sizes of 4-directionally connected land components using BFS."""
    if not grid or not grid[0]:
        return []

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    sizes = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1 or visited[r][c]:
                continue

            size = 0
            queue = deque([(r, c)])
            visited[r][c] = True

            while queue:
                cr, cc = queue.popleft()
                size += 1
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and grid[nr][nc] == 1 and not visited[nr][nc]):
                        visited[nr][nc] = True
                        queue.append((nr, nc))

            sizes.append(size)

    return sizes


def make_random_grid(rows=12, cols=18, land_probability=0.42, seed=7):
    rng = random.Random(seed)
    return [
        [1 if rng.random() < land_probability else 0 for _ in range(cols)]
        for _ in range(rows)
    ]


def print_grid(grid):
    print("\nGrid (# = land, . = water):")
    for row in grid:
        print(" ".join("#" if cell else "." for cell in row))


def save_plot(grid, sizes, filename="island_map.png"):
    try:
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap
    except ImportError:
        print("Matplotlib is not installed; skipping the image. Install with: python -m pip install matplotlib")
        return

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.imshow(grid, cmap=ListedColormap(["#4ea5d9", "#58a55c"]), vmin=0, vmax=1)
    ax.set_title(f"Island Counter — {len(sizes)} island(s)")
    ax.set_xticks(range(len(grid[0])))
    ax.set_yticks(range(len(grid)))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([x - 0.5 for x in range(1, len(grid[0]))], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, len(grid))], minor=True)
    ax.grid(which="minor", color="white", linewidth=1)
    ax.tick_params(which="both", length=0)
    fig.tight_layout()
    fig.savefig(filename, dpi=180)
    plt.close(fig)
    print(f"\nMap image saved as {filename}")


def main():
    grid = SAMPLE_GRID
    sizes = island_sizes(grid)
    print_grid(grid)
    print(f"\nNumber of islands: {len(sizes)}")
    print(f"Island sizes (cells): {sizes}")
    print(f"Largest island: {max(sizes, default=0)} cell(s)")
    save_plot(grid, sizes)


if __name__ == "__main__":
    main()
