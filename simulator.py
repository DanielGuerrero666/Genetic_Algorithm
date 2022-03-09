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

def selection(chromosomes, fitness_list):
    elitism_chosen = chromosomes.index(fitness_list.index(max(fitness_list)))
    for fitness in fitness_list:
        fitness = fitness if fitness_list.index(fitness) == 0 else fitness + fitness_list.index(fitness - 1)
    
    spin1 = random.randrange(fitness_list[-1])
    spin2 = random.randrange(fitness_list[-1])

    for i in range(len(fitness_list)):
        if i == 0:
            r1 = fitness_list[i] if spin1 <= fitness_list[i] else 0
            r2 = fitness_list[i] if spin1 <= fitness_list[i] else 0
        else:
            r1 = fitness_list[i] if fitness_list[i-1] < spin1 <= fitness_list[i] else 0
            r2 = fitness_list[i] if fitness_list[i-1] < spin2 <= fitness_list[i] else 0

    if r1 and r2 != 0:
        roulette_chosen1 = chromosomes.index(fitness_list.index(r1))
        roulette_chosen2 = chromosomes.index(fitness_list.index(r2)) 
    
    return(elitism_chosen, roulette_chosen1, roulette_chosen2)


print(simulation(population))