"""
第三题：DFA模拟
实现DFA的转移函数delta和扩展转移函数Edelta
DFA接受不含两个连续1的所有0/1串
"""

from common.dfa import DFA


def create_dfa():
    """
    创建课件中的DFA
    接受不含两个连续1的所有0/1串
    
    状态说明：
    - A: 起始状态，上一个字符不是1（或刚开始）
    - B: 上一个字符是1
    - C: 陷阱状态，已经出现连续两个1
    """
    states = {'A', 'B', 'C'}
    alphabet = {'0', '1'}
    
    # 转移函数
    transitions = {
        'A': {
            '0': 'A',  # 读0，保持在A
            '1': 'B'   # 读1，转到B
        },
        'B': {
            '0': 'A',  # 读0，回到A
            '1': 'C'   # 读1，出现连续两个1，转到陷阱状态C
        },
        'C': {
            '0': 'C',  # 陷阱状态，读任何字符都保持在C
            '1': 'C'
        }
    }
    
    start_state = 'A'
    accept_states = {'A', 'B'}  # A和B是接受状态
    
    return DFA(states, alphabet, transitions, start_state, accept_states)


def test_string(dfa, test_str, description):
    """
    测试字符串是否被DFA接受
    
    参数:
        dfa: DFA对象
        test_str: 测试字符串
        description: 字符串描述
    """
    print(f"\n{description}: \"{test_str}\"")
    print("-" * 60)
    
    # 使用扩展转移函数，打印每步转移
    final_state = dfa.extended_delta(dfa.start_state, test_str, verbose=True)
    
    # 判断是否接受
    is_accepted = final_state in dfa.accept_states
    result = "接受 ✓" if is_accepted else "拒绝 ✗"
    
    print(f"结果: {result}")
    print("-" * 60)


def main():
    print("=" * 60)
    print("第三题：DFA模拟")
    print("=" * 60)
    
    # 创建DFA
    dfa = create_dfa()
    
    print("\nDFA定义：")
    print(f"  状态集合 Q = {dfa.states}")
    print(f"  字母表 Σ = {dfa.alphabet}")
    print(f"  起始状态 q0 = {dfa.start_state}")
    print(f"  接受状态 F = {dfa.accept_states}")
    print("\n  转移函数 δ:")
    for state in sorted(dfa.states):
        for symbol in sorted(dfa.alphabet):
            next_state = dfa.transitions[state][symbol]
            print(f"    δ({state}, {symbol}) = {next_state}")
    
    print("\n" + "=" * 60)
    print("测试字符串")
    print("=" * 60)
    
    # 正例：不含连续两个1的字符串（至少3个字符）
    Sp = "0101"
    test_string(dfa, Sp, "正例字符串")
    
    # 负例：包含连续两个1的字符串（至少3个字符）
    Sn = "011"
    test_string(dfa, Sn, "负例字符串")
    
    # 额外测试用例
    print("\n" + "=" * 60)
    print("额外测试用例")
    print("=" * 60)
    
    additional_tests = [
        ("000", "全是0"),
        ("010", "不含连续1"),
        ("110", "开头就是连续1"),
        ("0110", "中间有连续1"),
    ]
    
    for test_str, desc in additional_tests:
        is_accepted = dfa.accepts(test_str)
        result = "接受 ✓" if is_accepted else "拒绝 ✗"
        print(f"  \"{test_str}\" ({desc}): {result}")
    
    print("\n" + "=" * 60)
    print("第三题完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
