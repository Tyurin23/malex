__author__ = 'tyurin'

import struct


def print_row(w, h, row, f="%3d"):
    for x in xrange(h):
        for y in xrange(w):
            print f % row[x * h + y],
        print ""


def read_idx(idx_images, idx_labels, size=0, seek=0):
    """
    Read from IDX files.
    See http://yann.lecun.com/exdb/mnist
    """
    return read_idx_images(idx_images, size, seek), read_idx_labels(idx_labels, size, seek)


def read_idx_images(idx_images, size=0, seek=0):
    """
    Read from IDX Images file.
    Return 2-dimensional array, where rows are training data and cols are features.
    """
    idx_file = open(idx_images, "rb")
    try:
        magic = struct.unpack('>i', idx_file.read(4))[0]  # read magic number
        if magic == 2051:  # images
            images_size = struct.unpack('>i', idx_file.read(4))[0]
            rows_size = struct.unpack('>i', idx_file.read(4))[0]
            columns_size = struct.unpack('>i', idx_file.read(4))[0]
            pix_in_image = rows_size * columns_size
            if not size:
                size = images_size
            if seek:
                idx_file.seek(idx_file.tell() + seek * pix_in_image)
            matrix = []
            for r in xrange(size):
                row = [0] * pix_in_image
                for c in xrange(pix_in_image):
                    row[c] = struct.unpack('B', idx_file.read(1))[0]
                matrix.append(row)
            return matrix
        else:
            raise ValueError
    finally:
        idx_file.close()


def read_idx_labels(idx_labels, size=0, seek=0):
    """

    """
    idx_file = open(idx_labels, "rb")
    try:
        magic = struct.unpack('>i', idx_file.read(4))[0]  # read magic number
        if magic == 2049:  # labels
            items_size = struct.unpack('>i', idx_file.read(4))[0]
            if not size:
                size = items_size
            matrix = [0] * size
            if seek:
                idx_file.seek(idx_file.tell() + seek)
            for r in xrange(size):
                matrix[r] = struct.unpack('B', idx_file.read(1))[0]
            return matrix
        else:
            raise ValueError
    finally:
        idx_file.close()


if __name__ == "__main__":
    idx = ["../t10k-images.idx3-ubyte", "../t10k-labels.idx1-ubyte", "../train-images.idx3-ubyte",
           "../train-labels.idx1-ubyte"]
    csv_f = ["../t10k-images.csv", "../t10k-labels.csv", "../train-images.csv", "../train-labels.csv"]
    # for i, idx_file in enumerate(idx):
    #     print "Converitng %s to %s..." % (idx_file, csv_f[i])
    #     idx_to_csv(idx_file, csv_f[i])
    #     print "Done"
    # pass
    x, y = read_idx(idx[0], idx[1], size=10, seek=1)
    for i, data in enumerate(x):
        print_row(28, 28, data)
        print y[i]
        raw_input("...")