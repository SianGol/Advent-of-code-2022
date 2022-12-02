from operator import itemgetter

input = "/Users/user/Dropbox/aoc_2022/Day1_input.txt"

count = 1
elves = {}
with open(input) as i:
    for line in i:
        if line != "\n":
            line = int(line.strip())
            try:
                elves[count].append(line)
            except KeyError:
                elves.update({count: [line]})
        if line == "\n":
            count += 1

total = {k: sum(elves[k]) for k in elves.keys()}
max_elf = max(total, key=total.get)
part1 = total[max_elf]

#part2
top3 = dict(sorted(total.items(), key = itemgetter(1), reverse = True)[:3])
part2 = sum(top3.values())






