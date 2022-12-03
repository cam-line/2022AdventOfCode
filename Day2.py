def puzzle1():
    with open('./inputs/rockpaperscissors.txt', 'r') as rpsinput:
        oponentweights = {'A': 1, 'B': 2, 'C': 3}
        myweights = {'X': 1, 'Y': 2, 'Z': 3}

        totalScore = 0
        lines = rpsinput.readlines()
        for line in lines:
            choices = line.split()
            oponent = oponentweights.get(choices[0])
            mychoice = myweights.get(choices[1])

            if oponent == mychoice: 
                totalScore = totalScore + 3 + mychoice
                continue
            elif oponent == 1: # rock
                if mychoice == 2:
                    totalScore = totalScore + 6 + mychoice
                else:
                    totalScore += mychoice
            elif oponent == 2: # paper
                if mychoice == 1:
                    totalScore += mychoice
                else:
                    totalScore = totalScore + 6 + mychoice
            elif oponent == 3: # scissors
                if mychoice == 1:
                    totalScore = totalScore + 6 + mychoice
                else:
                    totalScore += mychoice

        print("Total score puzzle 1:", totalScore)

def puzzle2():
    with open('./inputs/rockpaperscissors.txt', 'r') as rpsinput:
        oponentweights = {'A': 1, 'B': 2, 'C': 3}

        totalScore = 0
        lines = rpsinput.readlines()
        for line in lines:
            choices = line.split()
            oponent = oponentweights.get(choices[0])
            roundresult = choices[1]

            if roundresult == 'Y': # tie = 3
                totalScore = totalScore + 3 + oponent
                continue
            elif roundresult == 'X': # lose = 0
                if oponent == 1:
                    totalScore = totalScore + 3
                elif oponent == 2:
                    totalScore = totalScore + 1
                else:
                    totalScore = totalScore + 2
            elif roundresult == 'Z': # win = 6
                if oponent == 1:
                    totalScore = totalScore + 6 + 2
                elif oponent == 2:
                    totalScore = totalScore + 6 + 3
                else:
                    totalScore = totalScore + 6 + 1

        print("Total score puzzle 2:", totalScore)

if __name__ == "__main__":
    puzzle1()
    puzzle2()
