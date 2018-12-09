# Sudoku

[![](https://img.shields.io/codacy/coverage/af90b6b7da74437ca6b1b1b0eb0443cd.svg?style=for-the-badge)](https://www.codacy.com/app/spencerwooo/Sudoku?utm_source=github.com&utm_medium=referral&utm_content=spencerwooo/Sudoku&utm_campaign=Badge_Coverage)

> 🍳 数独 | BIT 软件工程个人作业

## 内容

`/tests` 目录下存放测试用例、测试方法和测试结果。

## 测试方法、用例

利用 `coverage.py` 进行代码覆盖率测试。

**测试用例**：

- `coverage run -a main.py`
- `coverage run -a main.py -c 1`
- `coverage run -a main.py -s 'solve-me.txt'`
- `coverage run -a main.py -c -1`
- `coverage run -a main.py -c 1.5`
- `coverage run -a main.py -c abc`
- `coverage run -a main.py -s 'balabala.txt'`
- `coverage run -a main.py abc`
- `coverage run -a main.py *`

## 测试结果

```bash
Name               Stmts   Miss  Cover
--------------------------------------
create_sudoku.py      34      0   100%
main.py               32      1    97%
solve_sudoku.py       67      1    99%
--------------------------------------
TOTAL                133      2    98%
```