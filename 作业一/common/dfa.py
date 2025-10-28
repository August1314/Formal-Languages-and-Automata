"""
DFA类 - 确定性有限自动机的可复用组件
支持状态转移、字符串接受判断等操作
"""


class DFA:
    """确定性有限自动机（Deterministic Finite Automaton）"""
    
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        """
        初始化DFA
        
        参数:
            states: 状态集合（set）
            alphabet: 输入字母表（set）
            transitions: 转移函数（dict[state][symbol] -> state）
            start_state: 起始状态
            accept_states: 接受状态集合（set）
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
    
    def delta(self, q, a):
        """
        单步转移函数 δ(q, a)
        
        参数:
            q: 当前状态
            a: 输入字符
            
        返回:
            下一个状态
            
        异常:
            ValueError: 如果状态或字符不存在，或转移未定义
        """
        if q not in self.states:
            raise ValueError(f"状态 {q} 不在状态集合中")
        
        if a not in self.alphabet:
            raise ValueError(f"字符 {a} 不在字母表中")
        
        if q not in self.transitions or a not in self.transitions[q]:
            raise ValueError(f"从状态 {q} 读入字符 {a} 的转移未定义")
        
        return self.transitions[q][a]
    
    def extended_delta(self, q, s, verbose=False):
        """
        扩展转移函数 δ*(q, s)
        处理字符串s，返回最终状态
        
        参数:
            q: 起始状态
            s: 输入字符串
            verbose: 是否打印每步转移过程
            
        返回:
            最终状态
        """
        current_state = q
        
        if verbose:
            print(f"起始状态: {current_state}")
        
        for i, char in enumerate(s):
            next_state = self.delta(current_state, char)
            if verbose:
                print(f"{current_state} --{char}--> {next_state}")
            current_state = next_state
        
        if verbose:
            print(f"最终状态: {current_state}")
        
        return current_state
    
    def accepts(self, s):
        """
        判断字符串是否被DFA接受
        
        参数:
            s: 输入字符串
            
        返回:
            True如果字符串被接受，否则False
        """
        try:
            final_state = self.extended_delta(self.start_state, s)
            return final_state in self.accept_states
        except ValueError:
            return False
    
    def __str__(self):
        """字符串表示"""
        return f"DFA(states={self.states}, start={self.start_state}, accept={self.accept_states})"
    
    def __repr__(self):
        """对象表示"""
        return self.__str__()
