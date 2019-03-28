""" Node class
"""

class Node:
    """ Node class for ID3 tree
    """
    def __init__(self, content, parent, children, subset, class_labels):
        self.content = content
        self.parent = parent
        self.children = children
        self.class_labels = class_labels
        self.subset = subset

    def __repr__(self):
        return f'<Node Object> label: {self.content}, class_labels: {self.class_labels}'

    def print_tree(self):
        if not self.children:
            print('Folha', self.content)
        else:
            print('Pai', self.content)
            for child in self.children:
                child[0].print_tree()
