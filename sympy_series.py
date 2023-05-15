from automata.fa.dfa import DFA
# DFA which matches all binary strings ending in an odd number of '1's
dfa = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)
dfa.read_input('01')   # answer is  'q1‘
print(dfa.read_input_stepwise('011'))
#Answer # yields:
# 'q0‘	# 'q0‘	# 'q1'
# 'q2‘	# 'q1'
if dfa.accepts_input('011'):
    print('accepted')
else:
    print('rejected')

if dfa.accepts_input('001'):
    print('accepted')
else:
    print('rejected')


