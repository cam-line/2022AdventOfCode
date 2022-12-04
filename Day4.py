def puzzle1():
    with open("./inputs/assignmentpairs.txt", "r") as assignmentpairstext:
        assignmentpairlines = assignmentpairstext.readlines()

        pairscontained = 0
        for line in assignmentpairlines:
            line = line.replace('\n', '').split(',')
            elf1 = line[0].split('-')
            elf2 = line[1].split('-')
     
            if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
                pairscontained += 1
            elif int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1]):
                pairscontained += 1
            
        print(pairscontained)

def puzzle2():  
    with open("./inputs/assignmentpairs.txt", "r") as assignmentpairstext:
        assignmentpairlines = assignmentpairstext.readlines()

        pairscontained = 0
        for line in assignmentpairlines:
            line = line.replace('\n', '').split(',')
            elf1 = line[0].split('-')
            elf2 = line[1].split('-')
     
            r1 = range(int(elf1[0]), int(elf1[1]) + 1)
            r2 = range(int(elf2[0]), int(elf2[1]) + 1)

            if set(r2).intersection(set(r1)):
                pairscontained += 1
        print(pairscontained)

if __name__ == "__main__":
    puzzle1()
    puzzle2()