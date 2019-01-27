""" Problem Class
"""
import urllib.request
import random
import math
from node import Node

class Problem:
    """ Problem Class
    """

    def __init__(self):
         # holds possible actions the agent can do
        self.population = []
        self.max_population = 8
        self.n_angles = 6

    def initialize_population(self):
        for i in range(self.max_population):
            angles = []
            for j in range(self.n_angles):
                angles.append(random.randint(0, 359))
            
            node = Node(angles)
            self.population.append(node)

    def fitness_function(self, angles: list) -> float:
        req = f'http://localhost:8080/antenna/simulate?phi1={angles[0]}&theta1={angles[1]}&phi2={angles[2]}&theta2={angles[3]}&phi3={angles[4]}&theta3={angles[5]}'
        with urllib.request.urlopen(req) as response:
            page = response.readlines()
            first_line = page[0]
            formated = float(first_line[:-1])
            return formated

    def selection(self) -> tuple:
        total_fitness = 0
        for individual in self.population:
            individual.fitness = self.fitness_function(individual.chromosome)
            total_fitness += individual.fitness
        
        self.population.sort(key=self.sort_node, reverse=True)

        f_individual = self.population[0].chromosome
        s_individual = self.population[1].chromosome

        self.crossover(f_individual, s_individual)
        
        self.population.pop()
        self.population.pop()

    def crossover(self, a:list, b:list):
        a = a.copy()
        b = b.copy()

        crossover_point = random.randint(0,5)
        a[crossover_point:], b[crossover_point:] = b[crossover_point:], a[crossover_point:]

        a = Node(a)
        b = Node(b)

        self.population.append(a)
        self.population.append(b)

        a.fitness = self.fitness_function(a.chromosome)
        b.fitness = self.fitness_function(b.chromosome)

        self.population.sort(key=self.sort_node, reverse=True)

    def mutation(self):
        for individual in self.population:
            for gen in range(self.n_angles):
                if random.uniform(0,1) < 0.05:
                    individual.chromosome[gen] = random.randint(0, 359)

        self.population.sort(key=self.sort_node, reverse=True)
       
    def sort_node(self, node: Node) -> float:
        return node.fitness
