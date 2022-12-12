import re
import operator
from operator import itemgetter
import math

# input = "/Users/user/Dropbox/Advent-of-code-2022/Day11_input.txt"

# manually created lists from input but could alternatively create them using for loop for each line pulling out info
monkey = [0,1,2,3,4,5,6,7]
items = [[50, 70, 89, 75, 66, 66],
        [85],
        [66,51,71,76,58,55,58,60],
        [79,52,55,51],
        [69,92],
        [71,76,73,98,67,79,99],
        [82,76,69,69,57],
        [65,79,86]]
operation = ["*5", "**2", "+1", "+6", "*17", "+8", "+7", "+5"]
test = ["/2", "/7", "/13", "/3", "/19", "/5", "/11", "/17"]
true = [2,3,1,6,7,0,7,5]
false = [1,6,3,4,5,2,4,0]

#operation dictionary
operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

counter_dict = {}

for r in range(0, 20):
    for idx, mky in enumerate(monkey):
        # possession
        monkeys_item = items[idx]
        # worry level
        number = list(map(int, re.findall(r"\d+", operation[idx])))
        action = re.findall(r"[*+\-\\]", operation[idx])
        # test
        number2 = list(map(int, re.findall(r"\d+", test[idx])))

        for i in monkeys_item:
            if len(action) == 1:
                stress = operatorlookup[action[0]](i, number[0])
            else:
                # if multiplying by itself
                stress = pow(i, 2)

            worry = int(stress / 3)
            tf_test = worry / number2[0]

            if tf_test.is_integer():
                items[true[idx]].append(worry)
                items[idx] = items[idx][1:]
                try:
                    counter_dict[monkey[idx]] += 1
                except KeyError:
                    counter_dict[monkey[idx]] = 1

            else:
                items[false[idx]].append(worry)
                items[idx] = items[idx][1:]
                try:
                    counter_dict[monkey[idx]] += 1
                except KeyError:
                    counter_dict[monkey[idx]] = 1
    print(r)


top2 = dict(sorted(counter_dict.items(), key = itemgetter(1), reverse = True)[:2])

answer = math.prod((top2.values()))

#part 2 just replace worry with stress and not dividing by 3 anymore
# find common multiple of test numbers
test2 = [2,7,13,3,19,5,11,17]
from functools import reduce
multiple = reduce(lambda x, y: x*y, test2)

for r in range(0, 10000):
    for idx, mky in enumerate(monkey):
        # possession
        monkeys_item = items[idx]
        # worry level
        number = list(map(int, re.findall(r"\d+", operation[idx])))
        action = re.findall(r"[*+\-\\]", operation[idx])
        # test
        number2 = list(map(int, re.findall(r"\d+", test[idx])))

        for i in monkeys_item:
            if len(action) == 1:
                stress = operatorlookup[action[0]](i, number[0])
            else:
                # if multiplying by itself
                stress = pow(i, 2)

            stress = stress % 9699690
            tf_test = stress % number2[0]

            if tf_test == 0:
                items[true[idx]].append(stress)
                items[idx] = items[idx][1:]
                try:
                    counter_dict[monkey[idx]] += 1
                except KeyError:
                    counter_dict[monkey[idx]] = 1

            else:
                items[false[idx]].append(stress)
                items[idx] = items[idx][1:]
                try:
                    counter_dict[monkey[idx]] += 1
                except KeyError:
                    counter_dict[monkey[idx]] = 1
    print(r)


top2 = dict(sorted(counter_dict.items(), key = itemgetter(1), reverse = True)[:2])

answer2 = math.prod((top2.values()))