import scipy.io
import config
import os.path
import numpy as np
import matplotlib.pyplot as plt

def load_mat (path, name):
    '''
    loading mat file
    :param path:
    :param name:
    :return:
    '''
    mat = scipy.io.loadmat(os.path.join(path, name))
    return mat

def get_pixs (row_number, mat):
    '''
    creating matirx of gray scale
    :param row_number: number of a row to plot
    :param mat: data with pnumbers
    :return:
    '''

    return np.reshape(mat['X'][row_number,:], (20,20))

def print_mat(pixes_mat):
    '''
    ploting pixels in grey scale
    :param pixes_mat:
    :return:
    '''
    plt.imshow(pixes_mat, cmap=plt.cm.gray, interpolation='nearest')
    plt.show()

def preaparing_data(data):
    prepared_data = {}
    keys = list(np.unique(data['y']))

    return data

class One_vs_all():
    def __init__(self):
        self.X = None
        self.y = None
        self.y_dict = None

    def set_X_and_Y_from_row(self, data):
        self.X = data['X']
        self.y_dict = {}
        for index, value in enumerate(list(np.unique(data['y']))):
            self.y_dict[index] = value
            if index == 0:
                self.y = np.place(data['y'], data['y']!=value, [0])
                self.y = np.place(data['y'], data['y']==value, [1])
            else:
                y2 = np.place(data['y'], data['y']!=value, [0])
                y2 = np.place(data['y'], data['y']==value, [1])
                self.y = np.c_([self.y, y2])

if __name__ == '__main__':

    data = load_mat(config.path_data, config.name)
    #print_mat(get_pixs(500, data))
    for i in range(1,10):
         plt.subplot(3,3,i)
         pixs_mat = get_pixs((i-1)*500, data)
         plt.imshow(pixs_mat, cmap=plt.cm.gray, interpolation='nearest')
    #machine_learning = One_vs_all()
    #machine_learning.set_X_and_Y_from_row(data)
    plt.show()


    print()

