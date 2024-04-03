import random
import matplotlib.pyplot as plt
import numpy as np

SIMULATION_NBR = 1_000_000
SIMULATION_SIZE = 100


def generate_random_list():
    random_list = []
    for i in range(SIMULATION_SIZE):
        random_list.append(random.random())
    return random_list


def score(nbr):
    random_list = generate_random_list()
    max_value = 0
    for i in range(0, nbr):
        max_value = max(max_value, random_list[i])
    for i in range(nbr, SIMULATION_SIZE):
        if random_list[i] > max_value:
            return [random_list[i], random_list[i] == max(random_list)]
    return [random_list[-1], random_list[-1] == max(random_list)]


number_score = []
winning_percentages = []
for i in range(SIMULATION_SIZE + 1):
    print(f"Simulating {i}...")
    all_scores = []
    all_percentages = []
    for j in range(SIMULATION_NBR):
        nbr_score = score(i)
        all_scores.append(nbr_score[0])
        all_percentages.append(nbr_score[1])
    number_score.append(np.mean(all_scores))
    winning_percentages.append(np.mean(all_percentages))


x = range(SIMULATION_SIZE + 1)
y = winning_percentages # number_score

plt.bar(x, y, width=0.8)

plt.show()
