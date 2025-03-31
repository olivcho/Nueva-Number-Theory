# Find modular multiplicative groups that are cyclic

n = 50 # Change this to any integer to find cyclic groups up to n

def gcd(a, b):
    # Compute the greatest common divisor of a and b using Euclidean algorithm.
    while b:
        a, b = b, a % b
    return a

def find_modular_multiplicative_group(n):
    # Find the modular multiplicative group of integers modulo n.
    group = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            group.append(i)

    return group

def find_element_order(element, n):
    if element == 1:
        return 1
    else:
        counter = 1
        current_value = element
        while current_value != 1:
            current_value = (current_value * element) % n
            counter += 1
        return counter

def is_a_generator(element, n, group_size):
    if find_element_order(element, n) == group_size:
        return True
    else:
        return False

def find_generators(cyclic_group, n):
    generators = []
    group_size = len(cyclic_group)
    for element in cyclic_group:
        if is_a_generator(element, n, group_size):
            generators.append(element)

    return generators

if __name__ == "__main__":
    non_cyclic = []
    cyclic = []

    for i in range(1, n):
        cyclic_group = find_modular_multiplicative_group(i)
        # print(f"Modular multiplicative group of integers modulo {n}: {cyclic_group}\nThis group has order: {len(cyclic_group)}")

        generators = find_generators(cyclic_group, i)
        if len(generators) == 0:
            non_cyclic.append(i)
        else:
            cyclic.append(i)
        
    print(f"Non-cyclic groups up to {n}: {non_cyclic}")
    print(f"Cyclic groups up to {n}: {cyclic}")