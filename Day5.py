def getstacks():
    # with open('./inputs/cargo.txt', 'r') as file:
    #     lines = file.readlines()
    #     for i, line in enumerate(lines):
    #         if i < 8:
    #             # line = line.replace('\n', '').split('    ')
    #             # for i, l in enumerate(line):
    #             #     line[i] = l.split(' ')
    #             # print(line)
    #             # for c in range(0, len(line)):
    #             #     print(c)
    #             #     #stacks[c].append(line[c])
    #             print()
    # Could not figure this out, maybe later. Hardcoded inputs instead
    return [['B', 'S', 'V', 'Z', 'G', 'P', 'W'], ['J', 'V', 'B', 'C', 'Z', 'F'], ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'], ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'], ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'], ['G', 'F', 'Q', 'T', 'S', 'L', 'B'], ['L', 'G', 'C', 'Z', 'V'], ['N', 'L', 'G'], ['J', 'F', 'H', 'C']]

def puzzle1():
    with open('./inputs/cargo.txt', 'r') as file:
        lines = file.readlines()
        stacks = getstacks()
        for i, line in enumerate(lines):
            if i > 9:
                line = line.split(' ')
                quantity = line[1]
                sfrom = line[3]
                sto = line[5].replace('\n', '')
                for c in range(0, int(quantity)):
                    stacks[int(sto)-1].append(stacks[int(sfrom)-1].pop())

        tops = ""
        for s in stacks:
            tops += s.pop()
        print(tops)

def puzzle2():
    with open('./inputs/cargo.txt', 'r') as file:
        lines = file.readlines()
        stacks = getstacks()
        for line in lines[10:]:
            line = line.split(' ')
            quantity = int(line[1])
            sfrom = int(line[3]) - 1
            sto = int(line[5].replace('\n', '')) - 1
            stackfrom = stacks[sfrom]
            stackfrom.reverse()
            newstackfrom = stackfrom[quantity:]
            newstackfrom.reverse()
            stackgrabbed = stackfrom[:quantity]
            stackgrabbed.reverse()
            newdestack = stacks[sto] + stackgrabbed
            stacks[sto] = newdestack
            stacks[sfrom] = newstackfrom
        tops = ""
        for s in stacks:
            if s != []:
                tops += s.pop() 
        print(tops)

if __name__ == "__main__":
    puzzle1()
    puzzle2()