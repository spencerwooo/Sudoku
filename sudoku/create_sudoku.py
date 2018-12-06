#!/usr/bin/env python3
# -*- coding=utf-8 -*-


import random

import numpy


class GenerateSudoku():
    # 种子数独
    sudoku = numpy.array([[4, 7, 3, 5, 1, 8, 6, 9, 2],
                          [9, 2, 8, 6, 3, 4, 5, 1, 7],
                          [5, 6, 1, 7, 2, 9, 3, 4, 8],
                          [6, 4, 2, 8, 7, 1, 9, 5, 3],
                          [1, 8, 7, 9, 5, 3, 4, 2, 6],
                          [3, 9, 5, 2, 4, 6, 7, 8, 1],
                          [7, 1, 6, 4, 9, 2, 8, 3, 5],
                          [2, 5, 9, 3, 8, 7, 1, 6, 4],
                          [8, 3, 4, 1, 6, 5, 2, 7, 9]])

    def __init__(self, count):
        print("[INFO] Generating", count, "sudoku...")
        with open('sudoku.txt', 'a+') as sudoku_creation_file:
            # 清除文件内容
            sudoku_creation_file.truncate(0)
            for _ in range(count):
                self.generate_candidate()
                numpy.savetxt(sudoku_creation_file, self.sudoku, fmt='%d')
                sudoku_creation_file.write('\n')

        print('[INFO] Generation process complete.')

    def swap_row(self, row1, row2):
        self.sudoku[[row1, row2]] = self.sudoku[[row2, row1]]

    def swap_col(self, col1, col2):
        self.sudoku[:, [col1, col2]] = self.sudoku[:, [col2, col1]]

    def swap_num(self, num1, num2):
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == num1:
                    self.sudoku[i][j] = num2
                elif self.sudoku[i][j] == num2:
                    self.sudoku[i][j] = num1

    def generate_candidate(self):
        # 根据要求：(3+0)/9+1=4, 右上角数字恒为 4
        num_seed = [1, 2, 3, 5, 6, 7, 8, 9]
        # 根据要求：其他行、列不能与第一行、第一列进行交换
        row_and_col_seed = [[1, 2], [3, 4, 5], [6, 7, 8]]
        for _ in range(10):
            random.shuffle(num_seed)
            random.shuffle(row_and_col_seed)
            random.shuffle([random.shuffle(seed) for seed in row_and_col_seed])
            # print(row_and_col_seed)
            self.swap_row(row_and_col_seed[0][0], row_and_col_seed[0][1])
            self.swap_col(row_and_col_seed[0][0], row_and_col_seed[0][1])
            self.swap_num(num_seed[0], num_seed[1])
