from os import PRIO_PGRP
from tkinter.constants import DISABLED


class game:
    greenScore = 0
    redScore = 0
    numOfRows = 6
    numOfCols = 7
    signs = {True: '1', False: '0'}
    bools = {'1': True, '0': False}
    DIAGONAL = "diag"
    ROW = "row"
    COLUMN = "col"


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

    def getHeuristic(self, board, turn, lastRow):
        self.board = board
        self.lastRow = lastRow
        # print(board[0])
        # print(board[(self.numOfRows-1)* self.numOfCols + 0])
        return self.countScore(turn)
 
    def getScore(self, board):
        self.board = board
        return 'Agent ' + str(self.countScore(False, done=True)) + ' human ' + str(self.countScore(True, done=True))
        
    def countScore(self, turn, done=False):
        score = 0
        dict = {0:0 ,1:0, 2:0, 3:0, 4:0}
        oppDict = {0:0, 1:0, 2:0, 3:0, 4:0}
        # horizontalCheck 
        for row in range (0, self.numOfRows):
            for col in range (0, self.numOfCols-3):
                if (done):
                    valid, consec = self.countConsecutive(abs(row-self.numOfRows+1), col, 0, 1, turn)
                    if (consec == 4):
                        score += 1
                else:
                    valid, consec = self.countConsecutive(abs(row-self.numOfRows+1), col, 0, 1, turn) # count consecutive for your turn
                    valid, consecOpp = self.countConsecutive(abs(row-self.numOfRows+1), col, 0, 1, not turn) # count consecutive for opponent
                    oppDict[consecOpp] += 1
                    dict[consec] += 1
        print('From horizontal')

        print(dict)

        if (not done):
            dict, subScore = self.fillDict(dict, self.ROW)
            score += subScore - (oppDict[3]*4 + oppDict[4]*100)
            print(subScore)

        # verticalCheck
        for row in range (0, self.numOfRows-3):
            for col in range (0, self.numOfCols):
                if (done):
                    valid, consec = self.countConsecutive(abs(row-self.numOfRows+1), col, 1, 0, turn)
                    if (consec == 4):
                        score += 1
                else:
                    valid, consec = self.countConsecutive(abs(row-self.numOfRows+1), col, 1, 0, turn, vertical=True)
                    valid, consecOpp = self.countConsecutive(abs(row-self.numOfRows+1), col, 1, 0, not turn, vertical=True)
                    oppDict[consecOpp] += 1
                    dict[consec] += 1

        print('vertical')
        print(dict)

        if (not done):
            dict, subScore = self.fillDict(dict, self.COLUMN)
            score += subScore - (oppDict[3]*4 + oppDict[4]*100)
            print(subScore)

        # ascendingDiagonalCheck 
        for row in range(self.numOfRows-3):
            for col in range (self.numOfCols-3):
                if (done):
                    valid, consec = self.countConsecutive(abs(row-self.numOfRows+1), col, 1, 1, turn)
                    if (consec == 4):
                        score += 1
                else:
                    valid, consec = self.countConsecutive(abs(row-self.numOfRows+1), col, 1, 1, turn, diagonal=True)
                    validOpp, consecOpp = self.countConsecutive(abs(row-self.numOfRows+1), col, 1, 1, not turn, diagonal=True)
                    oppDict[consecOpp] += (1 * validOpp)
                    dict[consec] += (1 * valid)

        print('A diagonal')
        print(dict)

        if (not done):
            dict, subScore = self.fillDict(dict, self.DIAGONAL)
            score += subScore - (oppDict[3]*4 + oppDict[4]*100)
            print(subScore)

        # descendingDiagonalCheck
        for row in range(3, self.numOfRows):
            for col in range (0, self.numOfCols-3):
                if (done):
                    valid, consec = self.countConsecutive(abs(row-self.numOfRows+1), col, -1, 1, turn)
                    if (consec == 4):
                        score += 1
                else:
                    valid, consec = self.countConsecutive(abs(row-self.numOfRows+1), col, -1, 1, turn, diagonal=True)
                    validOpp, consecOpp = self.countConsecutive(abs(row-self.numOfRows+1), col, -1, 1, not turn, diagonal=True)
                    oppDict[consecOpp] += (1 * validOpp)
                    dict[consec] += (1 * valid)

        print('B diagonal')
        print(dict)
        if (not done):
            dict, subScore = self.fillDict(dict, self.DIAGONAL)
            score += subScore - (oppDict[3]*100 + oppDict[4]*100)
            print(subScore)

        print(score)
        return score

    def fillDict(self ,dict, direction):
        subHeuristic = 0
        if (direction == self.ROW or direction == self.COLUMN):
            subHeuristic += dict[1] * 5 # if this opens a possibility with one bullet
            subHeuristic += dict[2] * 10 # if this opens a possibility with two bullets
            subHeuristic += dict[3] * 15 # if this opens a possibility with three bullets
            subHeuristic += dict[4] * 150 # That's a point
        
        elif (direction == self.DIAGONAL):
            subHeuristic += dict[1] * 1 # if this opens a possibility with one bullet
            subHeuristic += dict[2] * 2 # if this opens a possibility with two bullets
            subHeuristic += dict[3] * 3 # if this opens a possibility with three bullets
            subHeuristic += dict[4] * 150 # That's a point
        
        return dict.fromkeys(dict, 0), subHeuristic

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
    
    def check_index(self, ind):
        return ind < (self.numOfCols*self.numOfRows)

    def countConsecutive(self, row, col, deltaRow, deltaCol, turn, vertical=False, diagonal=False):
        countScore = 0
        valid_diagonal = 1
        for i in range(4):
            indx = row * self.numOfCols + col
            if (self.board[indx] != self.signs[turn]):
                if (self.board[indx] != self.defaultSign):
                    return valid_diagonal, 0
                if (vertical):
                    return valid_diagonal, countScore
            if (self.board[indx] == self.defaultSign):
                if not vertical:
                    lower_cell = (row + 1) * self.numOfCols + col
                    if self.check_index(lower_cell):
                        if self.board[lower_cell] == self.defaultSign:
                            print(str(row) + ' ' + str(col) + ' ' + str(abs(int(self.lastRow[col]) - self.numOfRows + 1)) + ' ' + str(lower_cell))
                            valid_diagonal *= 1/3#abs(abs(int(self.lastRow[col]) - self.numOfRows + 1) - row)
                row -= deltaRow
                col += deltaCol
                continue
            row -= deltaRow
            col += deltaCol
            countScore += 1
        return valid_diagonal, countScore