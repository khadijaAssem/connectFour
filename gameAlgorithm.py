class game:
    greenScore = 0
    redScore = 0
    numOfRows = 6
    numOfCols = 7

    # turn: 0 for human(red) 1 for computer(green)

    def __init__(self, numOfRows, numOfCols, board):
        self.score = 0
        for i in range (0, self.numOfRows):
            for j in range (0, self.numOfCols):
                indx = i * self.numOfRows + j % self.numOfCols
                print(str(board[indx]) + ' ', end = '')
            print('\n')

        self.board = board
        self.numOfCols = numOfCols
        self.numOfRows = numOfRows
        totalScore = self.countScore('0') 
        self.greenScore = self.score
        self.score = 0
        totalScore += self.countScore('1')
        self.redScore = self.score
        self.score = 0
        print(totalScore)
        return #totalScore
    
    def countScore(self, turn):
        # # horizontalCheck 
        for row in range (0, self.numOfRows):
            for col in range (0, self.numOfCols-3):
                # print(str(row) + ' ' + str(col) + ' ' , end ='')
                # indx = row * self.numOfRows + col % self.numOfCols
                # print(self.board[indx])
                self.score += self.countConsecutive(row, col, 0, 1, turn)

        # verticalCheck
        for row in range (0, self.numOfRows-3):
            for col in range (0, self.numOfCols):
                self.score += self.countConsecutive(row, col, 1, 0, turn)

        # ascendingDiagonalCheck 
        for row in range(self.numOfRows-3):
            for col in range (self.numOfCols-3):
                self.score += self.countConsecutive(row, col, 1, 1, turn)

        # descendingDiagonalCheck
        for row in range(3, self.numOfRows):
            for col in range (0, self.numOfCols-3):
                self.score += self.countConsecutive(row, col, -1, 1, turn)

        
        return self.score

    def countConsecutive(self, row, col, deltaRow, deltaCol, turn):
        countScore = 0
        for i in range(4):
            indx = row * self.numOfRows + col % self.numOfCols
            if(self.board[indx] != turn):
                return countScore * countScore # 0
            countScore += 1
            row += deltaRow
            col += deltaCol
        return 1 * self.score #countScore * countScore
