class game:
    greenScore = 0
    redScore = 0
    numOfRows = 6
    numOfCols = 7
    signs = {True: '1', False: '0'}
    bools = {'1': True, '0': False}

    def __init__(self, numOfRows, numOfCols, oponentSign, agentSign, defaultSign):
        self.numOfCols = numOfCols
        self.numOfRows = numOfRows
        self.oponentSign = oponentSign
        self.agentSign = agentSign
        self.defaultSign = defaultSign
        return

    def printState(self, board):
        print(board)
        for row in range (0, self.numOfRows):
            for col in range (0, self.numOfCols):
                indx = row * self.numOfCols + col
                print(str(board[indx]) + ' ', end = '')
            print('\n')
    
    # turn: 0 for human(red) 1 for computer(green)

    def getHeuristic(self, board, turn):
        self.board = board
        # print('Your turn')
        # self.countScore(turn)
        return self.countScore(turn)# - 10*self.countScore(not turn)
 
    def getScore(self, board):
        self.board = board
        return 'Agent ' + str(self.countScore(True, True)) + ' human ' + str(self.countScore(False, True))
        
    def countScore(self, turn, done=False):
        score = 0
        dict = {0:0 ,1:0, 2:0, 3:0, 4:0}
        # horizontalCheck 
        for row in range (0, self.numOfRows):
            for col in range (0, self.numOfCols-3):
                if (done):
                    score = self.countFinalScore(abs(row-self.numOfRows+1), col, 0, 1, turn)
                else:
                    score = self.countConsecutive(abs(row-self.numOfRows+1), col, 0, 1, turn)
                    dict[score] += 1
        print('From horizontal')
        print(dict)

        # verticalCheck
        for row in range (0, self.numOfRows-3):
            for col in range (0, self.numOfCols):
                if (done):
                    score = self.countFinalScore(abs(row-self.numOfRows+1), col, 1, 0, turn)
                else:
                    score = self.countConsecutive(abs(row-self.numOfRows+1), col, 1, 0, turn, True)
                    dict[score] += 1

        print('vertical')
        print(dict)

        # ascendingDiagonalCheck 
        for row in range(self.numOfRows-3):
            for col in range (self.numOfCols-3):
                if (done):
                    score = self.countFinalScore(abs(row-self.numOfRows+1), col, 1, 1, turn)
                else:
                    score = self.countConsecutive(abs(row-self.numOfRows+1), col, 1, 1, turn)
                    dict[score] += 1*0.3*score

        print('A diagonal')
        print(dict)

        # descendingDiagonalCheck
        for row in range(3, self.numOfRows):
            for col in range (0, self.numOfCols-3):
                if (done):
                    score = self.countFinalScore(abs(row-self.numOfRows+1), col, -1, 1, turn)
                else:
                    score = self.countConsecutive(abs(row-self.numOfRows+1), col, -1, 1, turn)
                    dict[score] += 1*0.3*score
        print('B diagonal')
        print(dict)
        score = 25 * dict[1] + 50 * dict[2] + 75 * dict[3] + 100 * dict[4]
        return score

    def countFinalScore(self, row, col, deltaRow, deltaCol, turn):
        countScore = 0
        for i in range(4):
            indx = row * self.numOfCols + col
            if(self.board[indx] != turn):
                return 0
            countScore += 1
            row += deltaRow
            col += deltaCol
        return 1

    def countConsecutive(self, row, col, deltaRow, deltaCol, turn, vertical=False):
        countScore = 0
        for i in range(4):
            indx = row * self.numOfCols + col
            row -= deltaRow
            col += deltaCol
            if (self.board[indx] != self.signs[turn]):
                if (self.board[indx] != self.defaultSign):
                    return 0
                if (vertical):
                    return countScore
            if (self.board[indx] == self.defaultSign):
                continue
            countScore += 1
        return countScore