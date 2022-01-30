import numpy as np

class Arithmetics:

    def __init__(self):
        pass

    def value(self):
        data = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], dtype=np.int64)

        data3d = np.array([
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            [
                [11, 12, 13],
                [14, 15, 16],
                [17, 18, 19]
            ],
            [
                [21, 22, 23],
                [24, 25, 26],
                [27, 28, 29]
            ],
            
        ], dtype=np.int64)

        # print("dimensi", data.ndim)
        # print("shape", data.shape)
        # print("size", data.size)
        # print("tipe data", data.dtype)

        # print("tipe data variable", type(data))

        return data, data3d

    def slicing(self):
        x = np.arange(15)
        x = x.reshape(5,3)
        return x

    def multiplier(self):
        pass

if __name__ == '__main__':
    arithmatics = Arithmetics()
    # data, data3d = arithmatics.value()
    # print(data[1, 1])
    # print(data3d.shape)
    # print(data3d[2,1,1])
    # data3d[2, 1, 1] = 30
    # print(data3d)

    data_slicing = arithmatics.slicing()
    print(data_slicing)
    print("="*50)
    print(data_slicing[:3][:])
    print("="*50)
    print(data_slicing[:3][:])