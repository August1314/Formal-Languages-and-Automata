"""
第四题：子集构造算法
将NFA转换为等价的DFA
"""

from common.nfa import NFA


def create_nfa():
    """
    创建课件中的NFA
    基于课件lec2-nfa的转移表
    """
    states = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    alphabet = {'r', 'b'}
    
    # 转移函数（基于课件转移表）
    transitions = {
        1: {
            'r': {2, 4},
            'b': {5}
        },
        2: {
            'r': {4, 6},
            'b': {1, 3, 5}
        },
        3: {
            'r': {2, 6},
            'b': {5}
        },
        4: {
            'r': {2, 8},
            'b': {1, 5, 7}
        },
        5: {
            'r': {2, 4, 6, 8},
            'b': {1, 3, 7, 9}
        },
        6: {
            'r': {2, 8},
            'b': {3, 5, 9}
        },
        7: {
            'r': {4, 8},
            'b': {5}
        },
        8: {
            'r': {4, 6},
            'b': {5, 7, 9}
        },
        9: {
            'r': {6, 8},
            'b': {5}
        }
    }
    
    start_state = 1
    accept_states = {9}
    
    return NFA(states, alphabet, transitions, start_state, accept_states)


def print_nfa_info(nfa):
    """打印NFA信息"""
    print("\nNFA定义：")
    print(f"  状态集合 Q = {nfa.states}")
    print(f"  字母表 Σ = {nfa.alphabet}")
    print(f"  起始状态 q0 = {nfa.start_state}")
    print(f"  接受状态 F = {nfa.accept_states}")
    print("\n  转移函数 δ:")
    for state in sorted(nfa.states):
        if state in nfa.transitions:
            for symbol in sorted(nfa.alphabet):
                if symbol in nfa.transitions[state]:
                    next_states = nfa.transitions[state][symbol]
                    next_states_str = '{' + ', '.join(map(str, sorted(next_states))) + '}'
                    print(f"    δ({state}, {symbol}) = {next_states_str}")


def print_dfa_info(dfa):
    """打印DFA信息"""
    print("\nDFA定义：")
    print(f"  状态数量: {len(dfa.states)}")
    
    # 格式化状态显示
    def format_state(state):
        if isinstance(state, frozenset):
            if not state:
                return '∅'
            return '{' + ', '.join(map(str, sorted(state))) + '}'
        return str(state)
    
    print(f"  起始状态: {format_state(dfa.start_state)}")
    print(f"  接受状态数量: {len(dfa.accept_states)}")
    
    print("\n  接受状态:")
    for state in sorted(dfa.accept_states, key=lambda s: sorted(s)):
        print(f"    {format_state(state)}")
    
    print("\n  DFA转移表:")
    print("  " + "-" * 70)
    print(f"  {'状态':<30} | {'r':<18} | {'b':<18}")
    print("  " + "-" * 70)
    
    # 按状态排序（按集合大小和内容）
    sorted_states = sorted(dfa.states, key=lambda s: (len(s), sorted(s)))
    
    for state in sorted_states:
        state_str = format_state(state)
        
        # 标记起始状态和接受状态
        marker = ""
        if state == dfa.start_state:
            marker += "→"
        if state in dfa.accept_states:
            marker += "*"
        if marker:
            state_str = f"{marker} {state_str}"
        
        if state in dfa.transitions:
            r_next = format_state(dfa.transitions[state].get('r', frozenset()))
            b_next = format_state(dfa.transitions[state].get('b', frozenset()))
            print(f"  {state_str:<30} | {r_next:<18} | {b_next:<18}")
    
    print("  " + "-" * 70)
    print("  说明: → 表示起始状态, * 表示接受状态")


def main():
    print("=" * 70)
    print("第四题：子集构造算法（NFA转DFA）")
    print("=" * 70)
    
    # 创建NFA
    nfa = create_nfa()
    print_nfa_info(nfa)
    
    print("\n" + "=" * 70)
    print("执行子集构造算法...")
    print("=" * 70)
    
    # 转换为DFA
    dfa = nfa.to_dfa()
    
    print_dfa_info(dfa)
    
    # 测试一些字符串
    print("\n" + "=" * 70)
    print("测试字符串（验证NFA和DFA等价性）")
    print("=" * 70)
    
    test_strings = ["r", "b", "rr", "rb", "br", "bb", "rrb", "rbr"]
    
    print(f"\n  {'字符串':<10} | {'NFA结果':<10} | {'DFA结果':<10} | {'一致性'}")
    print("  " + "-" * 50)
    
    for s in test_strings:
        nfa_result = nfa.accepts(s)
        dfa_result = dfa.accepts(s)
        match = "✓" if nfa_result == dfa_result else "✗"
        
        nfa_str = "接受" if nfa_result else "拒绝"
        dfa_str = "接受" if dfa_result else "拒绝"
        
        print(f"  {s:<10} | {nfa_str:<10} | {dfa_str:<10} | {match}")
    
    print("\n" + "=" * 70)
    print("第四题完成")
    print("=" * 70)


if __name__ == "__main__":
    main()
