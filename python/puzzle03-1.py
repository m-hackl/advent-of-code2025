from aocd import get_data, submit

inputData = get_data(day=3, year=2025).split("\n")
'''inputData = """987654321111111
811111111111119
234234234234278
818181911112111""".split("\n")'''

def findMax(block):
    maxV = sorted(block[:-1], reverse = True)[0]
    return int(maxV+max(block[block.find(maxV)+1:]))

solution = sum(map(findMax, inputData))

submit(solution, part="a", day=3, year=2025)

