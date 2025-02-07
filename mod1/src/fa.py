class FiniteAutomaton:
    def __init__(self, states, alphabet, transition_table, start_state, accept_states):
        """
        :param states: Set of states
        :param alphabet: Set of input symbols
        :param transition_table: Dictionary mapping (state, symbol) -> next state
        :param start_state: Initial state
        :param accept_states: Set of accepting states
        """
        self.states = states
        self.alphabet = alphabet
        self.transition_table = transition_table
        self.start_state = start_state
        self.accept_states = accept_states
    
    def process(self, input_string):
        """Process an input string and determine if it's accepted."""
        current_state = self.start_state
        
        for symbol in input_string:
            if (current_state, symbol) in self.transition_table:
                current_state = self.transition_table[(current_state, symbol)]
            else:
                return False  # Invalid transition
        
        return current_state in self.accept_states

# Example usage:
states = {"q0", "q1", "q2"}
alphabet = {"a", "b"}
transition_table = {
    ("q0", "a"): "q1",
    ("q1", "b"): "q2",
    ("q2", "a"): "q1"
}
start_state = "q0"
accept_states = {"q2"}

fa = FiniteAutomaton(states, alphabet, transition_table, start_state, accept_states)

# Test cases
print(fa.process("ab"))  # True
print(fa.process("aba")) # False
print(fa.process("abab")) # True
