import random

beats = {"R": "P", "P": "S", "S": "R"}

def player(prev_play, opponent_history=[], table={}):
    n = 5
    if prev_play == "":
        opponent_history.clear()
        table.clear()
    else:
        opponent_history.append(prev_play)

    if len(opponent_history) > n:
        key = "".join(opponent_history[-n-1:-1])
        table.setdefault(key, {"R": 0, "P": 0, "S": 0})
        table[key][opponent_history[-1]] += 1

    guess = random.choice("RPS")
    if len(opponent_history) >= n:
        key = "".join(opponent_history[-n:])
        if key in table:
            guess = max(table[key], key=table[key].get)

    return beats[guess]