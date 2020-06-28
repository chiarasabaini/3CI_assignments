__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0.0 2019-05-12"
import time

def get_fsa_program(program_name):
    """Sets the program for a finite state automaton
    described by a functional matrix (or transition function)
    """

    # fsm = (Q, I, f, q0, F)
    
    if program_name == "even parity":
        transition_function = {("s0", "0"):("s0"), #il mio lavoro qui è finito, ci penso tra 4 giorni quando scade
                               ("s0", "1"):("s1"),
                               ("s1", "0"):("s1"),
                               ("s1", "1"):("s0")}        
    return transition_function

def fsa_run(input_string, transition_function, final_states, initial_state="s0"):
    """Executes a finite state automaton recognizer, given in input the string,
    the rules (transition function), the final state set and the initial state.
    Returns True if the given string has been recognized, otherwise False.
    """

    return 0

if __name__ == '__main__':    
    input_string="0100110"
    result = fsa_run(input_string=input_string, transition_function=get_fsa_program("parità pari"), final_states={"s0"})
    
    if result:
        print(input_string, "riconosciuta")
    else:
        print(input_string, "non riconosciuta")
    
