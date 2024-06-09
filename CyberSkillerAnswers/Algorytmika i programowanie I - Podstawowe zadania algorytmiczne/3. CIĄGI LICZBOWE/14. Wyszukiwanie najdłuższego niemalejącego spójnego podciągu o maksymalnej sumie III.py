# Program code

# Function table_fill
def table_fill():
    return [int(i) for i in input().split()]


def max_subser(table):
    max_so_far = float('-inf')
    max_ending_here = 0

    for i in range(len(table)):
        max_ending_here += table[i]
        
        if max_ending_here < 0:
            max_ending_here = 0
        
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


print(max_subser(table_fill()))