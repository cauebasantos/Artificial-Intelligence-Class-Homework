import math
import bisect
import csv
import random
import pandas as pd

dataset = []
attr_lenght = 4
dataset_lenght = 0
training_set = []
test_set = []
min_values = [math.inf]*(attr_lenght)
max_values = [-math.inf]*(attr_lenght)
mean_values = [0]*(attr_lenght)

def normalize(case):
    # for each attribute
    for col in range(attr_lenght):
        # normalize it
        case[col] = (case[col] - mean_values[col])/(max_values[col] - min_values[col])

    return case

def prepare_dataset(filename, split, training_set=[] , test_set=[]):
    # open the file
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        # make each line in the file a row in the dataset
        dataset = list(lines)
        
        # number of rows
        dataset_lenght = len(dataset)-1
        
        # for each row on the dataset
        for row in range(dataset_lenght):
            # for each attribute
            for col in range(attr_lenght):
                # make it a float number
                dataset[row][col] = float(dataset[row][col])
                # sum the values of each attribute for every row
                mean_values[col] += dataset[row][col]
                
                # get the minimum value of each attribute
                if dataset[row][col] < min_values[col]:
                    min_values[col] = dataset[row][col]

                # get the maximum value of each attribute
                if dataset[row][col] > max_values[col]:
                    max_values[col] = dataset[row][col]

        # get the mean value of each attribute
        for col in range(len(mean_values)):
            mean_values[col] = mean_values[col]/dataset_lenght

        # separate between training and test set
        for row in range(dataset_lenght):                
            if random.random() < split:
                training_set.append(normalize(dataset[row]))
            else:
                test_set.append(dataset[row])

def manhattan_distance(instance1, instance2):
    """
    Return the manhattan distance bettween two given points
    """
    distance = 0
    for attribute in range(attr_lenght-1):
        distance += abs(instance1[attribute] - instance2[attribute])

    return distance

def select_class(k_nearest_neighbors):
    """
    Return the predicted class, given a list of k nearest neighbors
    """
    classes_dict = {}

    # for each neighbor
    for neighbor in k_nearest_neighbors:
        neighbor_class = neighbor[-1]
        # count it''s class
        if neighbor_class in classes_dict:
            classes_dict[neighbor_class] += 1
        else:
            classes_dict[neighbor_class] = 1

    # select the class that appears the most
    return max(classes_dict, key=lambda k:classes_dict[k])

def knn(training_set, case, k):
    # normalize the input
    case = normalize(case)

    neighbors = []
    # for each row in training set
    for training_instance in training_set:
        # calculate the distance between the row and the case
        distance = manhattan_distance(case, training_instance)
        # insert in a sorted list
        bisect.insort(neighbors, (distance, training_instance))

    k_nearest_neighbors = []
    # create a list with the k nearest neighbors
    for i in range(k):
        k_nearest_neighbors.append(neighbors[i][1])

    # return the predicted class
    return select_class(k_nearest_neighbors)

def evaluate_model(training_set, test_set, k):
    real_class = []
    predict_class = []
    
    for row in test_set:
        real = row[-1]
        predict = knn(training_set, row, k)
        real_class.append(real)
        predict_class.append(predict)

    real_class = pd.Series(real_class, name='Actual')
    predict_class = pd.Series(predict_class, name='Predicted')
    confusion_matrix = pd.crosstab(real_class, predict_class)
    return confusion_matrix

prepare_dataset(r'iris.data.txt', 0.70, training_set, test_set)

print('Training set size: ' + repr(len(training_set)))
print('Test set size: ' + repr(len(test_set)))
case = [6.0, 3.0, 4.8, 1.8]
k = 5
print(evaluate_model(training_set, test_set, k=k))
predict = knn(training_set, case, k=k)
print('k = ' + str(k))
print(f'Entrada: {case}\nClasse: {predict}')
