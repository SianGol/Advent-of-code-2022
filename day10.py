input = "/Users/user/Dropbox/Advent-of-code-2022/Day10_input.txt"

# create dictionary storing value following each cycle
cycle_dict = {}
cycle = 0
x = 1
with open(input) as i:
    for line in i:
        if "noop" in line:
            cycle += 1
            cycle_dict[cycle] = x
        else:
            cycle += 1
            cycle_dict[cycle] = x
            cycle += 1
            x += int(line.split(" ")[1])
            cycle_dict[cycle] = x

# find value at nth cycle
# 20th, 60th, 100th, 140th, 180th, 220th
cycle_list = [20, 60, 100, 140, 180, 220]
signal_strength = 0
# dictionary stores values after each cycle so check cycle before for value during that cycle
for item in cycle_list:
    value = cycle_dict[item-1]
    signal_strength = signal_strength + (value*item)

# part 2
# sprite position = x (+/-1 for 3 pixels)
# CRT_row  = cycle
# if x-1 <= cycle <= x+1 there is overlap
result = []
for key, value in cycle_dict.items():
    # find out where on 6x40 CRT cycle would fit
    key2 = key % 40
    if value-1 <= key2 <= value+1:
        result.append("#")
    else:
        result.append(".")

# print result as grid
for i in range(0, len(result), 40):
    print(result[i:i+40])




