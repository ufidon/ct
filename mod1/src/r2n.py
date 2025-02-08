from collections import defaultdict
from graphviz import Digraph

class NFA:
    """Represents an NFA."""
    def __init__(self):
        self.transitions = defaultdict(lambda: defaultdict(set))
        self.start_state = None
        self.accept_states = set()

    def add_transition(self, from_state, symbol, to_state):
        """Adds a transition to the NFA."""
        self.transitions[from_state][symbol].add(to_state)

    def epsilon_closure(self, states):
        """Computes the epsilon closure of a set of states."""
        stack = list(states)
        closure = set(states)

        while stack:
            state = stack.pop()
            for next_state in self.transitions[state].get('ε', set()):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

def nfa_to_dfa(nfa):
    """Converts an NFA to a DFA using the subset construction algorithm, ensuring full transitions."""
    dfa_transitions = {}
    dfa_start = frozenset(nfa.epsilon_closure({nfa.start_state}))
    dfa_states = {dfa_start}
    unprocessed = [dfa_start]
    dfa_accept_states = set()
    alphabet = set()  # Collect all input symbols from the NFA

    # Find all symbols in the NFA
    for state in nfa.transitions:
        for symbol in nfa.transitions[state]:
            if symbol != 'ε':
                alphabet.add(symbol)

    trap_state = frozenset({'TRAP'})  # Define a trap state

    while unprocessed:
        dfa_state = unprocessed.pop()
        dfa_transitions[dfa_state] = {}

        for symbol in alphabet:
            new_state = frozenset(nfa.epsilon_closure(set().union(
                *[nfa.transitions[s][symbol] for s in dfa_state if symbol in nfa.transitions[s]]
            )))

            if not new_state:
                new_state = trap_state  # Send missing transitions to TRAP

            if new_state not in dfa_states:
                dfa_states.add(new_state)
                unprocessed.append(new_state)

            dfa_transitions[dfa_state][symbol] = new_state

            if any(state in nfa.accept_states for state in new_state):
                dfa_accept_states.add(new_state)

    # Ensure the trap state transitions to itself for all symbols
    dfa_transitions[trap_state] = {symbol: trap_state for symbol in alphabet}

    return dfa_start, dfa_transitions, dfa_accept_states

def visualize_dfa(dfa_start, dfa_transitions, dfa_accept_states):
    """Generates a Graphviz visualization of the DFA."""
    dot = Digraph(format='png')
    state_map = {state: f"Q{i}" for i, state in enumerate(dfa_transitions)}

    for state, transitions in dfa_transitions.items():
        shape = "doublecircle" if state in dfa_accept_states else "circle"
        dot.node(state_map[state], shape=shape)

        for symbol, next_state in transitions.items():
            dot.edge(state_map[state], state_map[next_state], label=symbol)

    dot.render("dfa_visualization", view=True)

if __name__ == '__main__':
  # Example: Convert NFA to DFA for "a(a+b)*b"
  nfa = NFA()
  nfa.start_state = 0
  nfa.accept_states = {6}

  # Define transitions for NFA of a(a+b)*b
  nfa.add_transition(0, 'a', 1)
  nfa.add_transition(1, 'ε', 2)
  nfa.add_transition(1, 'ε', 3)
  nfa.add_transition(1, 'ε', 4)
  nfa.add_transition(2, 'a', 4)
  nfa.add_transition(3, 'b', 4)
  nfa.add_transition(4, 'ε', 1)
  nfa.add_transition(4, 'ε', 5)
  nfa.add_transition(5, 'b', 6)

  # Convert to DFA and visualize
  dfa_start, dfa_transitions, dfa_accept_states = nfa_to_dfa(nfa)
  visualize_dfa(dfa_start, dfa_transitions, dfa_accept_states)