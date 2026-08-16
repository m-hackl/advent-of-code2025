from aocd import get_data, submit

inputData = get_data(day=3, year=2025).split("\n")
inputData = """987654321111111
811111111111119
234234234234278
818181911112111""".split("\n")


def findMax(block):
    global result
    if len(result) == 12:
        return result
    maxV = sorted(block[:len(result)-12], reverse = True)[0]
    result = result + maxV
    return maxV+findMax(block[block.find(maxV)+1:])

solution = []
for i in inputData:
    result = ""
    solution.append(int(findMax(i)))

print(findMax("811111111111119"))
print(len(findMax("811111111111119")))
print(len("811111111111119"))
if findMax("811111111111119") == "811111111119":
    print("TRUE")

solution = sum(solution)

#solution = sum(map(findMax, inputData, ""))

#submit(solution, part="b", day=3, year=2025)

