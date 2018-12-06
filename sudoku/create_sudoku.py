#!/usr/bin/env python3
# -*- coding=utf-8 -*-


import random
import time

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
        # startTime = time.time()
        print("[INFO] Generating", count, "sudoku...")
        with open('sudoku.txt', 'a+') as f:
            # 清除文件内容
            f.truncate(0)
            for _ in range(count):
                self.generateCandidate()
                # print('[SUDOKU GENERATION TIME] Time', time.time() - startTime)
                numpy.savetxt(f, self.sudoku, fmt='%d')
                f.write('\n')
                # print('[FILE WRITE PROCEDURE] Time', time.time() - startTime)

        print('[INFO] Generation process complete.')

    def swapRow(self, row1, row2):
        self.sudoku[[row1, row2]] = self.sudoku[[row2, row1]]

    def swapCol(self, col1, col2):
        self.sudoku[:, [col1, col2]] = self.sudoku[:, [col2, col1]]

    def swapNum(self, num1, num2):
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == num1:
                    self.sudoku[i][j] = num2
                elif self.sudoku[i][j] == num2:
                    self.sudoku[i][j] = num1

    def generateCandidate(self):
        # 根据要求：(3+0)/9+1=4, 右上角数字恒为 4
        numSeed = [1, 2, 3, 5, 6, 7, 8, 9]
        # 根据要求：其他行、列不能与第一行、第一列进行交换
        rowAndColSeed = [[1, 2], [3, 4, 5], [6, 7, 8]]
        for _ in range(10):
            random.shuffle(numSeed)
            random.shuffle(rowAndColSeed)
            random.shuffle([random.shuffle(seed) for seed in rowAndColSeed])
            # print(rowAndColSeed)
            self.swapRow(rowAndColSeed[0][0], rowAndColSeed[0][1])
            self.swapCol(rowAndColSeed[0][0], rowAndColSeed[0][1])
            self.swapNum(numSeed[0], numSeed[1])
