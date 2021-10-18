import numpy as np
import generation


items_data = np.loadtxt('Program2Input.txt')
population_size = 1000

first_gen = generation.Generation(items_data, pop_size=population_size, first_gen=True)

best_list = []


def generate(d, c, pop):
    # create a new generation and add the most fit to the best_list list,
    next_gen = generation.Generation(d, c.next_gen_p1, c.next_gen_p2, pop)
    best_list.append(next_gen.best_fit)
    return next_gen


for i in range(100):
    # this for loop needs to be replaced with a while loop that checks to see if the average fitness has increased over
    # the last 10 generations but I don't have all day to test this
    x = generate(items_data, first_gen, population_size)
    print("Generation #: " + str(i))
    print("average fitness: " + str(x.get_average_fitness()))
    print("max fitness " + str(max(x.fitness_list)))
    first_gen = generate(items_data, x, population_size)

# sloppy loop to print stuff out and look at it
for i in best_list:
    weight = 0
    utility = 0
    count = 0
    print(i.bin)
    for gene in i:
        if gene:
            weight += items_data[count][1]
            utility += items_data[count][0]
        count += 1
    print("best weight = " + str(weight) + " with utility: " + str(utility))
