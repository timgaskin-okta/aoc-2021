from collections import Counter

from shared.Util import *


@timed
def read():
    file_name = f'input{input("Input file #: ")}.txt'
    with open(file_name) as input_file:
        start = input_file.readline().rstrip()
        input_file.readline()
        reactions = {}
        for line in input_file.readlines():
            reactants, finish = line.rstrip().split(' -> ')
            reactions[reactants] = finish
        return start, reactions


@timed
def part1(reactions):
    start, reactions = reactions

    start = list(start)

    for _ in range(10):
        new_start = []
        while start:
            new_start.append(start[0])
            if (first_two := ''.join(start[:2])) in reactions:
                new_start.append(reactions[first_two])
            start = start[1:]

        start = new_start

    count = Counter(start)
    print(count.most_common(1).pop()[1] - count.most_common()[-1][1])


@timed
def part2(reactions):
    start, reactions = reactions

    start = list(start)

    for _ in range(40):
        new_start = []
        while start:
            new_start.append(start[0])
            if (first_two := ''.join(start[:2])) in reactions:
                new_start.append(reactions[first_two])
            start = start[1:]

        start = new_start
        print(_)

    count = Counter(start)
    print(count.most_common(1).pop()[1] - count.most_common()[-1][1])


if __name__ == '__main__':
    reaction_list = read()
    part1(reaction_list)
    part2(reaction_list)
