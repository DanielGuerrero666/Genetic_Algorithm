import random
from Simulador import simulation

instruction_set = 'RLUD'

#print(random.randrange(1))

#for i in range(3):
    #print(random.randrange(15), instruction_set[random.randrange(4)])
chromosome = input()

print(simulation(chromosome))


