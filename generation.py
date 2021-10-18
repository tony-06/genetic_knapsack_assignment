import numpy as np

import autosome


class Generation:
    # There are a lot of variables here and I feel like it could be optimized but it works right now so it stays
    def __init__(self, data, p1_list=None, p2_list=None, pop_size=1000, max_weight=500, first_gen=False):
        self.data = data
        self.length = len(data)
        self.population = pop_size
        self.chromosome_list = []
        self.max_weight = max_weight
        self.probability_dist = []
        self.fitness_list = []
        self.parent1_list = p1_list if p1_list is not None else []
        self.parent2_list = p2_list if p2_list is not None else []
        self.first = first_gen
        self.first_gen()
        self.next_gen_p1 = []
        self.next_gen_p2 = []
        self.create_generation()
        self.get_fitness_list()
        self.selection()
        self.get_next_gen_parents()
        self.best_index = self.fitness_list.index(max(self.fitness_list))
        self.best_fit = self.chromosome_list[self.best_index]

    def get_fitness_list(self):
        # creates a list of fitness scores for the generation
        for c in self.chromosome_list:
            weight = 0
            utility = 0
            count = 0
            for gene in c:
                if gene:
                    weight += self.data[count][1]
                    utility += self.data[count][0]
                count += 1
            if weight > self.max_weight:
                temp = 1
                self.fitness_list.append(temp)
            else:
                temp = utility
                self.fitness_list.append(temp)

    def create_generation(self):
        # creates the next generation of chromosomes from the parent chromosomes
        for i in range(int(self.population / 2)):
            baby = autosome.Autosome(self.length, self.parent1_list[i], self.parent2_list[i])
            self.chromosome_list.append(baby.chromosome1)
            self.chromosome_list.append(baby.chromosome2)

    def selection(self):
        # create the probability distribution based on what I understand of L2 normalization
        squares = []
        for i in range(self.population):
            squares.append(self.fitness_list[i] ** 2)
        squares_sum = sum(squares)
        for j in range(self.population):
            self.probability_dist.append(squares[j] / squares_sum)

    def get_next_gen_parents(self):
        # choose parents from this generation based on the probability distribution of fitness scores
        for i in range(int(self.population / 2)):
            choice1 = np.random.choice(self.fitness_list, p=self.probability_dist)
            choice2 = np.random.choice(self.fitness_list, p=self.probability_dist)
            index1 = self.fitness_list.index(choice1)
            index2 = self.fitness_list.index(choice2)
            self.next_gen_p1.append(self.chromosome_list[index1])
            self.next_gen_p2.append(self.chromosome_list[index2])

    def get_average_fitness(self):
        # return the average fitness of this population
        return sum(self.fitness_list) / self.population

    def first_gen(self):
        # if this is the first generation the parent list has to be created at random
        if self.first:
            for i in range(int(self.population / 2)):
                a = autosome.Autosome(self.length)
                self.parent1_list.append(a.chromosome1)
                self.parent2_list.append(a.chromosome2)
