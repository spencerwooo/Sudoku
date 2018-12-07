---
sidebarDepth: 3
---

# 开发历程

## I. 项目地址

:::tip 项目地址与相关链接

-   GitHub 项目首页：<https://github.com/spencerwooo/Sudoku>
-   项目博客主页：[https://spencerwoo.com/Sudoku](/)
-   项目开发历程主页：[https://spencerwoo.com/Sudoku/Progress](/Progress/)

这里是项目要求的「解决项目的心路历程和收获」等开发历程内容页面。
:::

## II. PSP

|                PSP 2.1                | Personal Software Progress Stages | 预估耗时（分钟） | 实际耗时（分钟） |
| :-----------------------------------: | :-------------------------------: | :------: | :------: |
|                Planning               |                 计划                |    60    |          |
|                Estimate               |            估计这个任务需要多少时间           |   2500   |          |
|              Development              |                 开发                |   1500   |          |
|                Analysis               |           需求分析（包括学习新技术）           |    500   |          |
|              Design Spec              |               生成设计文档              |    60    |          |
|             Design Review             |          设计复审（和同事审核设计文档）          |    30    |          |
|            Coding Standard            |        代码规范（为目前的开发制定合适的规范）        |    30    |          |
|                 Design                |                具体设计               |    200   |          |
|                 Coding                |                具体编码               |    400   |          |
|              Code Review              |                代码复审               |    60    |          |
|                  Test                 |         测试（自我测试、修改代码、提交测试）        |    200   |          |
|               Reporting               |                 报告                |    20    |          |
|              Test Report              |                测试报告               |    20    |          |
|            Size Measurement           |               计算工作量               |    10    |          |
| Postmortem & Process Improvement Plan |           事后总结，并提出过程改进计划          |    60    |          |
|                                       |                 合计                |          |          |

## III. 解题思路

数独是一种数学逻辑游戏，游戏由 9 × 9 个格子组成，玩家需要根据格子提供的数字推理出其他格子的数字。本次项目要求：

- 生成不重复的数独终局至文件，要求数独左上角数字恒为：`(3 + 0) % 9 + 1 = 4`
- 读取文件中的数独问题，求解并将结果输出至文件

### 3.1 生成数独

经过我在网上的查阅资料，我发现目前生成数独的算法一共有这样的几种：

1.  暴力搜索 ＋ 回溯法
2.  矩阵变换法
3.  全排列平移法

首先我排除了「暴力搜索 + 回溯」的生成数独终局的方法，因为经过资料的对比，相比于另外的两种方法，暴力搜索效率低下，对于 1,000,000 个要求的数独生成数据量来说显得尤为不合适。

另外的一种矩阵变换方法，我参考了这篇文章 - [数独终盘生成的几种方法](https://my.oschina.net/wangmengjun/blog/781984)。**其主要思路在于选择一个初始种子数独，通过在合适范围内进行行、列与数字的随机次数的随机交换来生成我们所要的数独终局**。这种方法不仅效率较高，实现比较方便，最终生成的终局两两匹配度也很低，**于是我首先选择了利用矩阵变换的方法进行功能实现。**

### 3.2 求解数独

前期的初步搜索中，我发现大多数中文资料下求解数独的方法几乎都是「回溯法」和「舞蹈链 - 精确覆盖问题」这两种算法。

其中，解题过程我参考了：

- [暴力算法之美：如何在 1 毫秒内解决数独问题？| 暴力枚举法+深度优先搜索 POJ 2982](https://zhuanlan.zhihu.com/p/31865810?utm_source=qq&utm_medium=social)
- [Sudoku solving algorithms - Wikipedia](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms)
- [舞蹈链 - 维基百科](https://zh.wikipedia.org/wiki/%E8%88%9E%E8%B9%88%E9%93%BE)
- [使用 Dancing Links 算法求解数独](https://www.jianshu.com/p/93b52c37cc65)

等等资料。经过分析，我觉得对于求解数独来讲，最暴力的 **深度优先搜索与回溯的结合** 这种方法比较合适，在之后的实现过程我也先采用了这样的办法。

## IV. 设计实现

本次项目：

- 我选择使用 Python 进行实现，在 Windows 平台进行代码编写，在 Windows 和 Linux 平台进行测试
- 我利用 `git` 进行代码的版本控制，代码托管在 GitHub
- 我利用 `pylint` 对代码进行质量分析检查，利用 [Codacy](https://www.codacy.com/app/spencerwooo/Sudoku?utm_source=github.com&utm_medium=referral&utm_content=spencerwooo/Sudoku&utm_campaign=Badge_Grade) 平台对代码质量进行持续分析监测
- 我利用 `cProfile` 对代码进行性能分析，利用 `gprof2dot` 生成性能分析报告
- 我利用 Python 内建模块 `unittest` 进行单元测试，并利用 `Coverage.py` 测试分支覆盖率等指标，并通过 Codacy API 将结果同步至 Codacy 平台持续集成

本次项目的博客：

- 我选择利用 [VuePress](https://vuepress.vuejs.org/) 生成项目博客，来记录我的开发历程
- 为了部署方便，我利用 [Travis CI](https://travis-ci.org/) 持续集成我的博客内容，并利用 [GitHub Pages](https://pages.github.com/) 托管我博客的静态文件

### 4.1 项目结构

本次项目我托管在 GitHub，利用 `git` 进行版本控制。项目三个分支：

![](https://i.loli.net/2018/12/06/5c09197e3b1ff.png)

- `master` 分支托管数独主程序的源代码、单元测试与性能测试相关文件等
- `docs` 分支托管博客的源代码与持续集成 CI 配置文件
- `gh-pages` 分支托管博客的静态文件，GitHub Pages 在此分支进行构建

其中的主程序 `master` 分支结构与功能：

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
│   ├── __init__.py
│   ├── create_sudoku.py
│   ├── main.py
│   ├── solve-me.txt
│   ├── solve_sudoku.py
│   └── sudoku.txt
└── tests
    └── README.md

3 directories, 13 files
```

- 🐍 `sudoku/`：Python 主程序源码文件夹，程序入口为 `main.py`
- 🔍 `tests/`：单元测试用例
- 🚀 `performance/`：性能测试结果（包括原二进制文件与生成的性能测试图鉴）

### 4.2 代码设计

:::warning 注意
此处代码设计为最初未优化性能的版本，其中：

- 生成数独终局：采用了 **矩阵变换算法**
- 解决数独：采用了 **未剪枝的深度优先搜索与回溯** 的算法

有很大的改进空间，详见「性能改进」。
:::

项目建立了共三个文件：

- `main.py`：程序入口，处理输入参数、文件输出与异常情况
- `create_sudoku.py`：内含类 `GenerateSudoku`
- `solve_sudoku.py`：内含类 `SolveSudoku`

共两个类：

- `GenerateSudoku`:
  - `__init__()`：初始化函数
  - `swap_row(row1, row2)`：交换合适的两行
  - `swap_col(col1, col2)`：交换合适的两列
  - `swap_num(num1, num2)`：交换随机的两个数字
  - `generate_candidate()`：生成最终的数独终局
- `SolveSudoku`:
  - `__init__(sudoku_path)`：初始化函数，传入待解决数独文件路径
  - `solving_sudoku(sudoku)`：深度优先搜索解决数独问题主函数
  - `num_is_candidate(sudoku, num, row, col)`：判断传入数字能否填入相应的位置
  - `find_that_blank(sudoku, current)`：寻找剩余数独内是否还有未填入的空位

相关的包、UML 类图如下所示：

![](https://i.loli.net/2018/12/07/5c0a6bc5882bc.png)

数独模块的入口流程图如下所示：

![](https://i.loli.net/2018/12/07/5c0a75f8a00d9.png)

生成数独 `GenerateSudoku` 和求解数独 `SolveSudoku` 两个模块的流程图如下所示：

> 差个图。

## V. 性能改进

我通过 Python 性能分析模块 `cProfile` 生成了程序的性能总览二进制文件，利用 `gprof2dot` 将性能分析报告生成图片如下所示：

![](https://i.loli.net/2018/12/07/5c09fa4e3ebc4.png)

可以看到，针对「求解数独」这个问题，最耗时间的模块依旧是主运行模块 `solving_sudoku()` 这个方法。当然是由于算法「未剪枝的深度优先搜索与回溯」限制，这里性能瓶颈也就显现出来了。

## VI. 代码细节

### 6.1 生成数独的算法 —— 矩阵变换法

### 6.2 求解数独的算法 —— 精确剪枝、行列块约束下的深度优先搜索算法

## VII. 项目总结

🚧 通过这个项目...