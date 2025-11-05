transitions = {
    'A1': {'0': 'A1', '1': 'B2'},
    'B1': {'0': 'C1', '1': 'D2'},
    'B2': {'0': 'C1', '1': 'D2'},
    'C1': {'0': 'D2', '1': 'B2'},
    'C2': {'0': 'D1', '1': 'B2'},
    'D1': {'0': 'B2', '1': 'C1'},
    'D2': {'0': 'B2', '1': 'C1'},
    'E1': {'0': 'D2', '1': 'E1'}
}


output = {
    'A1': '1', 'A2': 'B', 'B1': 'A', 'B2': 'B',
    'C1': 'C', 'C2': 'B', 'D1': 'B', 'D2': 'C', 'E1': 'C'
}

def process_input(sequence, start_state='A1'):
    state = start_state
    result = ''
    for symbol in sequence:
        result += output[state]
        state = transitions[state][symbol]
    result += output[state]  
    return result

inputs = ["00110", "11001", "1010110", "101111"]

for inp in inputs:
    print(f"Input: {inp} -> Output: {process_input(inp)}")
