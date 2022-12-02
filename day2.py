input = "/Users/user/Dropbox/aoc_2022/Day2_input.txt"

# part 1
# A | X = rock = 1 point
# B | Y = paper = 2 points
# C | Z = scissors = 3 points
# 6 points for win, 3 points for draw, 0 points for loss
win = ["A Y", "B Z", "C X"]
draw = ["A X", "B Y", "C Z"]

points = 0
with open(input) as i:
    for line in i:
        if line.strip() in win:
            points += 6
        elif line.strip() in draw:
            points += 3
        else:
            points += 0

        if line.strip().split(" ")[1] == "X":
            points += 1
        elif line.strip().split(" ")[1] == "Y":
            points += 2
        else:
            points += 3

print(points)

# part 2
# Y = draw
# X = loss
# Z = win
win = {"A": "B",
       "B": "C", 
       "C": "A"}
loss = {"A": "C",
        "B": "A",
        "C": "B"}

points = 0

with open(input) as i:
    for line in i:
        if line.strip().split(" ")[1] == "Z":
            your_move = win[line.strip().split(" ")[0]]
            points += 6
        elif line.strip().split(" ")[1] == "X":
            your_move = loss[line.strip().split(" ")[0]]
            points += 0
        else:
            your_move = line.strip().split(" ")[0]
            points += 3
        
        if your_move == "A":
            points += 1
        elif your_move == "B":
            points += 2
        else:
            points += 3

print(points)
            










