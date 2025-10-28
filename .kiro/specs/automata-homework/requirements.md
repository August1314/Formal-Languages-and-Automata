# 需求文档

## 简介

本项目旨在完成形式语言与自动机课程的第一次Python编程作业，包括实现语言串接、星操作、DFA转移函数和NFA到DFA的子集构造算法。

## 术语表

- **System**: 形式语言与自动机作业系统
- **Language**: 字符串集合
- **DFA**: 确定性有限自动机 (Deterministic Finite Automaton)
- **NFA**: 非确定性有限自动机 (Nondeterministic Finite Automaton)
- **Concatenation**: 语言串接操作
- **Star Operation**: 星操作
- **Delta Function**: 转移函数
- **Extended Delta Function**: 扩展转移函数
- **Subset Construction**: 子集构造算法

## 需求

### 需求 1: 语言串接功能

**用户故事:** 作为学生，我想要实现两个语言的串接操作，以便理解语言串接的概念并完成作业第一题。

#### 验收标准

1. THE System SHALL 实现一个接受两个语言L1和L2作为输入参数的串接函数
2. WHEN 调用串接函数时，THE System SHALL 返回包含所有可能的xy组合的新语言，其中x来自L1且y来自L2
3. THE System SHALL 使用至少包含3个字符串的L1和L2进行测试
4. THE System SHALL 打印串接函数返回的语言中的所有字符串
5. THE System SHALL 验证串接结果的正确性

### 需求 2: 星操作功能

**用户故事:** 作为学生，我想要实现上界为T的星操作，以便理解星操作的概念并完成作业第二题。

#### 验收标准

1. THE System SHALL 实现一个接受语言L和上界T作为输入参数的星操作函数
2. WHEN 调用星操作函数时，THE System SHALL 返回所有长度不超过T的字符串串接组合
3. THE System SHALL 使用至少包含2个字符串的语言L进行测试
4. WHEN T等于3时，THE System SHALL 打印星操作函数返回的语言中的所有字符串
5. THE System SHALL 包含空字符串作为星操作结果的一部分

### 需求 3: DFA转移函数实现

**用户故事:** 作为学生，我想要实现DFA的转移函数和扩展转移函数，以便模拟DFA的执行过程并完成作业第三题。

#### 验收标准

1. THE System SHALL 实现一个接受状态q和字符a作为参数的转移函数delta(q, a)
2. THE System SHALL 实现一个接受状态q和字符串s作为参数的扩展转移函数Edelta(q, s)
3. THE System SHALL 通过调用delta(q, a)来实现Edelta(q, s)
4. THE System SHALL 使用课件lec1-dfa中的DFA定义（接受不含两个连续1的字符串）
5. WHEN 测试DFA时，THE System SHALL 使用至少包含3个字符的正例字符串Sp
6. WHEN 测试DFA时，THE System SHALL 使用至少包含3个字符的负例字符串Sn
7. THE System SHALL 打印DFA处理Sp和Sn时的每一次状态转移

### 需求 4: NFA到DFA的子集构造算法

**用户故事:** 作为学生，我想要实现子集构造算法，以便将NFA转换为等价的DFA并完成作业第四题。

#### 验收标准

1. THE System SHALL 实现课件lec2-nfa中的子集构造算法
2. THE System SHALL 使用课件中给定的NFA转移表作为输入
3. WHEN 执行子集构造算法时，THE System SHALL 生成等价的DFA转移表
4. THE System SHALL 打印生成的DFA转移表
5. THE System SHALL 正确处理NFA中的非确定性转移
6. THE System SHALL 标识DFA中的起始状态和接受状态
