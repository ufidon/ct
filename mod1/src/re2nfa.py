# https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b
# https://en.wikipedia.org/wiki/Thompson%27s_construction

from graphviz import Digraph

class State:
    """Represents a state in the NFA."""
    def __init__(self):
        self.transitions = {}  # {symbol: set(next_states)}
        self.epsilon_transitions = set()  # ε-transitions (empty moves)

class NFA:
    """Represents an NFA with start and accept states."""
    def __init__(self, start_state, accept_state):
        self.start_state = start_state
        self.accept_state = accept_state

def postfix_to_nfa(postfix_regex):
    """Converts a postfix regex to an NFA using Thompson's Construction."""
    stack = []
    operators = {'+', '*', '⋅'}
    for token in postfix_regex:
        if token not in operators:  # Single character NFA
            start = State()
            accept = State()
            start.transitions[token] = {accept}  # Single transition on `token`
            stack.append(NFA(start, accept))

        elif token == "⋅":  # Concatenation
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.accept_state.epsilon_transitions.add(nfa2.start_state)
            stack.append(NFA(nfa1.start_state, nfa2.accept_state))

        elif token == "+":  # Union (Alternation)
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            start = State()
            accept = State()
            start.epsilon_transitions.update({nfa1.start_state, nfa2.start_state})
            nfa1.accept_state.epsilon_transitions.add(accept)
            nfa2.accept_state.epsilon_transitions.add(accept)
            stack.append(NFA(start, accept))

        elif token == "*":  # Kleene Star
            nfa = stack.pop()
            start = State()
            accept = State()
            start.epsilon_transitions.update({nfa.start_state, accept})
            nfa.accept_state.epsilon_transitions.update({nfa.start_state, accept})
            stack.append(NFA(start, accept))

    return stack.pop()  # Final NFA

def visualize_nfa(nfa):
    """Generates a Graphviz visualization of the NFA."""
    dot = Digraph(format='png')
    
    state_map = {}  # Map state objects to unique labels
    queue = [nfa.start_state]
    state_id = 0

    while queue:
        state = queue.pop(0)

        if state not in state_map:
            state_map[state] = f"q{state_id}"
            state_id += 1

            # Add node to graph
            shape = "doublecircle" if state == nfa.accept_state else "circle"
            dot.node(state_map[state], shape=shape)

        # Process regular transitions
        for symbol, next_states in state.transitions.items():
            for next_state in next_states:
                if next_state not in state_map:
                    state_map[next_state] = f"q{state_id}"
                    state_id += 1
                    queue.append(next_state)
                dot.edge(state_map[state], state_map[next_state], label=symbol)

        # Process ε-transitions
        for next_state in state.epsilon_transitions:
            if next_state not in state_map:
                state_map[next_state] = f"q{state_id}"
                state_id += 1
                queue.append(next_state)
            dot.edge(state_map[state], state_map[next_state], label="ε", style="dashed")

    # Save and display the graph
    dot.render("corrected_nfa_visualization", view=True)



if __name__ == "__main__":
  postfix_regex = "αab+*⋅b⋅虫🦆⋅*⋅"

  nfa = postfix_to_nfa(postfix_regex)
  visualize_nfa(nfa)