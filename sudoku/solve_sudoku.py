#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import numpy


class SolveSudoku():
    # An ignorant initial blank baby sudoku
    solveThatSudoku = []

    def __init__(self, sudokuPath):
        try:
            self.solveThatSudoku = numpy.loadtxt(sudokuPath, dtype=int)
            print("[INFO] Begin solving sudoku at", sudokuPath, "...")

            self.solvingSudoku(self.solveThatSudoku)

            print(self.solveThatSudoku)

        except FileNotFoundError:
            print("[ERR] File not found.")

    def solvingSudoku(self, sudoku):
        currentBlock = [0, 0]

        if not self.blockIsEmpty(currentBlock):
            return True
        row = currentBlock[0]
        col = currentBlock[1]

        for num in range(1, 9):
            if self.numIsCandidate(row, col, num):
                self.solveThatSudoku[row][col] = num
                if self.solvingSudoku(self.solveThatSudoku):
                    return True
                self.solveThatSudoku[row][col] = 0
        
        return False

    def blockIsEmpty(self, currentBlock):
        for i in range(9):
            for j in range(9):
                if self.solveThatSudoku[i][j] == 0:
                    currentBlock[0] = i
                    currentBlock[1] = j
                    # print("empty: row="+str(i)+" col="+str(j))
                    return True
        return False

    def numUsedInRow(self, currentRow, currentNum):
        for i in range(9):
            if self.solveThatSudoku[currentRow][i] == currentNum:
                return True
        return False

    def numUsedInCol(self, currentCol, currentNum):
        for i in range(9):
            if self.solveThatSudoku[i][currentCol] == currentNum:
                return True
        return False

    def numUsedInBigBlock(self, currentRow, currentCol, currentNum):
        for i in range(3):
            for j in range(3):
                if self.solveThatSudoku[currentRow + i][currentCol + j] == currentNum:
                    return True
        return False

    def numIsCandidate(self, row, col, num):
        return not self.numUsedInRow(row, num) and not self.numUsedInCol(col, num) and not self.numUsedInBigBlock(row - row % 3, col - col % 3, num)