from aocd import get_data
from aocd import submit

#with open("python/input01-1.txt", encoding="utf-8") as f:
#    inputData = f.read().split()

inputData = get_data(day=1, year=2025).split("\n")

def dial(instr, steps):
    global state
    global solution
    direction = 1
    if instr == "L": direction = -1
    for i in range(steps):
        state = state + direction
        if state % 100 == 0:
            solution += 1

state = 50
solution = 0

for i in inputData:
    dial(i[0], int(i[1:]))

submit(solution, part="b", day=1, year=2025)