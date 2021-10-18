import random

import bitstring


class Autosome:
    # takes in two chromosomes, performs crossover, possibly mutates and then returns the two offspring chromosomes
    def __init__(self, length, parent1=None, parent2=None):
        self.length = length
        self.parent1 = parent1 if parent1 is not None else self.create_random_genes()
        self.parent2 = parent2 if parent2 is not None else self.create_random_genes()
        self.chromosome1 = bitstring.BitArray(self.length)
        self.chromosome2 = bitstring.BitArray(self.length)
        self.crossover()
        # i suppose if i knew what i was doing i could do these two things at once too
        self.mutate(self.chromosome1)
        self.mutate(self.chromosome2)

    def create_random_genes(self):
        # creates random genes at the length of the data if parents are not given (first generation usually)
        genes = bitstring.BitArray(self.length)
        for gene in range(self.length):
            chance = random.uniform(0, 1)
            if chance < .05:
                genes[gene] = True
        return genes

    def crossover(self):
        # choose a random crossover point and mix and match to make babies
        crossover_point = random.randrange(self.length)
        self.cross_before(crossover_point)
        self.cross_after(crossover_point)

    def cross_before(self, c):
        # I have these split up because if i was good i could parallelize
        for i in range(0, c):
            self.chromosome1[i] = self.parent2[i]
            self.chromosome2[i] = self.parent1[i]

    def cross_after(self, c):
        # I'm not
        for i in range(c, self.length):
            self.chromosome1[i] = self.parent2[i]
            self.chromosome2[i] = self.parent1[i]

    def mutate(self, gene):
        # a small chance for a gene to mutate
        for i in range(self.length):
            chance = random.uniform(0, 1)
            if chance < 0.0001:
                if gene[i]:
                    gene[i] = False
                else:
                    gene[i] = True
