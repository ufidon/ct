from collections import defaultdict

class FiniteAutomaton:
    def __init__(self, states, alphabet, transition_table, start_state, accept_states, epsilon_transitions=None):
        """
        :param states: Set of states
        :param alphabet: Set of input symbols
        :param transition_table: Dictionary mapping (state, symbol) -> set of next states
        :param start_state: Initial state
        :param accept_states: Set of accepting states
        :param epsilon_transitions: Dictionary mapping state -> set of epsilon transition states (for NFA-epsilon)
        """
        self.states = states
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.start_state = start_state
        self.accept_states = accept_states
        self.epsilon_transitions = defaultdict(set, epsilon_transitions) if epsilon_transitions else defaultdict(set)
    
    def epsilon_closure(self, states):
        """Computes the epsilon closure of a set of states."""
        stack = list(states)
        closure = set(states)
        
        while stack:
            state = stack.pop()
            for next_state in self.epsilon_transitions[state]:  # No KeyError now
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        
        return closure
    
    def process(self, input_string):
        """Process an input string and determine if it's accepted (for NFA/NFA-epsilon)."""
        current_states = self.epsilon_closure({self.start_state})
        
        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if (state, symbol) in self.transition_table:
                    next_states.update(self.transition_table[(state, symbol)])
            
            current_states = self.epsilon_closure(next_states)
        
        return any(state in self.accept_states for state in current_states)

# Example usage:
states = {"q0", "q1", "q2"}
alphabet = {"a", "b"}
transition_table = {
    ("q0", "a"): {"q1"},
    ("q1", "b"): {"q2"},
    ("q2", "a"): {"q1"}
}
epsilon_transitions = {
    "q0": {"q2"}  # Example epsilon transition
}
start_state = "q0"
accept_states = {"q2"}

fa = FiniteAutomaton(states, alphabet, transition_table, start_state, accept_states, epsilon_transitions)

# Test cases
print(fa.process("ab"))  # True
print(fa.process("aba")) # False
print(fa.process("abab")) # True
