#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import numpy


class SolveSudoku():
    def __init__(self, sudokuPath):
        try:
            solveThatSudoku = numpy.loadtxt(sudokuPath, dtype=int)
            print("[INFO] Begin solving sudoku at", sudokuPath, "...")

            print(solveThatSudoku)

        except Exception:
            print("[ERR] File not found.")

