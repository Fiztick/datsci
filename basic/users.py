class User:

    def __init__(self, keys):
        self.key = keys

    def pertambahan(self, data):
        result = []
        for baris in data:
            result.append({"bagus": baris + self.key})
        return result

    def pembagian(self, data):
        result = []
        for i, baris in enumerate(data):
            result.append(baris / self.key)
        return result


