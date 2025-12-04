from aocd import get_data
from aocd import submit

inputData = get_data(day=2, year=2025).split(",")

invalID = []


def checkID(id):
    if len(id) % 2 == 0:
        if id[:int(len(str(id))/2)] == id[int(len(str(id))/2):]:
            return True
    else: return False

inputData = list(map(lambda tup: tuple([tup.split("-")[0], tup.split("-")[1]]), inputData))

for i in inputData:
    for j in range(int(i[0]), int(i[1])):
        if checkID(str(j)):
            invalID.append(j)

solution = sum(invalID)

submit(solution, part="a", day=2, year=2025)
