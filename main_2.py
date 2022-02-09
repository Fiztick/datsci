# from basic.arithmatic_class import Arithmetics
from audioop import avg
from basic.sales import Sales
from basic.sales_method import perhitungan_item, barang_barang

def app():
    data_number = [
        1, 2, 4, 6, 8
    ]

    # matics = Arithmetics(keys = 10, name="aritmatika")
    # hasil_pertambahan = matics.pertambahan(data = data_number)
    # hasil_perkalian_pengurangan = matics.perkalian_pengurangan(data = data_number)

    # hasil_kombinasi_random = matics.perhitungan_random(data = data_number)
    
    # print(hasil_kombinasi_random)

    qty = [5, 10, 5, 8, 9, 3]

    sales = Sales(base_price = 1000)
    hasil_sales = sales.hitung_sales(data_sales = qty)
    print(hasil_sales)

def tuple_example():
    qty_tuple = (5, 7, 1, 3, 6)

    qty_tuple += (3,)

    print(max(qty_tuple))
    print(min(qty_tuple))
    print(sum(qty_tuple))
    print(type(qty_tuple))
    data_sorted = sorted(qty_tuple)
    print(type(data_sorted))

    print(len(qty_tuple))
    
    # Count fungsi berapa kali item muncul di tuple
    test_count = data_sorted.count(3)
    print(test_count)

def dict_example():
    customer_data = [
        {"nama": "bagus", "qty": 4, "cart": ["milk", "snack", "meat", "soda"]},
        {"nama": "mahesa", "qty": 6, "cart": ["milk", "snack", "meat", "soda", "coffee", "water"]},
        {"nama": "hafiz", "qty": 2, "cart": ["milk", "meat",]},
        {"nama": "adi", "qty": 1, "cart": ["snack"]},
        {"nama": "agung", "qty": 4, "cart": ["milk", "snack", "soda", "coffee"]}
    ]


    # for customer in customer_data:
    #     # Specify the Key to get Value
    #     # nama = customer["nama"]
    #     # qty = customer["qty"]
    #     # cart = customer["cart"]
    #     # for item in cart:
    #     #     print(item)
    #     # print(nama, " jumlah belanja = ", qty)

    #     # Get Value by extract the key first
    #     for key in customer:
    #         # Cek Variable Type
    #         if isinstance(customer[key], list):
    #             for item in customer[key]:
    #                 print(item)
    #         else:
    #             print(key, "=", customer[key])

    #     print("="*50)

    sales = Sales(base_price = 1000)
    data_sales = sales.hitung_sales_dict(data_customer_sales = customer_data)


    # data_sales = perhitungan_item(data_customer_sales = customer_data)
    # barang_barang[0]["qty"] = 10

    print(data_sales)
    # print(barang_barang)
    

if __name__ == '__main__':
    dict_example()