from collections import defaultdict, deque

class DFA:
    def __init__(self, 状态集, 字母表, 转移规则, 起始状态, 接受状态集):
        self.状态集 = 状态集
        self.字母表 = 字母表
        self.转移规则 = 转移规则  # {状态: {字符: 下一状态}}
        self.起始状态 = 起始状态
        self.接受状态集 = set(接受状态集)

def 最小化DFA(dfa):
    """Hopcroft算法最小化DFA"""
    # 初始划分
    分组 = [dfa.接受状态集, dfa.状态集 - dfa.接受状态集]
    分组 = [g for g in 分组 if g]  # 移除空组
    队列 = deque()  # 工作队列，存 (状态组, 字符)

    # 初始化队列
    for 字符 in dfa.字母表:
        最小组 = min(分组, key=len)
        队列.append((最小组, 字符))

    # 反向转移表
    反向转移 = defaultdict(list)
    for 状态 in dfa.状态集:
        for 字符, 下一状态 in dfa.转移规则[状态].items():
            反向转移[(下一状态, 字符)].append(状态)

    # 迭代细化
    while 队列:
        当前组, 字符 = 队列.popleft()
        受影响状态 = set()
        for 状态 in 当前组:
            for 前状态 in 反向转移[(状态, 字符)]:
                受影响状态.add(前状态)

        新分组 = []
        for 组 in 分组:
            子组1 = 组 & 受影响状态
            子组2 = 组 - 受影响状态
            if 子组1 and 子组2:  # 分割
                新分组.append(子组1)
                新分组.append(子组2)
                for 字符b in dfa.字母表:
                    较小组 = 子组1 if len(子组1) <= len(子组2) else 子组2
                    队列.append((较小组, 字符b))
            else:
                新分组.append(组)
        分组 = 新分组

    # 构造最小DFA
    状态到组 = {}
    for 序号, 组 in enumerate(分组):
        for 状态 in 组:
            状态到组[状态] = 序号

    新状态集 = set(range(len(分组)))
    新转移规则 = defaultdict(dict)
    新起始状态 = 状态到组[dfa.起始状态]
    新接受状态集 = set()

    for 组号, 组 in enumerate(分组):
        代表状态 = next(iter(组))
        if 代表状态 in dfa.接受状态集:
            新接受状态集.add(组号)
        for 字符 in dfa.字母表:
            下一状态 = dfa.转移规则[代表状态][字符]
            新转移规则[组号][字符] = 状态到组[下一状态]

    return DFA(新状态集, dfa.字母表, 新转移规则, 新起始状态, 新接受状态集)

# 打印DFA
def 打印DFA(dfa, 名称="DFA"):
    print(f"{名称}:")
    print(f"状态集: {dfa.状态集}")
    print(f"字母表: {dfa.字母表}")
    print("转移规则:")
    for 状态 in dfa.状态集:
        for 字符, 下一状态 in dfa.转移规则[状态].items():
            print(f"  δ({状态}, {字符}) = {下一状态}")
    print(f"起始状态: {dfa.起始状态}")
    print(f"接受状态集: {dfa.接受状态集}\n")

# 示例：L = {w | w 以 1 结尾}
def 示例():
    状态集 = {0, 1, 2}
    字母表 = {'0', '1'}
    转移规则 = {
        0: {'0': 1, '1': 2},
        1: {'0': 1, '1': 2},
        2: {'0': 1, '1': 2}
    }
    起始状态 = 0
    接受状态集 = {2}

    dfa = DFA(状态集, 字母表, 转移规则, 起始状态, 接受状态集)
    打印DFA(dfa, "原始DFA")

    新dfa = 最小化DFA(dfa)
    打印DFA(新dfa, "最小化DFA")

if __name__ == "__main__":
    示例()