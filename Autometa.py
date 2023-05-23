from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

def dfa_to_nfa(dfa):
    states = set(dfa.states)
    alphabet = set(dfa.input_symbols)
    transitions = {}

    for state in states:
        for symbol in dfa.input_symbols:
            next_states = set()
            for transition_symbol, transition_state in dfa.transitions[state].items():
                if symbol == transition_symbol:
                    next_states.add(transition_state)
            if next_states:
                transitions.setdefault((state, symbol), set()).update(next_states)
            alphabet.add(symbol)

    start_state = dfa.initial_state
    final_states = set(dfa.final_states)

    nfa = NFA(
        states=states,
        input_symbols=alphabet,
        transitions=transitions,
        initial_state=start_state,
        final_states=final_states
    )

    return nfa

# Example DFA
dfa = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q1', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)

print(dfa)

# Convert DFA to NFA
nfa = dfa_to_nfa(dfa)

# Print the NFA
print(nfa)
