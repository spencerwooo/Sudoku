---
home: true
heroImage: /hero.png
actionText: 开发历程
actionLink: /Progress/
features:
- title: 🔢
  details: 快速生成成千上万个数独终局
- title: 🤔
  details: 急速解决成千上万个数独问题
- title: 🐍
  details: Python 实现，高效简洁，迅猛开发
footer: MIT Licensed | Copyright © 2018 Spencer Woo
---

[![](https://img.shields.io/travis/spencerwooo/Sudoku/docs.svg?style=for-the-badge)](https://travis-ci.org/spencerwooo/Sudoku)
[![](https://img.shields.io/codacy/grade/af90b6b7da74437ca6b1b1b0eb0443cd.svg?style=for-the-badge)](https://www.codacy.com/app/spencerwooo/Sudoku?utm_source=github.com&utm_medium=referral&utm_content=spencerwooo/Sudoku&utm_campaign=Badge_Grade)
[![](https://img.shields.io/codacy/coverage/af90b6b7da74437ca6b1b1b0eb0443cd.svg?style=for-the-badge)](https://www.codacy.com/app/spencerwooo/Sudoku?utm_source=github.com&utm_medium=referral&utm_content=spencerwooo/Sudoku&utm_campaign=Badge_Coverage)
[![](https://img.shields.io/github/license/spencerwooo/Sudoku.svg?style=for-the-badge)](https://github.com/spencerwooo/Sudoku/blob/master/LICENSE)

> 🍳 数独 | BIT 软件工程个人作业

:::tip 项目相关链接

-   GitHub 项目首页：<https://github.com/spencerwooo/Sudoku>
-   项目博客主页：[https://spencerwoo.com/Sudoku](/)
-   项目开发历程主页：[https://spencerwoo.com/Sudoku/Progress](/Progress/)

此处为博客首页，包含了项目概要和编译方式。项目要求的「解决项目的心路历程和收获」等内容还请见开发历程页面。
:::

## 需求分析

**基础：**

1. 命令行程序：生成不重复的数独终局至文件
2. 读取文件中的数独问题，求解并将结果输出至文件

**进阶：**

GUI，实现一个窗口程序。数独游戏。

## 项目结构

```bash
.
├── LICENSE
├── README.md
├── docs
├── performance
│   ├── performance_update.png
│   ├── performance_update.pstats
│   ├── result.png
│   └── result.pstats
├── requirements.txt
├── sudoku
│   ├── README.md
│   ├── __init__.py
│   ├── create_sudoku.py
│   ├── main.py
│   ├── solve-me.txt
│   ├── solve_sudoku.py
│   └── sudoku.txt
└── tests
    ├── README.md
    └── coverage.xml
```

## 编译运行

``` bash
# 安装依赖
$ pip install -r requirements.txt

# 进入项目源代码目录
$ cd sudoku

# 生成一定数量的数独终局至文件 'sudoku.txt'
$ python main.py -c 2
```

![](https://i.loli.net/2018/12/06/5c08b302336dd.png)

``` bash
# 从指定文件路径读取文件并解决其中的数独
$ python main.py -s 'solve-me.txt'
```

![](https://i.loli.net/2018/12/06/5c08b3635562f.png)


## 项目进展

- ✅ 项目结构建立
- ✅ 生成不重复的数独
- ✅ 求解数独
- ✅ 建立项目文档（博客）
- ✅ 代码正确性测试
- ✅ 代码性能测试
- ✅ 撰写开发博客
- ✅ 撰写 PSP 表格 (Personal Software Progress)
- 🔲 实现 GUI

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

:::tip 我的时间：
- [2018-12-5] 时间：5.8187s
- [2018-12-9] 时间：0.012s
:::

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
:::tip 我的时间：
- [2018-12-5] 时间：142.0937s（_〆(´Д｀ ) 这垃圾性能）
- [2018-12-9] 时间：0.2017s（(づ￣ 3￣)づ 牛逼！）
:::

* * *

🔢 **Sudoku** ©Spencer Woo. Released under the MIT License.

Authored and maintained by Spencer Woo.

[@Blog](https://spencerwoo.com/) · [ⒿJike](https://web.okjike.com/user/4DDA0425-FB41-4188-89E4-952CA15E3C5E/post) · [@GitHub](https://github.com/spencerwooo)