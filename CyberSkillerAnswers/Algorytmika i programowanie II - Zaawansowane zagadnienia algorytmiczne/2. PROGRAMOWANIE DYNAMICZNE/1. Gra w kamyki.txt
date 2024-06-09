N, k = map(int, input().split())

def play(N: int, k: int, is_ala_turn: bool):
    
    if N == k or N > 2 * k + 1:
        N -= k
    else:
        N -= 1

    if (N > 0):
        play(N, k, not is_ala_turn)
    else:
        if (is_ala_turn):
            print("A")
        else:
            print("B")

play(N, k, True)