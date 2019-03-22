import bisect
import csv
import random

dataset = []
attr_lenght = 4
training_set = []
test_set = []
def handleDataset(filename, split, training_set=[] , test_set=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for row in range(len(dataset)-1):
            for col in range(attr_lenght):
                dataset[row][col] = float(dataset[row][col])
            if random.random() < split:
                training_set.append(dataset[row])
            else:
                test_set.append(dataset[row])

def manhattan_distance(instance1, instance2):
    distance = 0
    for attribute in range(attr_lenght-1):
        distance += abs(instance1[attribute] - instance2[attribute])

    return distance

def select_class(k_nearest_neighbors):
    classes_dict = {}

    for neighbor in k_nearest_neighbors:
        neighbor_class = neighbor[-1]
        if neighbor_class in classes_dict:
            classes_dict[neighbor_class] += 1
        else:
            classes_dict[neighbor_class] = 1

    return max(classes_dict, key=lambda k:classes_dict[k])

def knn(training_set, case, k):
    neighbors = []
    for training_instance in training_set:
        distance = manhattan_distance(case, training_instance)
        bisect.insort(neighbors, (distance, training_instance))

    k_nearest_neighbors = []
    for i in range(k):
        k_nearest_neighbors.append(neighbors[i][1])

    return select_class(k_nearest_neighbors)


handleDataset(r'iris.data.txt', 0.70, training_set, test_set)
print ('Train: ' + repr(len(training_set)))
print ('Test: ' + repr(len(test_set)))
training_set = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
predict = knn(training_set, [3,3,3], 1)
print(f'Entrada: [3,3,3]\nClasse: {predict}')