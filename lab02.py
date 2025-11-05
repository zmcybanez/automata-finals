mealy = {
    'A': {'0': ('A','A'), '1': ('B','B')},
    'B': {'0': ('C','A'), '1': ('D','B')},
    'C': {'0': ('D','C'), '1': ('B','B')},
    'D': {'0': ('B','B'), '1': ('C','C')},
    'E': {'0': ('D','C'), '1': ('E','C')},
}

inputs = ['0','1']

def moore_key(state, out): return f"{state}_on{out}"


moore_states = {}
for s in mealy:
    for inp in inputs:
        ns, out = mealy[s][inp]
        moore_states[moore_key(ns,out)] = out


moore_underlying = {k: k.split('_on')[0] for k in moore_states}
moore_trans = {}
for key, underlying in moore_underlying.items():
    moore_trans[key] = {}
    for inp in inputs:
        ns, out = mealy[underlying][inp]
        moore_trans[key][inp] = moore_key(ns, out)


def simulate(input_string, start_mealy='A'):
    s = start_mealy
    outputs = []
    moore_seq = []
    for ch in input_string:
        ns, out = mealy[s][ch]
        outputs.append(out)
        moore_seq.append(moore_key(ns, out))
        s = ns
    return ''.join(outputs), moore_seq

tests = ["00110", "11001", "1010110", "101111"]
for t in tests:
    outs, seq = simulate(t, 'A')
    print(f"{t} -> {outs}   Moore seq: {seq}")
