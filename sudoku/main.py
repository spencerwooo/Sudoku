#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys
import time

from colorama import Back, Fore, Style, init

import create_sudoku
import solve_sudoku


def main():
    try:
        # Run time timer
        startTime = time.time()

        # Init colorama terminal color support
        init()

        params = sys.argv[1]
        if params == '-c':
            createSudokuCount = int(sys.argv[2])
            assert createSudokuCount > 0
            create_sudoku.GenerateSudoku(createSudokuCount)
        elif params == '-s':
            sudokuPath = sys.argv[2]
            solve_sudoku.SolveSudoku(sudokuPath)
        else:
            print(Fore.RED + "[ERR] Invalid command.", Style.RESET_ALL)

    except ValueError:
        print(Fore.RED + "[ERR] Please input a positive integer.", Style.RESET_ALL)
    except AssertionError:
        print(Fore.RED + "[ERR] Number of sudoku must be larger than 0.", Style.RESET_ALL)
    except IOError:
        print(Fore.RED + "[ERR] Error reading file.", Style.RESET_ALL)
    except IndexError:
        print("[INFO] Usage:\n")
        print(Fore.CYAN + "-> [USAGE] `python main.py -c 10`: Create 10 sudoku final rounds.")
        print("-> [USAGE] - `python main.py -s \"solve-me.txt\"`: Solve sudoku puzzle at `solve-me.txt`.\n", Style.RESET_ALL)

    finally:
        print('[TIME] Total time:', round(
            time.time() - startTime, 4), 'seconds.')


if __name__ == "__main__":
    main()
