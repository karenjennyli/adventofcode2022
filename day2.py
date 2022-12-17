"""
A for Rock, B for Paper, and C for Scissors.
X for Rock, Y for Paper, and Z for Scissors.


Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

1 for Rock, 2 for Paper, and 3 for Scissors
0 if you lost, 3 if the round was a draw, and 6 if you won

X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
"""

opponent_dict = {"A": "rock", "B": "paper", "C": "scissors"}
my_dict = {"X": "rock", "Y": "paper", "Z": "scissors"}
scores = {"rock": 1, "paper": 2, "scissors": 3}

f = open("day2_input.txt", "r")
lines = f.readlines()

total_score = 0

for line in lines:
    opponent = line[0]
    my_move = line[2]
    if opponent_dict[opponent] == my_dict[my_move]:
        outcome = 3
    elif opponent_dict[opponent] == "rock" and my_dict[my_move] == "paper":
        outcome = 6
    elif opponent_dict[opponent] == "rock" and my_dict[my_move] == "scissors":
        outcome = 0
    elif opponent_dict[opponent] == "paper" and my_dict[my_move] == "rock":
        outcome = 0
    elif opponent_dict[opponent] == "paper" and my_dict[my_move] == "scissors":
        outcome = 6
    elif opponent_dict[opponent] == "scissors" and my_dict[my_move] == "rock":
        outcome = 6
    elif opponent_dict[opponent] == "scissors" and my_dict[my_move] == "paper":
        outcome = 0
    if my_move == "X":
        score = 1 + outcome
    elif my_move == "Y":
        score = 2 + outcome
    elif my_move == "Z":
        score = 3 + outcome
    total_score += score

print(total_score)

new_total_score = 0

for line in lines:
    opponent = line[0]
    outcome = line[2]
    if outcome == "X":
        if opponent_dict[opponent] == "rock":
            score = scores["scissors"]
        elif opponent_dict[opponent] == "paper":
            score = scores["rock"]
        elif opponent_dict[opponent] == "scissors":
            score = scores["paper"]
    elif outcome == "Y":
        score = 3 + scores[opponent_dict[opponent]]
    elif outcome == "Z":
        if opponent_dict[opponent] == "rock":
            score = scores["paper"]
        elif opponent_dict[opponent] == "paper":
            score = scores["scissors"]
        elif opponent_dict[opponent] == "scissors":
            score = scores["rock"]
        score = score + 6
    new_total_score += score

print(new_total_score)

f.close()