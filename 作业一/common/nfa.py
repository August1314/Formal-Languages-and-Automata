"""
NFA类 - 非确定性有限自动机的可复用组件
支持状态转移、字符串接受判断、转换为DFA等操作
"""

from .dfa import DFA


class NFA:
    """非确定性有限自动机（Nondeterministic Finite Automaton）"""
    
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        """
        初始化NFA
        
        参数:
            states: 状态集合（set）
            alphabet: 输入字母表（set）
            transitions: 转移函数（dict[state][symbol] -> set of states）
            start_state: 起始状态
            accept_states: 接受状态集合（set）
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
    
    def _move(self, states, symbol):
        """
        计算状态集合在读入symbol后的转移
        
        参数:
            states: 当前状态集合（set）
            symbol: 输入符号
            
        返回:
            转移后的状态集合（set）
        """
        result = set()
        for state in states:
            if state in self.transitions and symbol in self.transitions[state]:
                result.update(self.transitions[state][symbol])
        return result
    
    def accepts(self, s):
        """
        判断字符串是否被NFA接受
        
        参数:
            s: 输入字符串
            
        返回:
            True如果字符串被接受，否则False
        """
        # 当前可能的状态集合
        current_states = {self.start_state}
        
        # 处理每个输入字符
        for char in s:
            current_states = self._move(current_states, char)
            # 如果没有可达状态，直接返回False
            if not current_states:
                return False
        
        # 检查最终状态集合中是否有接受状态
        return bool(current_states & self.accept_states)
    
    def to_dfa(self):
        """
        子集构造算法：将NFA转换为等价的DFA
        
        返回:
            等价的DFA对象
        """
        # DFA的状态是NFA状态的集合，使用frozenset表示（可哈希）
        dfa_start_state = frozenset({self.start_state})
        dfa_states = set()
        dfa_transitions = {}
        dfa_accept_states = set()
        
        # 使用队列处理未处理的DFA状态
        unprocessed = [dfa_start_state]
        processed = set()
        
        while unprocessed:
            current_dfa_state = unprocessed.pop(0)
            
            if current_dfa_state in processed:
                continue
            
            processed.add(current_dfa_state)
            dfa_states.add(current_dfa_state)
            
            # 检查是否为接受状态（包含NFA的接受状态）
            if current_dfa_state & self.accept_states:
                dfa_accept_states.add(current_dfa_state)
            
            # 初始化当前DFA状态的转移
            if current_dfa_state not in dfa_transitions:
                dfa_transitions[current_dfa_state] = {}
            
            # 对每个输入符号计算转移
            for symbol in self.alphabet:
                # 计算NFA状态集合在读入symbol后的转移
                next_nfa_states = self._move(set(current_dfa_state), symbol)
                next_dfa_state = frozenset(next_nfa_states)
                
                # 记录转移
                dfa_transitions[current_dfa_state][symbol] = next_dfa_state
                
                # 如果是新状态，加入待处理队列
                if next_dfa_state and next_dfa_state not in processed:
                    unprocessed.append(next_dfa_state)
                    dfa_states.add(next_dfa_state)
        
        # 创建并返回DFA对象
        return DFA(
            states=dfa_states,
            alphabet=self.alphabet,
            transitions=dfa_transitions,
            start_state=dfa_start_state,
            accept_states=dfa_accept_states
        )
    
    def __str__(self):
        """字符串表示"""
        return f"NFA(states={self.states}, start={self.start_state}, accept={self.accept_states})"
    
    def __repr__(self):
        """对象表示"""
        return self.__str__()
