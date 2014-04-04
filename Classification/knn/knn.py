__author__ = 'tyurin'

import operator

import numpy as np


def find(x, groups, labels, n):
    data_size = groups.shape[0]
    diff = np.argsort(((np.tile(x, (data_size, 1)) - groups) ** 2).sum(axis=1) ** 0.5)
    counts = {}
    for k in range(n):
        label = labels[diff[k]]
        counts[label] = counts.get(label, 0) + 1
    sorted_count = sorted(counts.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_count[0][0]