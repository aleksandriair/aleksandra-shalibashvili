def generate_sequence(n):
    sequence = [n]
    current = n
    
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = current * 3 + 1
        sequence.append(current)
    
    return sequence

cache = {}

def generate_sequence_cached(n):
    if n in cache:
        return cache[n]
    
    sequence = [n]
    current = n
    
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = current * 3 + 1
            
        sequence.append(current)
        
        if current not in cache:
            cache[current] = sequence[sequence.index(current):]
    
    cache[n] = sequence
    return sequence

n = 3
print(f"Regular sequence for n={n}:", generate_sequence(n))
print(f"Cached sequence for n={n}:", generate_sequence_cached(n))