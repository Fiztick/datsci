class User:

    def __init__(self, keys):
        self.key = keys

    def __init

    def pertambahan(self, data):
        result = []
        for i, baris in enumerate(data):
            result.append(baris + self.key)
        return result

    def pembagian(self, data):
        result = []
        for i, baris in enumerate(data):
            result.append(baris / self.key)
        return result
