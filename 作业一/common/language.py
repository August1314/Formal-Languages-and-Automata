"""
Language类 - 形式语言操作的可复用组件
支持语言串接、星操作等基本操作
"""


class Language:
    """表示形式语言（字符串集合）的类"""
    
    def __init__(self, strings):
        """
        初始化语言
        
        参数:
            strings: 字符串集合（set或list）
        """
        if isinstance(strings, set):
            self.strings = strings
        else:
            self.strings = set(strings)
    
    def concatenate(self, other):
        """
        语言串接操作：L1L2 = {xy | x ∈ L1, y ∈ L2}
        
        参数:
            other: 另一个Language对象
            
        返回:
            新的Language对象，包含所有可能的串接结果
        """
        result = set()
        for x in self.strings:
            for y in other.strings:
                result.add(x + y)
        return Language(result)
    
    def star(self, max_length):
        """
        上界为T的星操作：S_T(L) = {w1w2...wn | n <= T, 每个wi ∈ L}
        
        参数:
            max_length: 上界T，串接的最大次数
            
        返回:
            新的Language对象，包含所有长度不超过T的串接组合
        """
        # 初始化结果集合，包含空字符串
        result = {''}
        
        # 当前层的字符串集合（初始为空字符串）
        current_level = {''}
        
        # 逐层生成，从1到max_length
        for i in range(max_length):
            next_level = set()
            # 对当前层的每个字符串，与L中的每个字符串串接
            for s in current_level:
                for w in self.strings:
                    next_level.add(s + w)
            # 将新生成的字符串加入结果集
            result.update(next_level)
            # 更新当前层
            current_level = next_level
        
        return Language(result)
    
    def union(self, other):
        """
        语言并集操作：L1 ∪ L2
        
        参数:
            other: 另一个Language对象
            
        返回:
            新的Language对象，包含两个语言的并集
        """
        return Language(self.strings | other.strings)
    
    def __str__(self):
        """
        字符串表示
        
        返回:
            格式化的字符串，显示语言中的所有字符串
        """
        if not self.strings:
            return '{}'
        
        # 将字符串排序后显示（空字符串用ε表示）
        sorted_strings = sorted(self.strings, key=lambda s: (len(s), s))
        display_strings = ['ε' if s == '' else s for s in sorted_strings]
        
        return '{' + ', '.join(display_strings) + '}'
    
    def __repr__(self):
        """对象表示"""
        return f'Language({self.strings})'
    
    def __len__(self):
        """返回语言中字符串的个数"""
        return len(self.strings)
