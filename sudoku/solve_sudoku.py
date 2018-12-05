#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import numpy


class SolveSudoku():
    def __init__(self, sudokuPath):
        try:
             # An ignorant initial baby sudoku
            solveThatSudoku = numpy.loadtxt(sudokuPath, dtype=int)
            print("[INFO] Begin solving sudoku at", sudokuPath, "...")
            self.solvingSudoku(solveThatSudoku)
            print(solveThatSudoku)

        except FileNotFoundError:
            print("[ERR] File not found.")

    def solvingSudoku(self, sudoku):
        current = [0, 0]

        if not self.findThatBlank(sudoku, current):
            return True
        row = current[0]
        col = current[1]

        for num in range(1, 10):
            if self.numIsCandidate(sudoku, num, row, col):
                sudoku[row][col] = num
                if self.solvingSudoku(sudoku):
                    return True
                sudoku[row][col] = 0
        return False

    def numIsCandidate(self, sudoku, num, row, col):
        # check if num is used in row
        for i in range(9):
            if sudoku[row][i] == num:
                return False

        # check if num is used in column:
        for i in range(9):
            if sudoku[i][col] == num:
                return False

        # check if num is used in block:
        rowStart = int(row / 3) * 3
        colStart = int(col / 3) * 3
        # print(rowStart, colStart)
        for i in range(rowStart, rowStart + 3):
            for j in range(colStart, colStart + 3):
                if sudoku[i][j] == num:
                    return False

        return True

    def findThatBlank(self, sudoku, current):
        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == 0:
                    current[0] = row
                    current[1] = col
                    return True
        return False