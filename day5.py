import re

input = "/Users/user/Dropbox/Advent-of-code-2022/Day5_input.txt"


# convert list into correct order
def convert_list(l):
    transposed = list(map(list, zip(*l[:-1])))
    new_list = transposed[1::4]
    for item in new_list:
        while " " in item:
            item.remove(" ")
    crates = []
    for item in new_list:
        crates.append(list(reversed(item)))

    return crates

# read in crates as lists
with open(input) as i:
    lists = []
    for line in i:
        if "move" not in line:
            lists.append(list(line))

    crate_list = convert_list(lists)

# move crates part 1
with open(input) as i:
    for line in i:
        if "move" in line:
            nums = re.findall(r'\d+', line)
            n_move = int(nums[0])
            og = int(nums[1])-1
            new = int(nums[2])-1

            for x in range(0, n_move):
                to_move = crate_list[og][-1]
                del crate_list[og][-1]
                crate_list[new].append(to_move)
                print(crate_list)

for i in range(len(crate_list)):
    print(crate_list[i][-1])


# move crates part 2
with open(input) as i:
    for line in i:
        if "move" in line:
            nums = re.findall(r'\d+', line)
            n_move = int(nums[0])*-1
            og = int(nums[1])-1
            new = int(nums[2])-1

            to_move = "".join(crate_list[og][n_move:])
            del crate_list[og][n_move:]
            crate_list[new] += to_move
            print(crate_list)

for i in range(len(crate_list)):
    print(crate_list[i][-1])

