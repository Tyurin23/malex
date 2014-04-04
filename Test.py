import random

import numpy as np

import Utils.data as d
import Classification.knn.knn as knn


__author__ = 'tyurin'


def test_knn():
    train_size = 10000
    train_seek = random.randint(0, 60000 - train_size)
    test_size = 100
    test_seek = random.randint(0, 10000 - test_size)
    n_size = 3

    x, y = d.read_idx("train-images.idx3-ubyte", "train-labels.idx1-ubyte", size=train_size, seek=train_seek)
    train_features, train_labels = np.array(x), np.array(y)
    x, y = d.read_idx("t10k-images.idx3-ubyte", "t10k-labels.idx1-ubyte", size=test_size, seek=test_seek)
    test_features, test_labels = np.array(x), np.array(y)
    ok = 0
    for i, features in enumerate(test_features):
        print ".",
        if not (i + 1) % 50 and i:
            print ""
        res = knn.find(features, train_features, train_labels, n_size)
        if res == test_labels[i]:
            ok += 1
    print "\nTest completed. %d from % is true. Result %d%%" % (
        ok, test_labels.shape[0], (1.0 * ok / test_labels.shape[0] * 100))


if __name__ == "__main__":
    test_knn()