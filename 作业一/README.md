# 形式语言与自动机 - 第一次Python编程作业

## 项目结构

```
作业一/
├── common/                    # 可复用组件包
│   ├── __init__.py           # 包初始化文件
│   ├── language.py           # Language类：语言操作
│   ├── dfa.py                # DFA类：确定性有限自动机
│   └── nfa.py                # NFA类：非确定性有限自动机
├── question1.py              # 第一题：语言串接
├── question2.py              # 第二题：星操作
├── question3.py              # 第三题：DFA模拟
├── question4.py              # 第四题：子集构造算法
└── README.md                 # 本文件

```

## 运行方式

### 使用conda环境（推荐）

```bash
# 激活ml环境
conda activate ml

# 运行各题
python 作业一/question1.py
python 作业一/question2.py
python 作业一/question3.py
python 作业一/question4.py
```

### 直接运行

```bash
python question1.py
python question2.py
python question3.py
python question4.py
```

## 各题说明

### 第一题：语言串接

**功能**: 实现两个语言的串接操作 L1L2 = {xy | x ∈ L1, y ∈ L2}

**测试用例**:
- 基本测试：L1 = {"a", "ab", "abc"}, L2 = {"x", "xy", "xyz"}
  - 结果包含9个字符串
- 额外测试：L3 = {ε, "a", "b", "ab"}, L4 = {"0", "1", "01"}
  - 结果包含12个字符串
  - 验证空字符串的单位元性质

**运行结果**: ✓ 通过

### 第二题：星操作

**功能**: 实现上界为T的星操作 S_T(L) = {w1w2...wn | n <= T, 每个wi ∈ L}

**测试用例**:
- 基本测试：L = {"0", "1"}, T = 3
  - 结果包含15个字符串（包括空字符串ε）
- 额外测试：L2 = {"a", "b", "c"}, T = 2
  - 结果包含13个字符串
  - 验证等比数列求和公式：(3^3 - 1) / (3 - 1) = 13

**运行结果**: ✓ 通过

### 第三题：DFA模拟

**功能**: 实现DFA的转移函数delta和扩展转移函数Edelta

**DFA定义**:
- 接受不含两个连续1的所有0/1串
- 状态: {A, B, C}
- 接受状态: {A, B}

**测试用例**:
- 正例: "0101" → 接受 ✓
- 负例: "011" → 拒绝 ✓

**运行结果**: ✓ 通过

### 第四题：子集构造算法

**功能**: 将NFA转换为等价的DFA

**NFA定义**:
- 9个状态 (1-9)
- 字母表: {r, b}
- 接受状态: {9}

**转换结果**:
- 生成7个DFA状态
- 2个接受状态
- NFA和DFA等价性验证通过 ✓

**运行结果**: ✓ 通过

## 可复用组件说明

### Language类 (common/language.py)

提供语言操作的基本功能：
- `concatenate(other)`: 语言串接
- `star(max_length)`: 上界为T的星操作
- `union(other)`: 语言并集

### DFA类 (common/dfa.py)

提供DFA的完整实现：
- `delta(q, a)`: 单步转移函数
- `extended_delta(q, s, verbose)`: 扩展转移函数
- `accepts(s)`: 判断字符串是否被接受

### NFA类 (common/nfa.py)

提供NFA的完整实现：
- `accepts(s)`: 判断字符串是否被接受
- `to_dfa()`: 子集构造算法，转换为DFA
- `_move(states, symbol)`: 计算状态集合的转移

## 测试结果总结

所有四道题目均已实现并通过测试：

✓ 第一题：语言串接 - 正确生成9个串接结果  
✓ 第二题：星操作 - 正确生成15个字符串（包含空串）  
✓ 第三题：DFA模拟 - 正确接受/拒绝测试字符串  
✓ 第四题：子集构造 - 成功将NFA转换为等价DFA  

## 作者信息

- 课程：形式语言与自动机
- 作业：第一次Python编程作业
- 完成日期：2025年
