A = ['alfa', 'beta', 'gamma']

def generate_subsets(elements):
    n = len(elements)
    all_subsets = []
    
    for i in range(2**n):

        subset = []

        for j in range(n):
            if i & (1 << j):
                subset.append(elements[j])

        all_subsets.append(subset)
    
    return all_subsets


subsets = generate_subsets(A)

for subset in subsets:
    if len(subset) == 0:
        print('.')
    else:
        print(' '.join(subset))