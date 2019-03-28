import math
import bisect
import csv
import random
from node import Node
import pandas as pd

dataset = []
len_dataset = 0
training_set = []
test_set = []
col_labels = []
 
def prepare_dataset(filename, split, training_set=[] , test_set=[]):
    # open the file
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        # make each line in the file a row in the dataset
        global dataset
        dataset = list(lines)
        
        # number of rows
        global len_dataset
        len_dataset = len(dataset)

        # separate between training and test set
        for row in range(len_dataset):                
            if random.random() < split:
                training_set.append(dataset[row])
            else:
                test_set.append(dataset[row])


def preprocess(attr_list):
    col_labels = {}
    for attr in attr_list:
        col_labels[attr] = []
        for row in dataset:
            instance = row[attr]
            if instance not in col_labels[attr]:
                col_labels[attr].append(instance)
        
    return col_labels

def entropy_classifier():
    """
    returns the entropy of the classifier
    """
    labels = {}
    for row in dataset:
        instance = row[-1]

        if instance in labels:
            labels[instance] += 1
        else:
            labels[instance] = 1

    entropy = 0
    for label in labels:
        p = labels[label]/len_dataset
        entropy -= p * math.log2(p)

    return entropy

def frequency(subset, attr, label):
    class_labels = {}
    n_rows = 0
    rows = []
    for row in subset:
        instance = row[attr]
        if instance == label:
            instance_class = row[-1]
            rows.append(row)
            if instance_class in class_labels:
                class_labels[instance_class] += 1
            else:
                class_labels[instance_class] = 1
            n_rows += 1   
    
    return rows, class_labels

def calculate_entropy(subset, attr, label):
    """
    returns the result of p(Classifier|atrr=label)*entropy(Classifier|atrr=label)
    """
    entropy = 0
    rows, class_labels = frequency(subset, attr, label)
    n_rows = len(rows)

    for cl in class_labels:
        p = class_labels[cl]/n_rows
        entropy -= p * math.log2(p)
#        print(cl, class_labels[cl], n_rows, p)
#    print(n_rows, len_dataset, entropy)
    return (n_rows/len_dataset)*entropy

def gain(subset, attr):
    """
    returns the gain of the attribute, wich means
    entropy(Classifier) - SUM[p(Classifier|atrr)*entropy(Classifier|attr)]
    """
    gain = entropy_classifier()
    for label in col_labels[attr]:
        gain -= calculate_entropy(subset, attr, label)

    return gain

def best_attr(attr_list, subset):
    gains = []
    for attr in attr_list:
        g = gain(subset, attr)
        bisect.insort(gains, (g, attr))
    #print(gains)
    return gains[-1][1]

def max_class_label(class_labels):
    max_cl = -math.inf
    max_label = 0
    for cl in class_labels:
        if class_labels[cl] > max_cl:
            max_cl = class_labels[cl]
            max_label = cl
    return max_label

def id3(rows_set, node):
    # if there is no row in the subset
    # get the attr that best represents the data
    node_attr = best_attr(attr_list, rows_set)

    # for each one of it's labels
    for label in col_labels[node_attr]:
        # gets the rows the it appears and it's class labels frequency
        rows, class_labels = frequency(rows_set, node_attr, label)
        if len(rows) > 0:
            new_node = Node(node_attr, node, [], rows, class_labels)
            node.children.append((new_node, label))
    
    for pair in node.children:
        child = pair[0]
        # if label perfectly classified
        if len(child.class_labels) == 1:
            leaf_label = max_class_label(child.class_labels)
            leaf_node = Node(leaf_label, child, [], [], child.class_labels)
            child.children.append((leaf_node, leaf_label)) 
        else:
            id3(child.subset, child)

def select_class(case, node):
    for pair in node.children:
        child = pair[0]
        label = pair[1]
        if len(child.children) == 0:
            return child.content
        if case[int(child.content)] == label:
            return select_class(case, child)

def evaluate_model(root, test_set):
    real_class = []
    predict_class = []
    
    for row in test_set:
        real = row[-1]
        predict = select_class(row, root)
        real_class.append(real)
        predict_class.append(predict)

    real_class = pd.Series(real_class, name='Actual')
    predict_class = pd.Series(predict_class, name='Predicted')
    confusion_matrix = pd.crosstab(real_class, predict_class)
    return confusion_matrix


attr_list = [0, 1, 2, 3, 4, 5]
prepare_dataset(r'car.data.txt', 0.70, training_set, test_set)
print('Training set size: ' + repr(len(training_set)))
print('Test set size: ' + repr(len(test_set)))
col_labels = preprocess(attr_list)
root = Node(None, None, [], [],  None)
id3(training_set, root)
print(evaluate_model(root, test_set))
#root.print_tree()