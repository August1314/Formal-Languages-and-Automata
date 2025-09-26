class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        """
        初始化 NFA
        :param states: 状态集合（set）
        :param alphabet: 输入字母表（set）
        :param transitions: 转移函数 dict[state][symbol] -> set of states
        :param start_state: 起始状态
        :param accept_states: 接受状态集合（set）
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
    
    def is_accept(self, input_string):
        """检查输入字符串是否被NFA接受"""
        # 当前可能的状态集合
        current_states = {self.start_state}
        
        # 处理每个输入字符
        for char in input_string:
            next_states = set()
            for state in current_states:
                # 获取从当前状态读入字符后的转移状态
                if state in self.transitions and char in self.transitions[state]:
                    next_states |= self.transitions[state][char] #这里是一个 { }
                # 如果没有定义转移，则保持空集
            current_states = next_states
        
        # 检查最终状态集合中是否有接受状态
        return any(state in self.accept_states for state in current_states)

# 示例：创建一个接受以"01"结尾的字符串的NFA
def create_sample_nfa():
    states = {'q0', 'q1', 'q2'}
    alphabet = {'0', '1'}
    
    # 定义转移函数
    transitions = {
        'q0': {
            '0': {'q0', 'q1'},
            '1': {'q0'}
        },
        'q1': {
            '1': {'q2'}
        }
    }
    
    start_state = 'q0'
    accept_states = {'q2'}
    
    return NFA(states, alphabet, transitions, start_state, accept_states)

# 示例：创建一个接受包含"01"的字符串的NFA
def create_sample_nfa1():
    states = {'q0', 'q1', 'q2'}
    alphabet = {'0', '1'}
    
    # 定义转移函数
    transitions = {
        'q0': {
            '0': {'q0', 'q1'},  # 读到0，可以继续找或开始检测
            '1': {'q0'}         # 读到1，继续寻找
        },
        'q1': {
            '0': {'q1'},        # 读到0，保持在等待1的状态
            '1': {'q2'}         # 读到1，成功检测到01
        },
        'q2': {
            '0': {'q2'},        # 一旦检测到01，接受所有后续字符
            '1': {'q2'}         # 因为已经满足条件
        }
    }
    
    start_state = 'q0'
    accept_states = {'q2'}
    
    return NFA(states, alphabet, transitions, start_state, accept_states)

# 测试NFA
nfa = create_sample_nfa1()
test_strings = ["01", "001", "101", "0101", "1001", "11"]
print("NFA测试结果:")
for test_str in test_strings:
    result = nfa.is_accept(test_str)
    print(f"'{test_str}': {'接受' if result else '拒绝'}")