from basic.arithmatic_class import Arithmetics

class Sales:
    def __init__(self, base_price):
        self.base_price = base_price
        self.aritmatika = Arithmetics(self.base_price, name="Sales Calculation")

    def hitung_sales(self, data_sales):
        hasil_sales = self.aritmatika.pertambahan(data_sales)
        return hasil_sales

    def hitung_sales_dict(self, data_customer_sales):
        data_sales = []

        for sales in data_customer_sales:
            nama = sales["nama"]
            qty = sales["qty"]

            result = {"nama": nama, "total_belanja": self.aritmatika.pertambahan_satuan(qty)}
            data_sales.append(result)
        
        print(self.__hitung_sales_barang())

        return data_sales

    def __hitung_sales_barang(self):
        return "test"

