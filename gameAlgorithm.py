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
                print(str(board[i][j]) + ' ', end = '')
            print('\n')

        self.numOfCols = numOfCols
        self.numOfRows = numOfRows
        print(self.countScore(board, 0))
        self.greenScore = self.score
        self.score = 0
        print(self.countScore(board, 1))
        self.redScore = self.score
        self.score = 0
        return
    
    def countScore(self, board, turn):
        # horizontalCheck 
        for j in range (0, self.numOfCols-3):
            for i in range (0, self.numOfRows):
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == turn:
                    self.score += 1
        # verticalCheck
        for i in range (0, self.numOfRows-3):
            for j in range (0, self.numOfCols):
                if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == turn:
                    self.score += 1

        # ascendingDiagonalCheck 
        for i in range(3, self.numOfRows):
            for j in range (0, self.numOfCols-3):
                if (board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == turn):
                    self.score += 1

        # descendingDiagonalCheck
        for i in range(3, self.numOfRows):
            for j in range (3, self.numOfCols-3):
                if (board[i][j] == board[i-1][j-1] == board[i-2][j-2] == board[i-3][j-3] == turn):
                    self.score += 1

        # # top-left to bottom-right
        # for rowStart in range(0, self.numOfRows - 4):
        #     count = 0
        #     row = col = 0
        #     row = rowStart; col = 0
        #     while (row < self.numOfRows and col < self.numOfCols):
        #         if(board[row][col] == turn):
        #             count+=1
        #             if(count == 4): 
        #                 self.score += 1
        #                 count = 0
        #         else :
        #             count = 0
        #         row+=1; col+=1
        # # top-left to bottom-right
        # for colStart in range(1, self.numOfCols - 4):
        #     count = 0
        #     row = col = 0
        #     row = 0; col = colStart
        #     while (row < self.numOfRows and col < self.numOfCols):
        #         if(board[row][col] == turn):
        #             count+=1
        #             if(count == 4): 
        #                 self.score += 1
        #                 count = 0
        #         else:
        #             count = 0
        #         row+=1; col+=1

        return self.score

    def check(self, turn):
        if (turn == 0):
            return
