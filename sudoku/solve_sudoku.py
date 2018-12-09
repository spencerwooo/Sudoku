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

                    print('[SOLVED!] Time:', round(
                        time.time() - start_time, 4), 'seconds.')

        except FileNotFoundError:
            print("[ERR] File not found.")

    def solving_sudoku(self, sudoku):
        # 每个格子所在列的数字集合
        col_num = []
        # 每个格子所在行的数字集合
        row_num = []
        # 每个格子所在 3x3 子块的数字集合
        sqr_num = [[0]*3 for _ in range(3)]

        # 初始化
        for i in range(9):
            col_num.append(set(tuple(range(1, 10))))
            row_num.append(set(tuple(range(1, 10))))

        for i in range(3):
            for j in range(3):
                sqr_num[i][j] = set(tuple(range(1, 10)))

        blank_in_sudoku = set()

        for i in range(9):
            for j in range(9):
                if sudoku[i][j] != 0:
                    if sudoku[i][j] in row_num[i]:
                        row_num[i].remove(sudoku[i][j])
                    if sudoku[i][j] in col_num[j]:
                        col_num[j].remove(sudoku[i][j])
                    if sudoku[i][j] in sqr_num[i//3][j//3]:
                        sqr_num[i//3][j//3].remove(sudoku[i][j])
                else:
                    blank_in_sudoku.add((i, j))

        self.dfs(blank_in_sudoku, col_num, row_num, sqr_num, sudoku)

    def dfs(self, blank_in_sudoku, col_num, row_num, sqr_num, sudoku):
        if not blank_in_sudoku:
            return True

        max_possible_len = 9

        for (m, n) in blank_in_sudoku:
            candidate_num = row_num[m] & col_num[n] & sqr_num[m//3][n//3]
            if len(candidate_num) <= max_possible_len:
                max_possible_len = len(candidate_num)
                i, j = m, n

        if max_possible_len == 0:
            return False

        blank_in_sudoku.remove((i, j))
        candidate_num = row_num[i] & col_num[j] & sqr_num[i//3][j//3]

        for num in candidate_num:
            row_num[i].remove(num)
            col_num[j].remove(num)
            sqr_num[i//3][j//3].remove(num)
            sudoku[i][j] = num
            if self.dfs(blank_in_sudoku, col_num, row_num, sqr_num, sudoku):
                return True
            sudoku[i][j] = 0
            row_num[i].add(num)
            col_num[j].add(num)
            sqr_num[i//3][j//3].add(num)

        blank_in_sudoku.add((i, j))
        return False
