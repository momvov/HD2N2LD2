n = int(input())

def powers_of_two_sum(n):

    result = []
    powers = 1

    while n > 0:
        if powers > n:
            if powers == 1:
                break

            powers /= 2

            result.append(int(powers))
            n -= powers

            powers = 1

        else:
            powers *= 2
    
    result = reversed(result)

    return result


result = powers_of_two_sum(n)

print(' '.join(map(str, result)))