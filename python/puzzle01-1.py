from aocd import get_data
from aocd import submit

#with open("python/input01-1.txt", encoding="utf-8") as f:
#    inputData = f.read().split()

inputData = get_data(day=1, year=2025).split("\n")

def dial(instr, steps):
    if instr == "R":
        resultList.append(resultList[-1]+steps)
    elif instr == "L":
        resultList.append(resultList[-1]-steps)
    else: print("Oops!")

resultList = [50]

for i in inputData:
    dial(i[0], int(i[1:]))

solution = 0

for i in resultList:
    if i % 100 == 0:
        solution += 1
    else: continue


submit(solution, part="a", day=1, year=2025)
