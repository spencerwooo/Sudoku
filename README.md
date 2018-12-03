# Sudoku

🍳 数独 | BIT 软件工程个人作业

## 需求分析

**基础：**

1. 命令行程序：生成不重复的数独终局至文件
2. 读取文件中的数独问题，求解并将结果输出至文件

**进阶：**

GUI，实现一个窗口程序。数独游戏。

## 项目结构

```
.
├── LICENSE
├── README.md
├── bin
├── sudoku
│   ├── __pycache__
│   │   └── create_sudoku.cpython-36.pyc
│   ├── create_sudoku.py
│   ├── main.py
│   ├── solve_sudoku.py
│   └── sudoku.txt
└── tests

4 directories, 7 files

```

## 编译构建

``` bash
# 进入项目源代码目录
$ cd sudoku

# 生成一定数量的数独终局至文件 'sudoku.txt'
$ ./__main__.py -c 10

# 从指定文件路径读取文件并解决其中的数独
$ ./__main__.py -s 'solve-me.txt'
```

## 项目进展

- [x] 项目结构建立
- [x] 生成不重复的数独
- [ ] 求解数独
- [ ] 建立项目文档（博客）
- [ ] 代码正确性测试
- [ ] 代码性能测试
- [ ] 撰写开发博客
- [ ] 撰写 PSP 表格 (Personal Software Progress)
- [ ] 实现 GUI