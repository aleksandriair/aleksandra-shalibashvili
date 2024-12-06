def find_collatz_sequence(n):
    counter_without_cache = 0
    sequence = [n]
    current_number = n
    
    while current_number > 1:
        if current_number % 2 == 0:
            current_number = current_number // 2
        elif current_number % 2 == 1:
            current_number = 3 * current_number + 1
        sequence.append(current_number)
        counter_without_cache += 1
    return sequence, counter_without_cache

def find_collatz_sequence_with_cache(n, cache):
    counter_with_cache = 0
    sequence = [n]
    current_number = n
    
    while current_number > 1:
        if current_number in cache:
            cached_sequence = cache[n]
            sequence.extend(cached_sequence[1:])
            counter_with_cache += 1
            break
        if current_number % 2 == 0:
            current_number = current_number // 2
        elif current_number % 2 == 1:
            current_number = 3 * current_number + 1
        sequence.append(current_number)
        counter_with_cache += 1
        
    cache[n] = sequence
    
    return sequence, counter_with_cache

def main():
    cache = {}
    
    n = 3
    
    sequence_without_cache, counter_without_cache = find_collatz_sequence(n)
    print(f"The Collatz sequence of {n} is: {sequence_without_cache} (without cache)")
    print(f"We used {counter_without_cache} step(s) without cache.")

    sequence_with_cache, counter_with_cache = find_collatz_sequence_with_cache(n, cache)
    print(f"The Collatz sequence of {n} is: {sequence_with_cache} (with cache)")
    print(f"We used {counter_with_cache} step(s) with cache.")

    sequence_again, counter_again = find_collatz_sequence_with_cache(n, cache)
    print(f"On the second try, we used {counter_again} step(s) with cache.")

if __name__ == "__main__":
    main()