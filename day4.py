input = "/Users/user/Dropbox/Advent-of-code-2022/Day4_input.txt"


# part 1
count = 0

with open(input) as i:
    for line in i:
        elf1 = line.strip().split(",")[0]
        elf2 = line.strip().split(",")[1]

        elf1_rooms = [i for i in range(int(elf1.split("-")[0]), int(elf1.split("-")[1]) + 1)]
        elf2_rooms = [i for i in range(int(elf2.split("-")[0]), int(elf2.split("-")[1]) + 1)]

        if all(e in elf1_rooms for e in elf2_rooms):
            count += 1

        elif all(e in elf2_rooms for e in elf1_rooms):
            count += 1
print(count)

# part2
# part 1
count2 = 0

with open(input) as i:
    for line in i:
        elf1 = line.strip().split(",")[0]
        elf2 = line.strip().split(",")[1]

        elf1_rooms = [i for i in range(int(elf1.split("-")[0]), int(elf1.split("-")[1]) + 1)]
        elf2_rooms = [i for i in range(int(elf2.split("-")[0]), int(elf2.split("-")[1]) + 1)]

        if any(e in elf1_rooms for e in elf2_rooms):
            count2 += 1

        elif any(e in elf2_rooms for e in elf1_rooms):
            count2 += 1
print(count2)





