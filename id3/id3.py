import math
import bisect
import csv
import random
from node import Node

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

def frequency(attr, label):
    class_labels = {}
    n_rows = 0
    for row in dataset:
        instance = row[attr]
        if instance == label:
            instance_class = row[-1]

            if instance_class in class_labels:
                class_labels[instance_class] += 1
            else:
                class_labels[instance_class] = 1
            n_rows += 1   
    
    return class_labels, n_rows

def calculate_entropy(attr, label):
    """
    returns the result of p(Classifier|atrr=label)*entropy(Classifier|atrr=label)
    """
    entropy = 0
    class_labels, n_rows = frequency(attr, label)
    
    for cl in class_labels:
        p = class_labels[cl]/n_rows
        entropy -= p * math.log2(p)
#        print(cl, class_labels[cl], n_rows, p)
#    print(n_rows, len_dataset, entropy)
    return (n_rows/len_dataset)*entropy

def gain(attr):
    """
    returns the gain of the attribute, wich means
    entropy(Classifier) - SUM[p(Classifier|atrr)*entropy(Classifier|attr)]
    """
    gain = entropy_classifier()
    for label in col_labels[attr]:
        gain -= calculate_entropy(attr, label)

    return gain

def best_attr(attr_list):
    gains = []
    for attr in attr_list:
        g = gain(attr)
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

def id3(attr_list, node):
    node_attr = best_attr(attr_list)
    attr_list.remove(node_attr)

    for label in col_labels[node_attr]:
        class_labels, n_rows = frequency(node_attr, label)
        node.children.append(Node(label, node, [], class_labels))
    
    for child in node.children:
        # if label perfectly classified
        if len(child.class_labels) == 1 or len(attr_list) == 0:
            leaf_node = Node(max_class_label(class_labels), child, [], class_labels)
            child.children.append(leaf_node) 
            return leaf_node
        else:
            id3(attr_list, child)
    
attr_list = [1, 2, 3, 4]
prepare_dataset(r'tenis.txt', 0.70, training_set, test_set)
col_labels = preprocess(attr_list)
print(best_attr(attr_list))
root = Node(None, None, [], None)
id3(attr_list, root)
root.print_tree()