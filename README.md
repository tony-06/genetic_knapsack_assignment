# genetic_knapsack_assignment
A genetic algorithm to solve the knapsack problem. CS461

Knapsack only holds 500lbs, input text has a list of utility/weight pairs

Autosomes - a chromosome pair. Class takes in two bit arrays as parents and creates two bit array offsprings
Crossover and mutation occur in this class

Generation - Takes in a list of bitArrays (chromosomes) sums their utility, and selects the candidates for the next generation to use for parents
