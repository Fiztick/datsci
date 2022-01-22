from random import random

class User:

    def __init__(self, keys):
        self.key = keys

    def pertambahan(self, data):
        result = []
        for i, item in enumerate(data):
            hasil = item + self.key
            result.append({"bagus": hasil})

        return result

    def pembagian(self, data):
        result = []
        for i, baris in enumerate(data):
            result.append(baris / self.key)
        return result

    def random_max(self, data):
        result = []
        maxs = 0

        for i, baris in enumerate(data):
            # hit = random() * baris
            result.append(baris)

            if baris > maxs:
                maxs = baris

        print("Nilai maksimum : ", maxs)

        return result


