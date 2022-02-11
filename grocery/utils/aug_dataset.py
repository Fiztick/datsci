import pandas as pd
from tqdm import tqdm
import numpy as np
import random
# from random import random, randrange, choice


products_info = {
    'iPhone' : [700, 4],
    'Xiaomi Mi' : [500, 5],
    'Macbook Pro Laptop' : [1500, 1],
    'AAA Batteries (4-pack)' : [2.99, 8],
    'Thinkpad Laptop' : [999.99, 3],
}

def generate_name(seed, sex, target = 300):
    name = []
    i = 0
    while i in range(target):
        # random_first = randrange(len(seed))
        # first = seed[random_first]
        first = random.choice(seed)

        # random_second = randrange(len(seed))
        # second = seed[random_second]
        second = random.choice(seed)

        if first != second:
            # name.append(first + " " + second)
            name.append({"name": first + " " + second, "sex": sex})
            i += 1

    return name

def generate_customer():
    name = pd.read_csv('../datasets/common_name.csv')
    name = name[["Name1", "Name2"]]

    # name["Full Name"] = name["Name1"] + " " + name["Name2"]
    name_m = name["Name1"].tolist()
    name_f = name["Name2"].tolist()

    compiled_name_m = generate_name(seed = name_m, sex = "M")
    compiled_name_f = generate_name(seed = name_f, sex = "F")

    combined_names = compiled_name_m + compiled_name_f
    print(combined_names)

def load_seed_data(dir = "../datasets/grocery_data.csv"):
    # Read csv file to d_grocery
    d_grocery = pd.read_csv(dir)

    # Remove NaN from d_grocery
    d_grocery = d_grocery.dropna(how="all")

    # Convert These Datas to Numeric
    d_grocery = d_grocery[d_grocery["Order ID"].str.isnumeric()]

    d_grocery["Quantity Ordered"] = pd.to_numeric(d_grocery["Quantity Ordered"])
    d_grocery["Price Each"] = pd.to_numeric(d_grocery["Price Each"])
    d_grocery["Order ID"] = pd.to_numeric(d_grocery["Order ID"])

    d_grocery["Month"] = d_grocery["Order Date"].str[0:2]
    d_grocery["Time"] = d_grocery["Order Date"].str[9:14]

    return d_grocery

def product_info(data_seed):
    # Initialize d_grocery_weight as a DataFrame

    d_grocery_weight = pd.DataFrame()

    # Making a sum of "Quantity Ordered" with a group by "Product"
    d_grocery_quantity = data_seed.groupby(["Product"])[["Quantity Ordered"]].sum().reset_index()

    # Making a Column in d_grocery_weight from these things
    d_grocery_weight["Product"] = d_grocery_quantity[["Product"]]
    d_grocery_weight["Ratio"] = d_grocery_quantity[["Quantity Ordered"]].apply(lambda x: x/1000)
    d_grocery_weight["Price Each"] = data_seed.groupby(["Product"])["Price Each"].unique().reset_index()["Price Each"]
    
    # Making a Dictionary called grocery_weight
    grocery_weight = {}

    # Making the datas in d_grocery_weight callable per row (Making it an array maybe still don't understand dict)
    for index, row in d_grocery_weight.iterrows():
        # Inserting into grocery_weight with a Structure of | 'Product' : [Price Each, Ratio] |
        # Example Insertion | 'iPhone': [700.0, 6,849] |
        grocery_weight[row["Product"]] = [row["Price Each"][0], row["Ratio"]]

    return grocery_weight

def ratio_item_monthly(data_seed):
    d_grocery_monthly = data_seed.groupby(["Month"])[["Quantity Ordered"]].sum().reset_index()
    total_order = d_grocery_monthly["Quantity Ordered"].sum()

    d_grocery_monthly["Ratio"] = d_grocery_monthly["Quantity Ordered"].apply(lambda x: x / total_order)
    return d_grocery_monthly

def ratio_product_monthly(data_seed):
    data_seed["Ordered Product"] = 1
    d_grocery_product = data_seed.groupby(["Month", "Order ID"])["Ordered Product"].sum().reset_index()

    d_product_average = round(d_grocery_product.groupby(["Month"])[["Ordered Product"]].mean().reset_index())["Ordered Product"].tolist()
    d_product_max = d_grocery_product.groupby(["Month"]).max()["Ordered Product"].reset_index()["Ordered Product"].tolist()
    
    return d_product_average, d_product_max




def main(target_augmented_data = 10000):
    data_seed = load_seed_data()

    products = product_info(data_seed = data_seed)
    monthly_item_ratio = ratio_item_monthly(data_seed = data_seed)

    monthly_item_ratio["Target Item"] = round(monthly_item_ratio["Ratio"].apply(lambda x: target_augmented_data * x))
    item_ratio = monthly_item_ratio["Target Item"].tolist()

    product_average, product_max = ratio_product_monthly(data_seed = data_seed)

    product_list = [p for p in products]
    product_weight = [products[p][1] for p in products]

    final_data = []
    for i in tqdm(range(0, 12)):
        order_limiter = 0
        while order_limiter < int(item_ratio[i]):

            selected_ratio = random.randrange(int(product_average[i]), int(product_max[i]))
            
            for pr in range(int(selected_ratio)):
                product_choice = random.choices(product_list, product_weight)

                final_data.append({"Order ID": order_limiter + 1, "Month": i+1, "Products": product_choice})
            order_limiter += 1

    print(len(final_data))

if __name__ == '__main__':
    # product_info(data_seed = data_seed) 

    main()