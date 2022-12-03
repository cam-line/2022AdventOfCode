def puzzle1():
    with open('./inputs/calorieInput.txt', 'r') as calorieInput:
        maxCal = 0
        elf = 0
        data = calorieInput.readlines()
        for i in data:
            item = i.split() 
            if item != [] and item[0].isdigit():
                elf = elf + int(item[0])
            else:
                maxCal = max(maxCal, elf)
                elf = 0
        
        print("largest calories: ", maxCal)

def puzzle2():
    with open('./inputs/calorieInput.txt', 'r') as calorieInput:
        # maxCal = 0
        elf = 0
        data = calorieInput.readlines()
        items = []
        for i in data:
            item = i.split() 
            if item != [] and item[0].isdigit():
                elf = elf + int(item[0])
            else:
                items.append(elf)
                elf = 0

        top3 = sorted(items, reverse=True)[:3]
        print("Top 3 total:", top3[0] + top3[1] + top3[2])

if __name__ == "__main__":
    puzzle1()
    puzzle2()