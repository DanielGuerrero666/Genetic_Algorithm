import random 
from population import generator

instruction_set = 'RLUD'
#Creacion de la matriz de nxm

testcase = ['DRUDLLDRRDLURDL', 'RRDDDULDDRUUDUU', 'ULRURRRULDLUDLR', 'UULRDUDLRDDUDRU', 'DURDDURRLRRUUUL']
population = []

for i in range(5):
    population.append(generator(instruction_set))

def simulation(chromosomes):
    n = 4
    matrix = [0] * n
    for i in range (n): 
        matrix[i] = [0] * n

    row = 3
    col = 0
    matrix[row][col] = 1
    movements = {"U":(-1,0), "D":(1,0), "R":(0,1), "L":(0,-1)} #Diccionario de movimeintos
    for instruction in chromosomes:
        #Codigo Basado en el metodo de Arce
        row += movements[instruction][0]
        col += movements[instruction][1]
         
        #Limites de la matriz
        if row < 0:
            row = 0
        elif row >= n:
            row = n - 1 
        elif col >= n:
            col = n - 1
        elif col < 0:
            col = 0

        matrix[row][col] = 1

    return sum(sum(row) for row in matrix)

for i in range(5):
    print(simulation(testcase[i]))
