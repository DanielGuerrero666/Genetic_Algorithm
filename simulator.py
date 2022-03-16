import random 

# POPULATION GENERATION - May correct
population = []

def generator():
    instruction_set = 'RLUD'
    chromosome = []

    for i in range(15):
        chromosome.append(instruction_set[random.randrange(4)])

    return "".join(chromosome)

for i in range(5):
    population.append(generator())

# SIMULATION OF FITNESS
def simulation(chromosomes):
    n = 4
    matrix = [0] * n
    for i in range (n): 
        matrix[i] = [0] * n

    row = 3
    col = 0
    matrix[row][col] = 1
    movements = {"U":(-1,0), "D":(1,0), "R":(0,1), "L":(0,-1)} # Movements dict
    fitness_list = []

    for chromosome in chromosomes:
        for instruction in chromosome:
            # Arce's version of movements in the matrix
            row += movements[instruction][0]
            col += movements[instruction][1]
            
            # Matrix's limits
            if row < 0:
                row = 0
            elif row >= n:
                row = n - 1 
            elif col >= n:
                col = n - 1
            elif col < 0:
                col = 0

            matrix[row][col] = 1
        
        fitness_list.append(sum(sum(row) for row in matrix)) 
    
    return dict(zip(chromosomes, fitness_list)) # returns fitness for the chromosome evaluated

# SELECTION (ROULETTE & ELITISM)

def selection(chromosomes_fitness):
    fitness_list = []
    fitness_list_keys = []

    for value in chromosomes_fitness.values():
        fitness_list.append(value)

    for key in chromosomes_fitness.keys():
        fitness_list_keys.append(key)

    elitism_chosen = fitness_list_keys[fitness_list.index(max(fitness_list))]

    roulette = []

    for i in range(len(fitness_list)): # The fitness list gets acumulated in the roulette list
        roulette.append(fitness_list[i] if i == 0 else fitness_list[i] + fitness_list[i-1])
    
    spin1 = random.randrange(roulette[-1])
    spin2 = random.randrange(roulette[-1])

    for i in range(len(chromosomes_fitness)):
        if i == 0:
            rlt_chosen1 = fitness_list_keys[i] if spin1 <= fitness_list[i] else 0
            rlt_chosen2 = fitness_list_keys[i] if spin2 <= fitness_list[i] else 0
        else:
            rlt_chosen1 = fitness_list_keys[i] if fitness_list[i-1] < spin1 <= fitness_list[i] else 0
            rlt_chosen2 = fitness_list_keys[i] if fitness_list[i-1] < spin2 <= fitness_list[i] else 0
    
    return(elitism_chosen, rlt_chosen1, rlt_chosen2)


simulation_result = simulation(population)

print(selection(simulation_result))