"""
第二题：星操作
实现上界为T的星操作 S_T(L) = {w1w2...wn | n <= T, 每个wi ∈ L}
"""

from common.language import Language


def main():
    print("=" * 60)
    print("第二题：上界为T的星操作")
    print("=" * 60)
    
    # 定义语言L（至少2个字符串）
    L = Language({"0", "1"})
    print(f"\nL = {L}")
    print(f"L包含 {len(L)} 个字符串")
    
    # 设置上界T
    T = 3
    print(f"\n上界 T = {T}")
    
    # 计算星操作 S_T(L)
    print("\n" + "-" * 60)
    print(f"计算星操作 S_{T}(L)...")
    print("-" * 60)
    
    S_T_L = L.star(T)
    
    print(f"\nS_{T}(L) = {S_T_L}")
    print(f"S_{T}(L)包含 {len(S_T_L)} 个字符串")
    
    # 验证包含空字符串
    if '' in S_T_L.strings:
        print("\n✓ 结果包含空字符串 ε")
    
    # 按长度分组显示结果
    print("\n按长度分组的结果：")
    
    # 按长度分组
    by_length = {}
    for s in S_T_L.strings:
        length = len(s)
        if length not in by_length:
            by_length[length] = []
        by_length[length].append(s if s else 'ε')
    
    # 按长度排序显示
    for length in sorted(by_length.keys()):
        strings = sorted(by_length[length])
        print(f"  长度 {length}: {{{', '.join(strings)}}} ({len(strings)}个)")
    
    # 额外测试：更复杂的语言和更大的上界
    print("\n" + "=" * 60)
    print("额外测试：更复杂的语言")
    print("=" * 60)
    
    L2 = Language({"a", "b", "c"})
    T2 = 2
    
    print(f"\nL2 = {L2}")
    print(f"L2包含 {len(L2)} 个字符串")
    print(f"\n上界 T = {T2}")
    
    print("\n" + "-" * 60)
    print(f"计算星操作 S_{T2}(L2)...")
    print("-" * 60)
    
    S_T2_L2 = L2.star(T2)
    
    print(f"\nS_{T2}(L2) = {S_T2_L2}")
    print(f"S_{T2}(L2)包含 {len(S_T2_L2)} 个字符串")
    
    # 验证数量
    expected_count = sum(3**i for i in range(T2 + 1))
    print(f"\n预期数量: 3^0 + 3^1 + 3^2 = 1 + 3 + 9 = {expected_count}")
    print(f"实际数量: {len(S_T2_L2)}")
    print(f"验证: {'✓ 正确' if len(S_T2_L2) == expected_count else '✗ 错误'}")
    
    # 按长度分组显示
    print("\n按长度分组的结果：")
    by_length = {}
    for s in S_T2_L2.strings:
        length = len(s)
        if length not in by_length:
            by_length[length] = []
        by_length[length].append(s if s else 'ε')
    
    for length in sorted(by_length.keys()):
        strings = sorted(by_length[length])
        print(f"  长度 {length}: {{{', '.join(strings)}}} ({len(strings)}个)")
    
    print("\n" + "=" * 60)
    print("第二题完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
