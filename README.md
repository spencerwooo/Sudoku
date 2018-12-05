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
│   └── README.md
├── sudoku
│   ├── README.md
│   ├── __main__.py
│   ├── __pycache__
│   │   ├── create_sudoku.cpython-36.pyc
│   │   └── solve_sudoku.cpython-36.pyc
│   ├── create_sudoku.py
│   ├── solve_sudoku.py
│   └── sudoku.txt
└── tests
    └── README.md

4 directories, 11 files

```

## 编译构建

``` bash
# 进入项目源代码目录
$ cd sudoku

# 生成一定数量的数独终局至文件 'sudoku.txt'
$ python3 main.py -c 2
```

![](https://i.loli.net/2018/12/04/5c063f6c2c75c.png)

``` bash
# 从指定文件路径读取文件并解决其中的数独
$ python3 main.py -s 'solve-me.txt'
```

![](https://i.loli.net/2018/12/05/5c07868b6ca7b.png)

## 项目进展

- [x] 项目结构建立
- [x] 生成不重复的数独
- [x] 求解数独
- [ ] 🚧 建立项目文档（博客）
- [ ] 代码正确性测试
- [ ] 代码性能测试
- [ ] 撰写开发博客
- [ ] 撰写 PSP 表格 (Personal Software Progress)
- [ ] 实现 GUI

## 性能测试数独用例

1. 初阶性能测试用例

```
0 0 9 0 0 8 0 4 0
6 0 0 0 0 0 0 1 7
0 1 0 0 4 0 0 0 0
0 0 0 0 0 0 0 0 4
4 8 0 6 0 3 0 2 1
3 0 0 0 0 0 0 0 0
0 0 0 0 9 0 0 8 0
2 4 0 0 0 0 0 0 6
0 5 0 7 0 0 1 0 0
```

[2018-12-5] 时间：5.8187s

2. 高阶性能测试用例

```
0 0 0 0 0 5 0 2 0
1 0 0 9 0 0 0 0 0
4 0 0 0 0 0 0 0 0
0 0 8 0 0 2 0 0 0
0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 9 0 4
0 0 5 0 0 0 3 0 0
0 0 0 1 0 0 0 0 7
0 0 2 4 0 8 0 0 0
```

[2018-12-5] 时间：142.0937s（_〆(´Д｀ )这垃圾性能）