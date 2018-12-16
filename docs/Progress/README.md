---
sidebarDepth: 3
---

# 开发历程

## I. 项目地址

:::tip 项目地址与相关链接

-   GitHub 项目首页：<https://github.com/spencerwooo/Sudoku>
-   项目博客、README 主页：[https://spencerwoo.com/Sudoku](/)
-   **项目开发历程主页**：[https://spencerwoo.com/Sudoku/Progress](/Progress/)

**这里是项目要求的「解决项目的心路历程和收获」等开发历程内容页面。**
:::

## II. PSP

|                PSP 2.1                |   Personal Software Progress Stages    | 预估耗时（分钟） | 实际耗时（分钟） |
| :-----------------------------------: | :------------------------------------: | :--------------: | :--------------: |
|               Planning                |                  计划                  |        60        |        30        |
|               Estimate                |        估计这个任务需要多少时间        |       2500       |       3000       |
|              Development              |                  开发                  |       1500       |       1800       |
|               Analysis                |       需求分析（包括学习新技术）       |       500        |       500        |
|              Design Spec              |              生成设计文档              |        60        |        60        |
|             Design Review             |     设计复审（和同事审核设计文档）     |        30        |        30        |
|            Coding Standard            | 代码规范（为目前的开发制定合适的规范） |        30        |        30        |
|                Design                 |                具体设计                |       200        |       250        |
|                Coding                 |                具体编码                |       400        |       450        |
|              Code Review              |                代码复审                |        60        |        60        |
|                 Test                  |  测试（自我测试、修改代码、提交测试）  |       200        |       250        |
|               Reporting               |                  报告                  |        20        |        60        |
|              Test Report              |                测试报告                |        20        |        20        |
|           Size Measurement            |               计算工作量               |        10        |        10        |
| Postmortem & Process Improvement Plan |      事后总结，并提出过程改进计划      |        60        |        30        |
|                                       |                  合计                  |       3090       |       3580       |


## III. 解题思路

数独是一种数学逻辑游戏，游戏由 9 × 9 个格子组成，玩家需要根据格子提供的数字推理出其他格子的数字。本次项目要求：

-   生成不重复的数独终局至文件，要求数独左上角数字恒为：`(3 + 0) % 9 + 1 = 4`
-   读取文件中的数独问题，求解并将结果输出至文件

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

-   [暴力算法之美：如何在 1 毫秒内解决数独问题？| 暴力枚举法+深度优先搜索 POJ 2982](https://zhuanlan.zhihu.com/p/31865810?utm_source=qq&utm_medium=social)
-   [Sudoku solving algorithms - Wikipedia](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms)
-   [舞蹈链 - 维基百科](https://zh.wikipedia.org/wiki/%E8%88%9E%E8%B9%88%E9%93%BE)
-   [使用 Dancing Links 算法求解数独](https://www.jianshu.com/p/93b52c37cc65)

等等资料。经过分析，我觉得对于求解数独来讲，最暴力的 **深度优先搜索与回溯的结合** 这种方法比较合适，在之后的实现过程我也先采用了这样的办法。

## IV. 设计实现

本次项目：

-   我选择使用 Python 进行实现，在 Windows 平台进行代码编写，在 Windows 和 Linux 平台进行测试
-   我利用 `git` 进行代码的版本控制，代码托管在 GitHub
-   我利用 `pylint` 对代码进行质量分析检查，利用 [Codacy](https://www.codacy.com/app/spencerwooo/Sudoku?utm_source=github.com&utm_medium=referral&utm_content=spencerwooo/Sudoku&utm_campaign=Badge_Grade) 平台对代码质量进行持续分析监测：[![Codacy Badge](https://api.codacy.com/project/badge/Grade/af90b6b7da74437ca6b1b1b0eb0443cd)](https://www.codacy.com/app/spencerwooo/Sudoku?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=spencerwooo/Sudoku&amp;utm_campaign=Badge_Grade)
-   我利用 `cProfile` 对代码进行性能分析，利用 `gprof2dot` 生成性能分析报告
-   我设计了 [十组测试用例](https://github.com/spencerwooo/Sudoku/tree/master/tests) 进行单元测试，并利用 `Coverage.py` 测试分支覆盖率等指标，并通过 Codacy API 将结果同步至 [Codacy 平台](https://app.codacy.com/project/spencerwooo/Sudoku/dashboard) 持续集成：[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/af90b6b7da74437ca6b1b1b0eb0443cd)](https://www.codacy.com/app/spencerwooo/Sudoku?utm_source=github.com&utm_medium=referral&utm_content=spencerwooo/Sudoku&utm_campaign=Badge_Coverage)

本次项目的博客：

-   我选择利用 [VuePress](https://vuepress.vuejs.org/) 生成项目博客，来记录我的开发历程
-   为了部署方便，我利用 [Travis CI](https://travis-ci.org/) 持续集成我的博客内容，并利用 [GitHub Pages](https://pages.github.com/) 托管我博客的静态文件

### 4.1 项目结构

本次项目我托管在 GitHub，利用 `git` 进行版本控制。项目三个分支：

![](https://i.loli.net/2018/12/06/5c09197e3b1ff.png)

-   `master` 分支托管数独主程序的源代码、单元测试与性能测试相关文件等
-   `docs` 分支托管博客的源代码与持续集成 CI 配置文件
-   `gh-pages` 分支托管博客的静态文件，GitHub Pages 在此分支进行构建

其中的主程序 `master` 分支结构与功能：

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

-   🐍 `sudoku/`：Python 主程序源码文件夹，程序入口为 `main.py`
-   🔍 `tests/`：单元测试用例
-   🚀 `performance/`：性能测试结果（包括原二进制文件与生成的性能测试图鉴）

### 4.2 代码设计

:::warning 注意
此处代码设计为最初未优化性能的版本，其中：

-   生成数独终局：采用了 **矩阵变换算法**
-   解决数独：采用了 **未剪枝的深度优先搜索与回溯** 的算法

有很大的改进空间，详见「性能改进」。
:::

项目建立了共三个文件：

-   `main.py`：程序入口，处理输入参数、文件输出与异常情况
-   `create_sudoku.py`：内含类 `GenerateSudoku`
-   `solve_sudoku.py`：内含类 `SolveSudoku`

共两个类：

-   `GenerateSudoku`:
    -   `__init__()`：初始化函数
    -   `swap_row(row1, row2)`：交换合适的两行
    -   `swap_col(col1, col2)`：交换合适的两列
    -   `swap_num(num1, num2)`：交换随机的两个数字
    -   `generate_candidate()`：生成最终的数独终局
-   `SolveSudoku`:
    -   `__init__(sudoku_path)`：初始化函数，传入待解决数独文件路径
    -   `solving_sudoku(sudoku)`：深度优先搜索解决数独问题主函数
    -   `num_is_candidate(sudoku, num, row, col)`：判断传入数字能否填入相应的位置
    -   `find_that_blank(sudoku, current)`：寻找剩余数独内是否还有未填入的空位

相关的包、UML 类图如下所示：

![](https://i.loli.net/2018/12/07/5c0a6bc5882bc.png)

数独模块的入口流程图如下所示：

![](https://i.loli.net/2018/12/07/5c0a75f8a00d9.png)

生成数独 `GenerateSudoku` 和求解数独 `SolveSudoku` 两个模块的流程图如下所示：

![](https://i.loli.net/2018/12/08/5c0b61d0cca47.png)

## V. 性能改进

我通过 Python 性能分析模块 `cProfile` 生成了程序的性能总览二进制文件，利用 `gprof2dot` 将性能分析报告生成图片如下所示：

![](https://i.loli.net/2018/12/07/5c09fa4e3ebc4.png)

可以看到，针对「求解数独」这个问题，最耗时间的模块依旧是主运行模块 `solving_sudoku()` 这个方法。当然是由于算法「未剪枝的深度优先搜索与回溯」限制，这里性能瓶颈也就显现出来了。

一次偶然的机会，我在 LeetCode 平台看到了一个算法问题：「Sudoku Solver」，这道题目的需求和我们本次项目类似，也是输入数独求解题目。在这道题目的评论区我看到了这样的一只提交：[28ms python solution beats 100.0%](https://leetcode.com/problems/sudoku-solver/discuss/199974/28ms-python-solution-beats-100.0?tdsourcetag=s_pctim_aiomsg)，经过仔细的观察分析，我发现这只提交的算法设计十分巧妙，剪枝十分到位，由于篇幅，我在[「代码细节 - 求解数独的算法」](/Progress/#_6-2-求解数独)里面对这个方法进行详细剖析。

总之，我按照这只提交的算法设计从头攥写了我的 SolveSudoku 模块，进行了彻底的运算优化，并生成了相应的性能分析报告如下图：

![](https://i.loli.net/2018/12/09/5c0cc941a6cb4.png)

可以看到，虽然 `solving_sudoku()` 依旧是算法耗时最长的模块，但是相比上一次修改，这个模块运行效率有了显著的提升。直观的比较起来，我在 [项目 README 这里](/#性能测试数独用例) 附上了两个性能测试用例（下两图倒数第二三行）：第一个相对简单，用我最初的方法进行测试需要 5s 左右跑出结果；第二个则比较难，用我最初的算法需要跑近 150s：

![](https://i.loli.net/2018/12/09/5c0cc9e3b1836.png)

经过这次优化的结果：

![](https://i.loli.net/2018/12/09/5c0cc9ef2550d.png)

可以看到，经过优化，就算是最难的数独我们也能在一秒内解出答案。算法为王！💪

## VI. 代码细节

### 6.1 生成数独

> 算法 —— 矩阵变换法

矩阵变换的方法生成数独相对方便，其核心在于随机的交换相应的两行、两列和两个数字。我首先封装了行、列、数字交换的三个方法：

```python
# 交换两行
def swap_row(self, row1, row2):
  self.sudoku[[row1, row2]] = self.sudoku[[row2, row1]]

#交换两列
def swap_col(self, col1, col2):
  self.sudoku[:, [col1, col2]] = self.sudoku[:, [col2, col1]]

# 交换两个数字
def swap_num(self, num1, num2):
  for i in range(9):
    for j in range(9):
      if self.sudoku[i][j] == num1:
        self.sudoku[i][j] = num2
      elif self.sudoku[i][j] == num2:
        self.sudoku[i][j] = num1
```

之后，我随机选取合适的两行、两列和两个数字进行交换，生成最终的数独：

```python
def generate_candidate(self):
  # 根据要求：(3+0)/9+1=4, 左上角数字恒为 4
  num_seed = [1, 2, 3, 5, 6, 7, 8, 9]
  # 根据要求：其他行、列不能与第一行、第一列进行交换
  row_and_col_seed = [[1, 2], [3, 4, 5], [6, 7, 8]]
  for _ in range(10):
    random.shuffle(num_seed)
    random.shuffle(row_and_col_seed)
    random.shuffle([random.shuffle(seed) for seed in row_and_col_seed])
    self.swap_row(row_and_col_seed[0][0], row_and_col_seed[0][1])
    self.swap_col(row_and_col_seed[0][0], row_and_col_seed[0][1])
    self.swap_num(num_seed[0], num_seed[1])
```

### 6.2 求解数独

> 算法 —— 精确剪枝、行列块约束下的深度优先搜索算法

这里求解数独的算法精髓在于：**在行、列与 3x3 子块的约束下，确定当前块所能填入的候选数字集合。**

```python
def dfs(self, blank_in_sudoku, col_num, row_num, sqr_num, sudoku):
  # 判断当前数独是否还有未填入的空格
  if not blank_in_sudoku:
    return True

  max_possible_len = 9

  for (m, n) in blank_in_sudoku:
    candidate_num = row_num[m] & col_num[n] & sqr_num[m//3][n//3]
    if len(candidate_num) <= max_possible_len:
      max_possible_len = len(candidate_num)
      i, j = m, n

  if max_possible_len == 0:
    return False

  # 经过行、列、3x3 块约束，确定候选数字
  blank_in_sudoku.remove((i, j))
  candidate_num = row_num[i] & col_num[j] & sqr_num[i//3][j//3]

  for num in candidate_num:
    #填入数字，判断能否进行下一步的填写
    row_num[i].remove(num)
    col_num[j].remove(num)
    sqr_num[i//3][j//3].remove(num)
    sudoku[i][j] = num
    if self.dfs(blank_in_sudoku, col_num, row_num, sqr_num, sudoku):
      return True

    # 如果不能，回退，将当前格子赋 0
    sudoku[i][j] = 0
    row_num[i].add(num)
    col_num[j].add(num)
    sqr_num[i//3][j//3].add(num)

  blank_in_sudoku.add((i, j))
  return False
```

由于经过 **行、列和子块的约束**，当前块所能填入的候选数字变得极少，通过这样的方法进行深度优先搜索的算法就能极大提升运算效率。

## VII. 项目总结

通过这个一个月来的开发经历：

**针对算法实现方面：**

我更加熟悉了回溯、剪枝和深度优先搜索算法的精妙之处，能够更加熟练的对数独相关的算法进行求解和编写。同时，由于我使用 Python 进行实现，我也更加深刻的体会到 Python 这门语言的神奇、强大，简简单单的语法就能实现强有力的功能。在本次开发过程中我使用面向对象的思想进行编码，这也让我更加深入理解了面向对象的内涵所在。

**针对软件开发方面：**

从需求分析、解决问题、实际开发、性能测试、单元测试等等过程中，我更加熟悉了一款软件的真实开发过程是怎样的。这次的项目不仅让我对软件开发有了更深刻的了解、思考，还让我对一款软件从「能实现功能」就行，到要「注重性能」、要「进行测试」等等环节更加重视。这是软件工程开发的精髓所在。

本次项目除了让我熟悉编程语言、算法实现和开发工具以外，更重要的是让我理解一款软件从无到有的真正过程是怎样的，要经历怎样的测试、怎样的审核等等，这是这次项目带给我最精致的体验。
