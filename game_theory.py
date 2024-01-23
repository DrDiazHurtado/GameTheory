import random
import matplotlib.pyplot as plt
import itertools

def tit_for_tat(opponent_history):
    # Cooperates on the first move, then repeats the opponent's last move.
    return opponent_history[-1] if opponent_history else True

def always_defect(_):
    # Always defects.
    return False

def always_cooperate(_):
    # Always cooperates.
    return True

def random_choice(_):
    # Chooses randomly between cooperating and defecting.
    return random.choice([True, False])

def grudger(opponent_history):
    # Cooperates until the opponent defects once, then always defects.
    return False if False in opponent_history else True

def tit_for_two_tats(opponent_history):
    # Cooperates unless the opponent has defected in the last two rounds.
    return opponent_history[-2:].count(False) < 2 if len(opponent_history) > 1 else True

def suspicious_tit_for_tat(opponent_history):
    # Starts by defecting, then follows the Tit for Tat strategy.
    return opponent_history[-1] if opponent_history else False

def play_game(strategy1, strategy2, rounds=200):
    # Plays a game of 'rounds' rounds between two strategies.
    history1, history2 = [], []
    for _ in range(rounds):
        move1 = strategy1(history2)
        move2 = strategy2(history1)
        history1.append(move1)
        history2.append(move2)
    return history1, history2

def score_game(history1, history2):
    # Scores the game based on the moves.
    score = 0
    for move1, move2 in zip(history1, history2):
        if move1 and move2:
            score += 1  # Mutual cooperation
        elif move1 and not move2:
            score += 0  # Betrayed
        elif not move1 and move2:
            score += 3  # Successful betrayal
        else:
            score += 2  # Mutual betrayal
    return score

# Adding new strategies to the list
strategies = [tit_for_tat, always_defect, always_cooperate, random_choice, grudger, tit_for_two_tats, suspicious_tit_for_tat]
strategy_names = ["Tit-for-Tat", "Always Defect", "Always Cooperate", "Random", "Grudger", "Tit for Two Tats", "Suspicious Tit for Tat"]
scores = []

# Simulate games between all pairs of strategies
for strategy1, strategy2 in itertools.combinations(strategies, 2):
    history1, history2 = play_game(strategy1, strategy2)
    scores.append((strategy_names[strategies.index(strategy1)], score_game(history1, history2)))
    scores.append((strategy_names[strategies.index(strategy2)], score_game(history2, history1)))

# Calculate the average ranking
average_scores = {name: 0 for name in strategy_names}
for name, score in scores:
    average_scores[name] += score
for name in average_scores:
    average_scores[name] /= len(strategies) - 1

# Sort strategies by their average score
sorted_scores = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)

# Plotting the results
plt.bar([x[0] for x in sorted_scores], [x[1] for x in sorted_scores])
plt.xlabel('Strategies')
plt.ylabel('Average Score')
plt.title('Game Theory Strategies Ranking')
plt.show()
