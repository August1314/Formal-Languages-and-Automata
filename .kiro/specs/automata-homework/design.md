# 设计文档

## 概述

本设计文档描述了形式语言与自动机作业的实现方案。系统将实现四个主要功能模块：语言串接、星操作、DFA模拟和NFA到DFA转换。每个模块都将作为独立的Python函数实现，并包含测试用例。

## 架构

### 系统架构

```
作业一/
├── common/
│   ├── __init__.py
│   ├── language.py          # 可复用的语言操作类
│   ├── dfa.py               # 可复用的DFA类
│   └── nfa.py               # 可复用的NFA类
├── question1.py             # 第一题：语言串接
├── question2.py             # 第二题：星操作
├── question3.py             # 第三题：DFA模拟
└── question4.py             # 第四题：子集构造
```

### 模块职责

**common/language.py** - 语言操作工具类（可复用）
- Language类：封装语言的基本操作
- 串接操作
- 星操作
- 并集、交集等操作

**common/dfa.py** - DFA类（可复用）
- DFA类：封装DFA的定义和操作
- 转移函数delta
- 扩展转移函数Edelta
- 字符串接受判断
- 可视化转移过程

**common/nfa.py** - NFA类（可复用）
- NFA类：封装NFA的定义和操作
- 转移函数
- 字符串接受判断
- 转换为DFA（子集构造算法）

**question1.py** - 第一题独立实现
- 使用common.language模块
- 定义测试用例
- 打印结果

**question2.py** - 第二题独立实现
- 使用common.language模块
- 定义测试用例
- 打印结果

**question3.py** - 第三题独立实现
- 使用common.dfa模块
- 定义课件中的DFA
- 测试正例和负例

**question4.py** - 第四题独立实现
- 使用common.nfa模块
- 定义课件中的NFA
- 执行子集构造算法
- 打印DFA转移表

## 组件和接口

### 1. common/language.py - 语言操作类（可复用）

**类定义:**
```python
class Language:
    def __init__(self, strings: set):
        """初始化语言"""
        self.strings = strings
    
    def concatenate(self, other: 'Language') -> 'Language':
        """语言串接操作"""
        pass
    
    def star(self, max_length: int) -> 'Language':
        """上界为max_length的星操作"""
        pass
    
    def union(self, other: 'Language') -> 'Language':
        """语言并集"""
        pass
    
    def __str__(self) -> str:
        """字符串表示"""
        pass
```

**功能描述:**
- concatenate：实现L1L2串接操作
- star：实现上界为T的星操作，包含空字符串
- union：实现语言并集（可能用于后续扩展）

### 2. common/dfa.py - DFA类（可复用）

**类定义:**
```python
class DFA:
    def __init__(self, states: set, alphabet: set, transitions: dict, 
                 start_state, accept_states: set):
        """初始化DFA"""
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions  # dict[state][symbol] -> state
        self.start_state = start_state
        self.accept_states = accept_states
    
    def delta(self, q, a):
        """单步转移函数"""
        pass
    
    def extended_delta(self, q, s, verbose=False):
        """扩展转移函数，verbose=True时打印每步转移"""
        pass
    
    def accepts(self, s: str) -> bool:
        """判断字符串是否被接受"""
        pass
```

**DFA定义（基于课件图片）:**
- 状态集合：Q = {'A', 'B', 'C'}
- 字母表：Σ = {'0', '1'}
- 起始状态：q0 = 'A'
- 接受状态：F = {'A', 'B'}
- 转移函数：
  - δ(A, 0) = A
  - δ(A, 1) = B
  - δ(B, 0) = A
  - δ(B, 1) = C
  - δ(C, 0) = C
  - δ(C, 1) = C

### 3. common/nfa.py - NFA类（可复用）

**类定义:**
```python
class NFA:
    def __init__(self, states: set, alphabet: set, transitions: dict,
                 start_state, accept_states: set):
        """初始化NFA"""
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions  # dict[state][symbol] -> set of states
        self.start_state = start_state
        self.accept_states = accept_states
    
    def accepts(self, s: str) -> bool:
        """判断字符串是否被接受"""
        pass
    
    def to_dfa(self) -> 'DFA':
        """子集构造算法：将NFA转换为等价的DFA"""
        pass
    
    def _move(self, states: set, symbol: str) -> set:
        """计算状态集合在读入symbol后的转移"""
        pass
```

**NFA定义（基于课件转移表）:**
- 状态集合：Q = {1, 2, 3, 4, 5, 6, 7, 8, 9}
- 字母表：Σ = {'r', 'b'}
- 起始状态：q0 = 1
- 接受状态：F = {9}
- 转移函数（从图片读取）：
  - δ(1, r) = {2, 4}, δ(1, b) = {5}
  - δ(2, r) = {4, 6}, δ(2, b) = {1, 3, 5}
  - δ(3, r) = {2, 6}, δ(3, b) = {5}
  - δ(4, r) = {2, 8}, δ(4, b) = {1, 5, 7}
  - δ(5, r) = {2, 4, 6, 8}, δ(5, b) = {1, 3, 7, 9}
  - δ(6, r) = {2, 8}, δ(6, b) = {3, 5, 9}
  - δ(7, r) = {4, 8}, δ(7, b) = {5}
  - δ(8, r) = {4, 6}, δ(8, b) = {5, 7, 9}
  - δ(9, r) = {6, 8}, δ(9, b) = {5}

### 4. question1.py - 第一题实现

**功能:**
- 导入Language类
- 定义L1和L2（各至少3个字符串）
- 调用concatenate方法
- 打印结果

**测试用例:**
- L1 = {"a", "ab", "abc"}
- L2 = {"x", "xy", "xyz"}

### 5. question2.py - 第二题实现

**功能:**
- 导入Language类
- 定义L（至少2个字符串）
- 调用star方法，T=3
- 打印结果

**测试用例:**
- L = {"0", "1"}
- T = 3

### 6. question3.py - 第三题实现

**功能:**
- 导入DFA类
- 定义课件中的DFA
- 定义正例Sp和负例Sn（各至少3个字符）
- 调用extended_delta，verbose=True
- 打印每步转移

**测试用例:**
- 正例：Sp = "0101"（不含连续两个1）
- 负例：Sn = "011"（包含连续两个1）

### 7. question4.py - 第四题实现

**功能:**
- 导入NFA类
- 定义课件中的NFA
- 调用to_dfa方法
- 打印生成的DFA转移表

**输出格式:**
- 打印DFA的状态集合
- 打印DFA的转移表
- 标识起始状态和接受状态

## 数据模型

### 语言表示
- 使用Python的set类型表示语言（字符串集合）
- 字符串使用str类型

### 自动机表示
- 状态：使用字符串或整数表示
- 转移函数：使用嵌套字典表示
  - DFA: `dict[state][symbol] -> state`
  - NFA: `dict[state][symbol] -> set of states`
- DFA状态集合：使用frozenset表示（可哈希）

## 错误处理

### 输入验证
- 验证语言集合不为空
- 验证上界T为正整数
- 验证输入字符串只包含字母表中的字符
- 验证状态和符号在自动机定义中存在

### 异常处理
```python
# 示例
def delta(q, a):
    if q not in transitions:
        raise ValueError(f"状态 {q} 不存在")
    if a not in transitions[q]:
        raise ValueError(f"从状态 {q} 没有字符 {a} 的转移")
    return transitions[q][a]
```

## 测试策略

### 单元测试
- 每个函数都有独立的测试函数
- 测试正常情况和边界情况

### 集成测试
- 测试完整的执行流程
- 验证输出格式符合作业要求

### 测试用例设计原则
1. 语言串接：测试不同大小的语言
2. 星操作：测试不同的T值（0, 1, 2, 3）
3. DFA：测试接受和拒绝的字符串
4. 子集构造：验证生成的DFA与原NFA等价

## 输出格式

### 打印格式要求
1. 每道题的输出清晰分隔
2. 使用中文标题和说明
3. DFA转移过程逐步打印
4. 子集构造算法打印转移表

### 示例输出格式
```
========== 第一题：语言串接 ==========
L1 = {'a', 'ab', 'abc'}
L2 = {'x', 'xy', 'xyz'}
L1L2 = {'ax', 'axy', 'axyz', ...}

========== 第二题：星操作 ==========
L = {'0', '1'}
T = 3
S_3(L) = {'ε', '0', '1', '00', ...}

========== 第三题：DFA模拟 ==========
正例字符串: "0101"
A --0--> A
A --1--> B
B --0--> A
A --1--> B
最终状态: B (拒绝)

========== 第四题：子集构造 ==========
DFA转移表:
状态 {1} --r--> {2, 4}
状态 {1} --b--> {5}
...
```

## 实现注意事项

1. **代码组织**：
   - 可复用组件放在common/目录下
   - 每道题目独立的Python文件
   - 便于后续课程中继续使用这些组件

2. **注释**：每个函数添加中文注释说明功能

3. **可读性**：使用有意义的变量名

4. **效率**：对于星操作，注意避免生成过多字符串

5. **正确性**：仔细核对DFA和NFA的转移表定义

6. **可复用性**：
   - Language类可用于后续语言操作相关作业
   - DFA类可用于后续DFA相关作业
   - NFA类可用于后续NFA相关作业和转换算法

7. **提交方式**：
   - 可以将common/目录和所有question*.py文件一起打包提交
   - 或者将common/中的代码复制到每个question文件中（如果要求单文件提交）
