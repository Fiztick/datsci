from basic.arithmatic_class import Arithmetics

aritmatika = Arithmetics(keys = 1000, name="Sales Calculation")

barang_barang = [
    {"nama": "meat", "qty": 0}
]

def perhitungan_item(data_customer_sales):
    data_sales = []

    for sales in data_customer_sales:
        nama = sales["nama"]
        qty = sales["qty"]

        result = {"nama": nama, "total_belanja": aritmatika.pertambahan_satuan(qty)}
        data_sales.append(result)
    
    return data_sales