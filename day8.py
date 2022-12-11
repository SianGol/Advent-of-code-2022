import numpy as np

input = "/Users/user/Dropbox/Advent-of-code-2022/Day8_input.txt"

# part1
def count_trees(grid):
    visible = []
    for index, g in enumerate(grid):
        # don't count top or bottom row
        if 0 < index < len(grid)-1:
            left_tree = g[0]
            for tree in range(1, (len(g)-1)):
                if int(left_tree) < int(g[tree]):
                    coords = str(index) + "-" + str(tree)
                    visible.append(coords)
                    left_tree = g[tree]

            right_tree = g[-1]
            for tree in list(reversed(range(1, len(g)-1))):
                if int(g[tree]) > int(right_tree):
                    coords = str(index) + "-" + str(tree)
                    visible.append(coords)
                    right_tree = g[tree]

    return visible


def swap_coords(string):
    # storing the first character
    start = string.split("-")[0]
    # storing the last character
    end = string.split("-")[1]
    swapped_string = end + "-" + start

    return swapped_string


with open(input) as i:
    normal_grid = []
    for line in i:
        new_line = list(line.strip())
        normal_grid.append(new_line)

    transposed_grid = list(map(list, zip(*normal_grid)))

    normal_res = count_trees(normal_grid)
    transposed_res = count_trees(transposed_grid)
    # flip order of coords for transposed list (trees columns)
    for index, c in enumerate(transposed_res):
        transposed_res[index] = swap_coords(c)

    merged = normal_res + transposed_res
    # remove duplicate values in merged list
    filt_merged = list(dict.fromkeys(merged))

    # finally count outside trees
    width = len(normal_grid[0])*2
    height = (len(transposed_grid)*2)-4

    answer = len(filt_merged) + width + height

print(answer)


# part 2
# count trees left/right/up/down until it finds one taller
def scenic_dist(grid, tree_height, f, s):
    left = 0
    right = 0
    # left
    for m in list(reversed(range(0, s))):
        if grid[f][m] < tree_height:
            left += 1
        else:
            left += 1
            break

    # right
    for m in range(s+1, len(grid)):
        if grid[f][m] < tree_height:
            right += 1
        else:
            right += 1
            break

    return left*right


# find visible tree in original grid and count how many are lower or equal to it
scenic_score = {}
for item in filt_merged:
    first = int(item.split("-")[0])
    second = int(item.split("-")[1])
    tree_h = normal_grid[first][second]

    scenic_score[item] = [scenic_dist(normal_grid, tree_h, first, second)]
    scenic_score[item].append(scenic_dist(transposed_grid, tree_h, second, first))

result2 = []
for key, value in scenic_score.items():
    result2.append(np.prod(value))

print(max(result2))
