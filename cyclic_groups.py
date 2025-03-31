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

if __name__ == "__main__":
    cyclic_group = find_modular_multiplicative_group(n)
    print(f"Modular multiplicative group of integers modulo {n}: {cyclic_group}\nThis group has order: {len(cyclic_group)}")

    for element in cyclic_group:
        order = find_element_order(element, n)
        print(f"{element} has order {order}")