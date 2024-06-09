# Program code

# Function table_fill
def table_fill():
    return [int(i) for i in input().split()]


def max_subser(table):
    lengths = [1] * len(table)
    index = 0

    last_num = table[0]

    for num in range(1, len(table)):
        if table[num] >= last_num:
            lengths[index] = lengths[index] + 1
        else: 
            index = num

        last_num = table[num]
    
    max_length = max(lengths)
    max_length_index = lengths.index(max_length)

    return (max_length_index, max_length)


print(max_subser(table_fill()))