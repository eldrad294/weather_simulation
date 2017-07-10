import numpy.random, \
       numpy as np
import random as rnd
import time
state_bank = ['SUNNY','RAINY','WINDY','CLOUDY','THUNDERSTORM']
#
def markov_prob_matrix(orig_matrix):
    new_matrix = []
    for i in range(len(orig_matrix)):
        new_matrix.append([])
        temp_value = 0
        for j, j_val in enumerate(orig_matrix[i]):
            temp_value += j_val
            new_matrix[i].append(temp_value)
    return new_matrix
#
probability_matrix = []
for i, x in enumerate(state_bank):
    dirichlet_distribution = numpy.random.dirichlet(np.ones(len(state_bank)), size=1)
    dirichlet_distribution = np.array(dirichlet_distribution).tolist()
    probability_matrix.append(dirichlet_distribution)
#
probability_matrix = [item for sublist in probability_matrix for item in sublist]
markov_matrix = markov_prob_matrix(probability_matrix)
print(probability_matrix)
curr_state = state_bank[0]
curr_state_index = 0
while True:
    for i, state in enumerate(state_bank):
        if state == curr_state:
            curr_state_index = i
            state_probabilities = markov_matrix[i]
            break;
    #
    random_val = rnd.uniform(0,1)

    for i in range(len(state_probabilities)):
        if i == 0:
            if 0 <= random_val <= state_probabilities[i]:
                curr_state = state_bank[i]
                print(curr_state)
        else:
            if state_probabilities[i-1] < random_val <= state_probabilities[i]:
                curr_state = state_bank[i]
                print(curr_state)
    time.sleep(2)




