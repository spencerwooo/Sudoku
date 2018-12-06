# Sudoku

[![Travis CI](https://api.travis-ci.org/spencerwooo/Sudoku.svg?branch=docs)](https://travis-ci.org/spencerwooo/Sudoku)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b6449ccc6f3546e686ff8227525ef14e)](https://www.codacy.com/app/spencerwooo/Sudoku?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=spencerwooo/Sudoku&amp;utm_campaign=Badge_Grade)
![BIT](https://img.shields.io/badge/BIT%20%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B-%E6%95%B0%E7%8B%AC-ff69b4.svg)
[![GitHub](https://img.shields.io/dub/l/vibe-d.svg)](https://github.com/spencerwooo/Sudoku/blob/master/LICENSE)

> 🍳 数独 | BIT 软件工程个人作业

-   GitHub 项目首页：<https://github.com/spencerwooo/Sudoku>
-   项目博客主页：<https://spencerwoo.com/Sudoku>
-   项目开发历程主页：<https://spencerwoo.com/Sudoku/Progress>

## 需求分析

**⚡ 基础：**

1.  命令行程序：生成不重复的数独终局至文件
2.  读取文件中的数独问题，求解并将结果输出至文件

**🚀 进阶：**

GUI，实现一个窗口程序。数独游戏。

## 项目结构

```bash
.
├── LICENSE
├── README.md
├── performance
│   ├── result.png
│   └── result.pstats
├── requirements.txt
├── sudoku
│   ├── README.md
│   ├── create_sudoku.py
│   ├── main.py
│   ├── solve-me.txt
│   ├── solve_sudoku.py
│   └── sudoku.txt
└── tests
    └── README.md
```

## 编译运行

```bash
# 安装依赖
$ pip install -r requirements.txt

# 进入项目源代码目录
$ cd sudoku

# 生成一定数量的数独终局至文件 'sudoku.txt'
$ python main.py -c 2
```

![](https://i.loli.net/2018/12/06/5c08b302336dd.png)

```bash
# 从指定文件路径读取文件并解决其中的数独
$ python main.py -s 'solve-me.txt'
```

![](https://i.loli.net/2018/12/06/5c08b3635562f.png)

## 项目进展

-   [x] 项目结构建立
-   [x] 生成不重复的数独
-   [x] 求解数独
-   [ ] 🚧 建立项目文档（博客）
-   [ ] 代码正确性测试
-   [ ] 代码性能测试
-   [ ] 代码性能优化
-   [ ] 撰写开发博客
-   [ ] 撰写 PSP 表格 (Personal Software Progress)
-   [ ] 实现 GUI

## 性能测试数独用例

1.  初阶性能测试用例

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

2.  高阶性能测试用例

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

[2018-12-5] 时间：142.0937s（\_〆(´Д｀ )这垃圾性能）

* * *

🔢 **Sudoku** ©Spencer Woo. Released under the MIT License.

Authored and maintained by Spencer Woo.

[@Blog](https://spencerwoo.com/) · [ⒿJike](https://web.okjike.com/user/4DDA0425-FB41-4188-89E4-952CA15E3C5E/post) · [@GitHub](https://github.com/spencerwooo)
