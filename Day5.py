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
        for i, line in enumerate(lines):
            if i > 9:
                line = line.split(' ')
                quantity = int(line[1])
                sfrom = int(line[3])
                sto = int(line[5].replace('\n', ''))
                # newstack = stacks[sto-1] + stacks[sfrom-1][len(stacks[sfrom-1])-quantity:len(stacks[sfrom-1])]
                # stacks[sto-1] = newstack
                print('#', quantity, 'to', sto, stacks[sto-1], 'from', sfrom, stacks[sfrom-1], 'new dest stack', stacks[sfrom-1][-quantity:-1])
                #print(stacks)
        
        tops = ""
        for s in stacks:
            tops += s.pop()
        print(tops)

if __name__ == "__main__":
    #puzzle1()
    puzzle2()