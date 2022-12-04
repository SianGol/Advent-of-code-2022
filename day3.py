import string

input = "/Users/user/Dropbox/Advent-of-code-2022/Day3_input.txt"

# part 1
count = 0
with open(input) as i:
    for line in i:
        midpoint = int(len(line.strip())/2)
        pack1 = line[0:midpoint]
        pack2 = line[midpoint:]

        for p in pack1:
            if p in pack2:
                try:
                    count += string.ascii_lowercase.index(p)+1
                except ValueError:
                    count += string.ascii_uppercase.index(p)+27
                break

print(count)


# part 2
def find_match(l):
    first = list(l[0])
    second = list(l[1])
    third = list(l[2])
    for p in first:
        if p in second and p in third:
            return p


count = 0
count2 = 0
with open(input) as i:
    packs = []
    for line in i:
        packs.append(line.strip())
        count2 += 1
        if count2 == 3:
            p = find_match(packs)

            try:
                count += string.ascii_lowercase.index(p) + 1
            except ValueError:
                count += string.ascii_uppercase.index(p) + 27

            count2 = 0
            packs = []

print(count)
