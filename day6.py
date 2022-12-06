input = "/Users/user/Dropbox/Advent-of-code-2022/Day6_input.txt"

# part 1
with open(input) as i:
    for line in i:
        total = len(line)
        for x in range(0, total, 1):
            chunk = line[x:x+4]
            print(chunk)
            if len(set(chunk)) == 4:
                answer = line.index(str(chunk))+4
                break

print(answer)

# part 2
with open(input) as i:
    for line in i:
        total = len(line)
        for x in range(0, total, 1):
            chunk = line[x:x+14]
            print(chunk)
            if len(set(chunk)) == 14:
                answer2 = line.index(str(chunk))+14
                break
print(answer2)



