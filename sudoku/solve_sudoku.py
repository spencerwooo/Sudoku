#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import time

import numpy


class SolveSudoku():
    def __init__(self, ssudoku_path):
        try:
             # An ignorant initial baby sudoku
            solve_that_sudoku = numpy.loadtxt(ssudoku_path, dtype=int)
            print("[INFO] Begin solving sudoku at", ssudoku_path, "...")
            sudoku_count = int(len(solve_that_sudoku) / 9)
            sudoku_list = numpy.array_split(solve_that_sudoku, sudoku_count)
            with open('sudoku.txt', 'a+') as sudoku_answer_file:
                sudoku_answer_file.truncate(0)
                for each_sudoku in sudoku_list:
                    start_time = time.time()
                    self.solving_sudoku(each_sudoku)
                    # print(each_sudoku)
                    numpy.savetxt(sudoku_answer_file, each_sudoku, fmt='%d')
                    sudoku_answer_file.write('\n')
                    print('[SOLVED!] Time:', round(time.time() - start_time, 4), 'seconds.')

        except FileNotFoundError:
            print("[ERR] File not found.")

    def solving_sudoku(self, sudoku):
        current = [0, 0]

        if not self.find_that_blank(sudoku, current):
            return True
        row = current[0]
        col = current[1]

        for num in range(1, 10):
            if self.num_is_candidate(sudoku, num, row, col):
                sudoku[row][col] = num
                if self.solving_sudoku(sudoku):
                    return True
                sudoku[row][col] = 0
        return False

    def num_is_candidate(self, sudoku, num, row, col):
        # check if num is used in row
        for i in range(9):
            if sudoku[row][i] == num:
                return False

        # check if num is used in column:
        for i in range(9):
            if sudoku[i][col] == num:
                return False

        # check if num is used in block:
        row_start = int(row / 3) * 3
        col_start = int(col / 3) * 3
        # print(row_start, col_start)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if sudoku[i][j] == num:
                    return False

        return True

    def find_that_blank(self, sudoku, current):
        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == 0:
                    current[0] = row
                    current[1] = col
                    return True
        return False
