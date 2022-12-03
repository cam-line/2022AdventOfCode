def charvalue(c):
    if c.islower():
        return ord(c) - 96
    else: 
        return ord(c) - 64 + 26

def puzzle1():
    with open('./inputs/rucksack.txt', 'r') as rucksackfile:
        rucksacks = rucksackfile.readlines()
        total = 0
        for rucksack in rucksacks:
            rucksack = rucksack.split()[0]
            rucklen = len(rucksack)
            compartment1 = rucksack[0:rucklen//2]
            compartment2 = rucksack[rucklen//2:rucklen]

           
            dup = ''
            for i in range(len(compartment1)):
                for j in range(len(compartment2)):
                    if compartment1[i] == compartment2[j]:
                        dup = compartment1[i]
            
            total += charvalue(dup)
        print(total)

def puzzle2():
    with open('./inputs/rucksack.txt', 'r') as rucksackfile:
        rucksacks = rucksackfile.readlines()
        total = 0
        rucksacklist = []
        for rucksack in rucksacks:
            rucksack = rucksack.replace("\n", "")
            rucksacklist.append(rucksack)
    
        for i in range(len(rucksacklist)):
            if (i + 1) % 3 == 0:
                s1 = set(rucksacklist[i - 2])
                s2 = set(rucksacklist[i - 1])
                s3 = set(rucksacklist[i])
            
                intersection = (s1.intersection(s2)).intersection(s3)
                groupval = charvalue(intersection.pop())
                total += groupval

        print(total)
        

if __name__ == "__main__":
    puzzle1()
    puzzle2()