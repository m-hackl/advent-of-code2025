from aocd import get_data, submit

inputData = get_data(day=2, year=2025).split(",")
#inputData = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224","1698522-1698528","446443-446449","38593856-38593862","565653-565659","824824821-824824827","2121212118-2121212124"]
invalID = []

def checkID(id):
    if len(id) == 1:
        return False
    if id[0]*len(id) == id:
        print(id, "invalid")
        return id
    if id[:2]*int(len(id)/2) == id and len(id) > 2:
        print(id, "invalid")
        return id
    for i in range(2, len(id)):
        if id[:i]*int(len(id)/i) == id:
            print(id, "invalid")
            return id
    return False

inputData = list(map(lambda tup: tuple([tup.split("-")[0], tup.split("-")[1]]), inputData))

for i in inputData:
    for j in range(int(i[0]), int(i[1])+1):
        invalID.append(int(checkID(str(j))))

solution = sum(invalID)

submit(solution, part="b", day=2, year=2025)

