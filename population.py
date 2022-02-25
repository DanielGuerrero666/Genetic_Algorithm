import random

def generator(instruction_set):
    chromosome = []
    for i in range(15):
        chromosome.append(instruction_set[random.randrange(4)])
    return str(chromosome)

