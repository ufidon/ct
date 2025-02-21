from graphviz import Digraph
from collections import defaultdict, deque

# 状态类
class 状态:
    """表示NFA中的一个状态"""
    def __init__(self):
        self.转移 = {}  # {字符: set(下一状态)}
        self.ε转移 = set()  # ε转移（空转移）

# NFA类
class NFA:
    """表示NFA，包含起始状态和接受状态"""
    def __init__(self, 起始状态, 接受状态):
        self.起始状态 = 起始状态
        self.接受状态 = 接受状态

# DFA类
class DFA:
    """表示DFA，包含状态集、字母表等"""
    def __init__(self, 状态集, 字母表, 转移规则, 起始状态, 接受状态集):
        self.状态集 = 状态集
        self.字母表 = 字母表
        self.转移规则 = 转移规则  # {状态: {字符: 下一状态}}
        self.起始状态 = 起始状态
        self.接受状态集 = set(接受状态集)

# Thompson构造：后缀表达式转NFA
def 后缀转NFA(后缀表达式):
    """使用Thompson构造法将后缀正则表达式转换为NFA"""
    栈 = []
    操作符 = {'+', '*', '⋅'}
    for 标记 in 后缀表达式:
        if 标记 not in 操作符:  # 单个字符NFA
            起始 = 状态()
            接受 = 状态()
            起始.转移[标记] = {接受}
            栈.append(NFA(起始, 接受))
        elif 标记 == "⋅":  # 连接
            nfa2 = 栈.pop()
            nfa1 = 栈.pop()
            nfa1.接受状态.ε转移.add(nfa2.起始状态)
            栈.append(NFA(nfa1.起始状态, nfa2.接受状态))
        elif 标记 == "+":  # 并集
            nfa2 = 栈.pop()
            nfa1 = 栈.pop()
            起始 = 状态()
            接受 = 状态()
            起始.ε转移.update({nfa1.起始状态, nfa2.起始状态})
            nfa1.接受状态.ε转移.add(接受)
            nfa2.接受状态.ε转移.add(接受)
            栈.append(NFA(起始, 接受))
        elif 标记 == "*":  # 闭包
            nfa = 栈.pop()
            起始 = 状态()
            接受 = 状态()
            起始.ε转移.update({nfa.起始状态, 接受})
            nfa.接受状态.ε转移.update({nfa.起始状态, 接受})
            栈.append(NFA(起始, 接受))
    return 栈.pop()

# 计算ε闭包
def ε闭包(状态集):
    """计算给定状态集的ε闭包"""
    结果 = set(状态集)
    队列 = deque(状态集)
    while 队列:
        当前状态 = 队列.popleft()
        for 下一状态 in 当前状态.ε转移:
            if 下一状态 not in 结果:
                结果.add(下一状态)
                队列.append(下一状态)
    return 结果

# NFA转DFA（子集构造法）
def NFA转DFA(nfa, 字母表):
    """将NFA转换为DFA"""
    状态映射 = {}  # 子集到DFA状态编号的映射
    未处理 = deque()  # 未处理的DFA状态（子集）
    DFA状态集 = set()
    DFA转移规则 = defaultdict(dict)
    DFA接受状态集 = set()

    # 初始状态为起始状态的ε闭包
    起始子集 = frozenset(ε闭包({nfa.起始状态}))
    状态映射[起始子集] = 0
    未处理.append(起始子集)
    DFA状态集.add(0)
    if nfa.接受状态 in 起始子集:
        DFA接受状态集.add(0)

    while 未处理:
        当前子集 = 未处理.popleft()
        当前状态号 = 状态映射[当前子集]

        for 字符 in 字母表:
            下一子集 = set()
            for 状态 in 当前子集:
                if 字符 in 状态.转移:
                    下一子集.update(状态.转移[字符])
            下一子集 = frozenset(ε闭包(下一子集))

            if 下一子集:
                if 下一子集 not in 状态映射:
                    新状态号 = len(状态映射)
                    状态映射[下一子集] = 新状态号
                    未处理.append(下一子集)
                    DFA状态集.add(新状态号)
                    if nfa.接受状态 in 下一子集:
                        DFA接受状态集.add(新状态号)
                DFA转移规则[当前状态号][字符] = 状态映射[下一子集]

    return DFA(DFA状态集, 字母表, DFA转移规则, 0, DFA接受状态集)

# Hopcroft最小化DFA
def 最小化DFA(dfa):
    """使用Hopcroft算法最小化DFA"""
    分组 = [dfa.接受状态集, dfa.状态集 - dfa.接受状态集]
    分组 = [g for g in 分组 if g]
    队列 = deque()

    for 字符 in dfa.字母表:
        最小组 = min(分组, key=len)
        队列.append((最小组, 字符))

    反向转移 = defaultdict(list)
    for 状态 in dfa.状态集:
        for 字符, 下一状态 in dfa.转移规则[状态].items():
            反向转移[(下一状态, 字符)].append(状态)

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
            if 子组1 and 子组2:
                新分组.append(子组1)
                新分组.append(子组2)
                for 字符b in dfa.字母表:
                    较小组 = 子组1 if len(子组1) <= len(子组2) else 子组2
                    队列.append((较小组, 字符b))
            else:
                新分组.append(组)
        分组 = 新分组

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
            if 字符 in dfa.转移规则[代表状态]:  # 检查转移是否存在
                下一状态 = dfa.转移规则[代表状态][字符]
                新转移规则[组号][字符] = 状态到组[下一状态]

    return DFA(新状态集, dfa.字母表, 新转移规则, 新起始状态, 新接受状态集)

# 可视化NFA
def 可视化NFA(nfa, 文件名="nfa可视化"):
    """生成NFA的Graphviz可视化图：起始状态虚线，接受状态实线双圈，其余实线单圈"""
    图 = Digraph(format='png')
    状态映射 = {}
    队列 = [nfa.起始状态]
    状态编号 = 0

    while 队列:
        当前状态 = 队列.pop(0)
        if 当前状态 not in 状态映射:
            状态映射[当前状态] = f"q{状态编号}"
            状态编号 += 1
            # 设置节点样式
            if 当前状态 == nfa.起始状态:
                图.node(状态映射[当前状态], shape="circle", style="dashed")  # 起始状态虚线
            elif 当前状态 == nfa.接受状态:
                图.node(状态映射[当前状态], shape="doublecircle")  # 接受状态实线双圈
            else:
                图.node(状态映射[当前状态], shape="circle")  # 其余状态实线单圈

        for 字符, 下一状态集 in 当前状态.转移.items():
            for 下一状态 in 下一状态集:
                if 下一状态 not in 状态映射:
                    状态映射[下一状态] = f"q{状态编号}"
                    状态编号 += 1
                    队列.append(下一状态)
                图.edge(状态映射[当前状态], 状态映射[下一状态], label=字符)

        for 下一状态 in 当前状态.ε转移:
            if 下一状态 not in 状态映射:
                状态映射[下一状态] = f"q{状态编号}"
                状态编号 += 1
                队列.append(下一状态)
            图.edge(状态映射[当前状态], 状态映射[下一状态], label="ε", style="dashed")

    图.render(文件名, view=True)

# 可视化DFA
def 可视化DFA(dfa, 文件名="dfa可视化"):
    """生成DFA的Graphviz可视化图：起始状态虚线，接受状态实线双圈，其余实线单圈"""
    图 = Digraph(format='png')
    for 状态 in dfa.状态集:
        # 设置节点样式
        if 状态 == dfa.起始状态:
            图.node(str(状态), shape="circle", style="dashed")  # 起始状态虚线
        elif 状态 in dfa.接受状态集:
            图.node(str(状态), shape="doublecircle")  # 接受状态实线双圈
        else:
            图.node(str(状态), shape="circle")  # 其余状态实线单圈

    for 状态 in dfa.转移规则:
        for 字符, 下一状态 in dfa.转移规则[状态].items():
            图.edge(str(状态), str(下一状态), label=字符)

    图.render(文件名, view=True)

# 主函数测试
if __name__ == "__main__":
    # 后缀表达式 = "ab+"
    字母表 = {'a', 'b'}  # 手动指定字母表，避免操作符干扰

    后缀表达式 = "αab+*⋅b⋅虫🦆⋅*⋅"
    字母表 = {'α','a', 'b', '虫', '🦆'}  # 手动指定字母表，避免操作符干扰

    # 构造NFA并可视化
    nfa = 后缀转NFA(后缀表达式)
    可视化NFA(nfa, "nfa可视化")

    # NFA转DFA并可视化
    dfa = NFA转DFA(nfa, 字母表)
    可视化DFA(dfa, "中间DFA")

    # 最小化DFA并可视化
    最小dfa = 最小化DFA(dfa)
    可视化DFA(最小dfa, "最小DFA")