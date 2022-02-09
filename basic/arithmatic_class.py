from random import random

class Arithmetics:
    
    def __init__(self, keys, name):
        self.keys = keys
        self.name = name

    def pertambahan(self, data):
        # Variable untuk menampung hasil
        result = []
        for i, item in enumerate(data):
            hasil_tambah = item + self.keys
            result.append(hasil_tambah)
        return result

    def pertambahan_satuan(self, qty):
        return qty * self.keys
    
    def perkalian_pengurangan(self, data, key_kurang):
        result = []
        for item in data:
            hasil_perkalian = item * self.keys
            hasil_pengurangan = hasil_perkalian - key_kurang
            result.append(hasil_pengurangan)
        
        return result

    def perhitungan_random(self, data):
        result_tambah = self.pertambahan(data = data)
        result_kombinasi = self.perkalian_pengurangan(data = result_tambah, key_kurang = random())

        return result_kombinasi