from collections import defaultdict, deque

class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states  # State set Q
        self.alphabet = alphabet  # Alphabet Σ
        self.transitions = transitions  # Transition function δ: {state: {symbol: next_state}}
        self.start_state = start_state  # Start state q0
        self.accept_states = set(accept_states)  # Accept state set F

def hopcroft_minimization(dfa):
    """Implement DFA minimization using Hopcroft's algorithm"""
    # Step 1: Initialize partition
    P = [dfa.accept_states, dfa.states - dfa.accept_states]  # Split into accept and non-accept states
    P = [p for p in P if p]  # Remove empty sets
    W = deque()  # Work queue to store (state set, symbol) pairs

    # Step 2: Initialize queue
    for a in dfa.alphabet:
        # Add each initial partition and symbol to queue (choose the smaller set)
        smaller_set = min(P, key=len)
        W.append((smaller_set, a))

    # Inverse transition for quick lookup
    inverse_trans = defaultdict(list)
    for state in dfa.states:
        for symbol, next_state in dfa.transitions[state].items():
            inverse_trans[(next_state, symbol)].append(state)

    # Step 3: Iteratively refine partitions
    while W:
        S, a = W.popleft()  # Take (S, a) from queue
        affected_states = set()
        # Find all states transitioning to S
        for s in S:
            for prev_state in inverse_trans[(s, a)]:
                affected_states.add(prev_state)

        # Check if each partition group needs splitting
        new_P = []
        for group in P:
            P1 = group & affected_states  # Part transitioning to S
            P2 = group - affected_states  # Part not transitioning to S
            if P1 and P2:  # If split occurs
                new_P.append(P1)
                new_P.append(P2)
                # Add smaller subset to queue
                for b in dfa.alphabet:
                    smaller = P1 if len(P1) <= len(P2) else P2
                    W.append((smaller, b))
            else:
                new_P.append(group)
        P = new_P

    # Step 4: Construct minimized DFA
    # Mapping from states to partition groups
    state_to_group = {}
    for i, group in enumerate(P):
        for state in group:
            state_to_group[state] = i

    # New state set
    new_states = set(range(len(P)))
    new_transitions = defaultdict(dict)
    new_start = state_to_group[dfa.start_state]
    new_accept = set()

    # Build transition function and accept states
    for group_idx, group in enumerate(P):
        rep = next(iter(group))  # Take a representative state from the group
        if rep in dfa.accept_states:
            new_accept.add(group_idx)
        for a in dfa.alphabet:
            next_state = dfa.transitions[rep][a]
            new_transitions[group_idx][a] = state_to_group[next_state]

    return DFA(new_states, dfa.alphabet, new_transitions, new_start, new_accept)

# Test function: Print DFA
def print_dfa(dfa, name="DFA"):
    print(f"{name}:")
    print(f"States: {dfa.states}")
    print(f"Alphabet: {dfa.alphabet}")
    print("Transitions:")
    for state in dfa.states:
        for symbol, next_state in dfa.transitions[state].items():
            print(f"  δ({state}, {symbol}) = {next_state}")
    print(f"Start state: {dfa.start_state}")
    print(f"Accept states: {dfa.accept_states}\n")

# Example: L = {w | w ends with 1}
def example():
    states = {0, 1, 2}
    alphabet = {'0', '1'}
    transitions = {
        0: {'0': 1, '1': 2},  # A
        1: {'0': 1, '1': 2},  # B
        2: {'0': 1, '1': 2}   # C
    }
    start_state = 0
    accept_states = {2}

    dfa = DFA(states, alphabet, transitions, start_state, accept_states)
    print_dfa(dfa, "Original DFA")

    minimized_dfa = hopcroft_minimization(dfa)
    print_dfa(minimized_dfa, "Minimized DFA")

if __name__ == "__main__":
    example()