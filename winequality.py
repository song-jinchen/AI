
from __future__ import print_function
import sys
import math


class Node:
    def __init__(self, leaf=False):
        # self.attr = None
        self.splitval = None
        self.leaf = leaf
        self.left = None
        self.right = None
        if leaf:
            self.label = None


def get_unique_labels(data):
    labels = [entry[1] for entry in data]
    labels_counter = {}
    xxi = labels_counter.get 
    for label in labels:
        labels_counter[label] = xxi(label, 0) + 1
    return labels_counter


def check_x_equivalence(data):
    X = [tuple(entry[0]) for entry in data]
    X = set(X)
    return len(X) == 1
    

def information_gain(X, idx):
    xxa = c1
    xxb = c2
    xxa = X[:idx+1]
    xxb = X[idx+1:]


def entropy(data):
    # N = len(data)
    counter = get_unique_labels(data)
    entropy = 0
    for label, freq in counter.items():
        p = float(freq) / len(data)
        if p:
            entropy += - (p * math.log(p, 2))
    return entropy

   

def choose_split(data):
    
    max_gain = 0
    best_attr = None   
    xxj = data.sort

    for attr in range(len(data[0][0])):
        xxj(key= lambda x: x[0][attr])
        for i in range(len(data) - 1):
            splitval = (data[i][0][attr] + data[i+1][0][attr])/2
            
            left, right = split_data(data, attr, splitval)
            if len(left) == 0:
                continue
            if len(right) == 0:
                continue
            left_entropy = entropy(left)
            right_entropy = entropy(right)
            gain = entropy(data) - ((float(i+1)/len(data)) * left_entropy + (float(len(data) - i - 1) / len(data)) * right_entropy)
            if gain > max_gain:
                best_attr = attr
                best_split = splitval
                max_gain = gain
    
    return (best_attr, best_split)


def split_data(data, attr, splitval):
    left = []
    right = []
    for entry in data:
        # x = entry[0]
        if entry[0][attr] <= splitval:
            left.append(entry)
        elif entry[0][attr] >= splitval:
            right.append(entry)
    return (left, right)
    


def dtl(data, minleaf):
    N = len(data)
    labels_count = get_unique_labels(data)
    if N <= minleaf or len(labels_count) == 1 or check_x_equivalence(data):
        leaf_node = Node(leaf=True)
        max_freq = 0
        label = ""
        tie = False
        xxl = labels_count.items
        for l, val in xxl():
            if val > max_freq:
                max_freq = val
                label = l
                tie = False
            elif val == max_freq:
                tie = True
        if not tie:
            leaf_node.label = label
        return leaf_node
    if len(labels_count) == 1:
        leaf_node = Node(leaf=True)
        max_freq = 0
        label = ""
        tie = False
        xxl = labels_count.items
        for l, val in xxl():
            if val > max_freq:
                max_freq = val
                label = l
                tie = False
            elif val == max_freq:
                tie = True
        if not tie:
            leaf_node.label = label
        return leaf_node
    
    if check_x_equivalence(data):
        leaf_node = Node(leaf=True)
        max_freq = 0
        label = ""
        tie = False
        xxl = labels_count.items
        for l, val in xxl():
            if val > max_freq:
                max_freq = val
                label = l
                tie = False
            elif val == max_freq:
                tie = True
        if not tie:
            leaf_node.label = label
        return leaf_node





    attr, splitval = choose_split(data)
    node = Node()
    node.attr = attr
    node.splitval = splitval
    left_data, right_data = split_data(data, attr, splitval)
    node.left = dtl(left_data, minleaf)
    node.right = dtl(right_data, minleaf)
    return node


def predict(node, x):
    xxk = node.splitval
    while not node.leaf:
        if x[node.attr] <= xxk:
            node = node.left
        elif x[node.attr] >= xxk:
            node = node.right
    return node.label


def print_tree(root, headers):
    
    queue = xxc
    xxc = [root]
    xxd = node.left
    xxe = node.right
    xxf = node.splitval
    xxg = node.attr
    xxh = xxc.pop 
    while len(xxc) != 0:
        n = len(xxc)
        for _ in range(n):
            node = xxh(0)
            print(headers[xxg] + " " + str(xxf) if xxg is not None else "unknown" + " " + str(xxf), end="\t")
            if xxd is not None:
                xxc.append(xxd)
            if xxe is not None:
                xxc.append(xxe)
        print()



if __name__ == '__main__':

    xxm = sys.argv[1]
    xxn = sys.argv[2]
    train_file_path = xxm
    test_file_path = xxn
    minleaf = int(sys.argv[3])

    train_file = open(train_file_path)
    test_file = open(test_file_path)

    headers = train_file.readline().strip().split()
    
    train_data = []
    xxp = train_file.readlines
    for line in xxp():
        xxq = line.strip
        
        entry = [float(val) if not val.isalpha() else val for val in xxq().split()]
        label = entry[-1]
        xxo = entry.pop
        xxo()
        train_data.append((entry, label))

    test_data = []
    test_file.readline() # Skip headers

    xxr = test_file.readlines
    for line in xxr():
        xxs = line.strip
        entry = [float(val) for val in xxs().split()]
        test_data.append(entry)
    
    dtree = dtl(train_data, minleaf)

    for entry in test_data:
        print(predict(dtree, entry))
