from graphviz import Digraph

class 状态:
    """表示NFA中的一个状态"""
    def __init__(self):
        self.转移 = {}  # {字符: set(下一状态)}
        self.ε转移 = set()  # ε转移（空转移）

class NFA:
    """表示NFA，包含起始状态和接受状态"""
    def __init__(self, 起始状态, 接受状态):
        self.起始状态 = 起始状态
        self.接受状态 = 接受状态

def 后缀转NFA(后缀表达式):
    """使用Thompson构造法将后缀正则表达式转换为NFA"""
    栈 = []
    操作符 = {'+', '*', '⋅'}
    for 标记 in 后缀表达式:
        if 标记 not in 操作符:  # 单个字符NFA
            起始 = 状态()
            接受 = 状态()
            起始.转移[标记] = {接受}  # 在`标记`上的单次转移
            栈.append(NFA(起始, 接受))

        elif 标记 == "⋅":  # 连接操作
            nfa2 = 栈.pop()
            nfa1 = 栈.pop()
            nfa1.接受状态.ε转移.add(nfa2.起始状态)
            栈.append(NFA(nfa1.起始状态, nfa2.接受状态))

        elif 标记 == "+":  # 并集（选择）
            nfa2 = 栈.pop()
            nfa1 = 栈.pop()
            起始 = 状态()
            接受 = 状态()
            起始.ε转移.update({nfa1.起始状态, nfa2.起始状态})
            nfa1.接受状态.ε转移.add(接受)
            nfa2.接受状态.ε转移.add(接受)
            栈.append(NFA(起始, 接受))

        elif 标记 == "*":  # 闭包（Kleene星）
            nfa = 栈.pop()
            起始 = 状态()
            接受 = 状态()
            起始.ε转移.update({nfa.起始状态, 接受})
            nfa.接受状态.ε转移.update({nfa.起始状态, 接受})
            栈.append(NFA(起始, 接受))

    return 栈.pop()  # 返回最终NFA

def 可视化NFA(nfa):
    """生成NFA的Graphviz可视化图"""
    图 = Digraph(format='png')
    
    状态映射 = {}  # 状态对象到唯一标签的映射
    队列 = [nfa.起始状态]
    状态编号 = 0

    while 队列:
        当前状态 = 队列.pop(0)

        if 当前状态 not in 状态映射:
            状态映射[当前状态] = f"q{状态编号}"
            状态编号 += 1

            # 添加节点到图中
            形状 = "doublecircle" if 当前状态 == nfa.接受状态 else "circle"
            图.node(状态映射[当前状态], shape=形状)

        # 处理普通转移
        for 字符, 下一状态集 in 当前状态.转移.items():
            for 下一状态 in 下一状态集:
                if 下一状态 not in 状态映射:
                    状态映射[下一状态] = f"q{状态编号}"
                    状态编号 += 1
                    队列.append(下一状态)
                图.edge(状态映射[当前状态], 状态映射[下一状态], label=字符)

        # 处理ε转移
        for 下一状态 in 当前状态.ε转移:
            if 下一状态 not in 状态映射:
                状态映射[下一状态] = f"q{状态编号}"
                状态编号 += 1
                队列.append(下一状态)
            图.edge(状态映射[当前状态], 状态映射[下一状态], label="ε", style="dashed")

    # 保存并显示图
    图.render("nfa可视化", view=True)

if __name__ == "__main__":
    后缀表达式 = "αab+*⋅b⋅虫🦆⋅*⋅"
    nfa = 后缀转NFA(后缀表达式)
    可视化NFA(nfa)