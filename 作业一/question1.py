"""
第一题：语言串接
实现两个语言的串接操作 L1L2 = {xy | x ∈ L1, y ∈ L2}
"""

from common.language import Language


def main():
    print("=" * 60)
    print("第一题：语言串接")
    print("=" * 60)
    
    # 定义语言L1（至少3个字符串）
    L1 = Language({"a", "ab", "abc"})
    print(f"\nL1 = {L1}")
    print(f"L1包含 {len(L1)} 个字符串")
    
    # 定义语言L2（至少3个字符串）
    L2 = Language({"x", "xy", "xyz"})
    print(f"\nL2 = {L2}")
    print(f"L2包含 {len(L2)} 个字符串")
    
    # 计算串接 L1L2
    print("\n" + "-" * 60)
    print("计算串接 L1L2...")
    print("-" * 60)
    
    L1L2 = L1.concatenate(L2)
    
    print(f"\nL1L2 = {L1L2}")
    print(f"L1L2包含 {len(L1L2)} 个字符串")
    
    # 详细列出所有串接结果
    print("\n串接结果详细列表：")
    sorted_strings = sorted(L1L2.strings, key=lambda s: (len(s), s))
    for i, s in enumerate(sorted_strings, 1):
        print(f"  {i}. {s}")
    
    # 额外测试：更复杂的语言
    print("\n" + "=" * 60)
    print("额外测试：更复杂的语言串接")
    print("=" * 60)
    
    L3 = Language({"", "a", "b", "ab"})  # 包含空字符串
    L4 = Language({"0", "1", "01"})
    
    print(f"\nL3 = {L3}")
    print(f"L3包含 {len(L3)} 个字符串（包括空字符串ε）")
    
    print(f"\nL4 = {L4}")
    print(f"L4包含 {len(L4)} 个字符串")
    
    L3L4 = L3.concatenate(L4)
    
    print(f"\nL3L4 = {L3L4}")
    print(f"L3L4包含 {len(L3L4)} 个字符串")
    
    print("\n串接结果详细列表：")
    sorted_strings = sorted(L3L4.strings, key=lambda s: (len(s), s))
    for i, s in enumerate(sorted_strings, 1):
        display_s = 'ε' + s if s and '' in L3.strings else s
        # 显示原始组合
        for x in L3.strings:
            for y in L4.strings:
                if x + y == s:
                    x_display = 'ε' if x == '' else x
                    print(f"  {i}. {s if s else 'ε':<6} (来自 {x_display} + {y})")
                    break
            else:
                continue
            break
    
    print("\n" + "=" * 60)
    print("第一题完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
