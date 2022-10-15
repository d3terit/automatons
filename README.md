# automatons
# Automatons is a library for creating and manipulating finite state machines.
To run, choose a python file and run it with python3.
for example, to run the example file, run `python3 afd.py`
install the library graphviz to visualize the automaton.
## Automatons
# afd.py
afd.py create an automata finit determinist with the following parameters: 
- states: a list of states
- alphabet: a list of symbols
- transitions: a list of tuples (state, symbol, state)
- initial_state: the initial state
- final_states: a list of final states
you can visualize the quintuple with the function `showAFD()`
you can validate a word with the method `execute()`
you can visualize the automaton with the method `showAFDDiagram()`

# afnd.py
afnd.py create an automata finit non-determinist with the following parameters:
- states: a list of states
- alphabet: a list of symbols
- transitions: a list of tuples (state, symbol, state)
- initial_state: the initial state
- final_states: a list of final states
- epsilon_transitions: a list of tuples (state, symbol, state)
you can visualize the quintuple with the function `showAFND()`
you can validate a word with the method `executeAFND()`
you can visualize the automaton with the method `showAFNDDiagram()`

# conversion.py
conversion.py contains the functions to convert an AFND to an AFD
contains the parameters:
- states: a list of states
- alphabet: a list of symbols
- transitions: a list of tuples (state, symbol, state)
- initial_state: the initial state
- final_states: a list of final states
- epsilon_transitions: a list of tuples (state, symbol, state)
you can call the functions of AFND
call the function `convertAFNDtoAFD()` to convert the AFND to AFD


It is all for now, I hope you enjoy it.

Elaborate with Copilot - AI Code Completion for GitHub 
# Author:
Daniel Hernando Mantilla

