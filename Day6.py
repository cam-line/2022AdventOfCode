def puzzle1and2(messagelength):
    with open('./inputs/datastream.txt', 'r') as datastreamtxt:
        datastream = datastreamtxt.readline()
        
        queue = []
        for i in range(0, messagelength):
            queue.append(datastream[i])
        
        chars = messagelength
        for char in datastream[messagelength:]:
            isuniqueflag = len(set(queue)) == len(queue)
            
            if isuniqueflag:
                print('unique queue', queue, 'after', chars, 'chars')
                break
            queue.pop(0)
            queue.append(char)
            chars += 1
            


if __name__ == "__main__":
    puzzle1and2(4)
    puzzle1and2(14)