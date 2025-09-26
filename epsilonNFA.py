class EpsilonNFADebug:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        """
        初始化带调试功能的 ε-NFA
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
    
    def epsilon_closure(self, states, debug=False):
        """计算给定状态集的ε闭包，支持调试"""
        closure = set(states)
        stack = list(states)
        
        if debug:
            print(f"  计算ε闭包，初始状态: {states}")
        
        while stack:
            state = stack.pop()
            # 检查是否有ε转移
            if state in self.transitions and 'ε' in self.transitions[state]:
                epsilon_transitions = self.transitions[state]['ε']
                for next_state in epsilon_transitions:
                    if next_state not in closure:
                        if debug:
                            print(f"    状态 {state} --ε--> {next_state}")
                        closure.add(next_state)
                        stack.append(next_state)
        
        if debug:
            print(f"  ε闭包结果: {closure}")
        
        return closure
    
    def is_accept(self, input_string, debug=False):
        """检查输入字符串是否被ε-NFA接受，支持调试模式"""
        if debug:
            print("=" * 60)
            print(f"ε-NFA 开始处理输入: '{input_string}'")
            print("=" * 60)
        
        # 从起始状态的ε闭包开始
        current_states = self.epsilon_closure({self.start_state}, debug)
        
        if debug:
            print(f"初始ε闭包: {current_states}")
            print("-" * 40)
        
        # 处理每个输入字符
        for i, char in enumerate(input_string):
            if debug:
                print(f"\n步骤 {i+1}: 处理字符 '{char}'")
                print(f"当前状态集合: {current_states}")
            
            # 第一步：从当前状态集合通过输入字符转移
            next_states = set()
            for state in current_states:
                if state in self.transitions and char in self.transitions[state]:
                    transition_result = self.transitions[state][char]
                    next_states |= transition_result
                    if debug:
                        print(f"  状态 {state} --'{char}'--> {transition_result}")
                else:
                    if debug:
                        print(f"  状态 {state} --'{char}'--> 无转移定义")
            
            if debug:
                print(f"字符转移后状态集合: {next_states}")
            
            # 第二步：计算新状态集的ε闭包
            current_states = self.epsilon_closure(next_states, debug)
            
            if debug:
                print(f"ε闭包后状态集合: {current_states}")
                print("-" * 40)
        
        # 检查最终状态集合中是否有接受状态
        final_result = any(state in self.accept_states for state in current_states)
        
        if debug:
            print("\n" + "=" * 60)
            print("处理完成")
            print(f"最终状态集合: {current_states}")
            print(f"接受状态: {self.accept_states}")
            print(f"是否有接受状态: {final_result}")
            print("=" * 60)
        
        return final_result

# 创建示例ε-NFA
def create_sample_epsilon_nfa_debug():
    states = {'q0', 'q1', 'q2', 'q3', 'q4'}
    alphabet = {'a', 'b', 'c'}
    
    # 定义转移函数（包含ε转移）
    transitions = {
        'q0': {
            'ε': {'q1', 'q3'}
        },
        'q1': {
            'a': {'q2'},
            'ε': {'q1'}  # 自循环ε转移
        },
        'q2': {
            'ε': {'q1'},  # 回到q1
            'b': {'q4'}
        },
        'q3': {
            'c': {'q4'}
        }
    }
    
    start_state = 'q0'
    accept_states = {'q4'}
    
    return EpsilonNFADebug(states, alphabet, transitions, start_state, accept_states)

# 测试带调试的ε-NFA
print("ε-NFA 调试演示")
print("=" * 60)
epsilon_nfa_debug = create_sample_epsilon_nfa_debug()

# 测试几个字符串
test_cases = ["ab", "c", "ac"]
for test_str in test_cases:
    result = epsilon_nfa_debug.is_accept(test_str, debug=True)
    print(f"\n最终结果: 字符串 '{test_str}' {'被接受' if result else '被拒绝'}")
    print("=" * 60 + "\n")