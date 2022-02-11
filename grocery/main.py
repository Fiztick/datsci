import pandas as pd

def get_city(address):
    return address.split(',')[1].strip(" ")

def get_state(address):
    return address.split(',')[2].strip(" ")[0:2]

def calculate_quantity(number):
    return number * 1000

def load_dataset(dir: str):
    # Load CSV File
    d_grocery = pd.read_csv(dir)

    # Check if Dataset contains nan
    d_nan = d_grocery[d_grocery.isna().any(axis=1)]

    # Remove NAN from Dataset
    d_grocery = d_grocery.dropna(how="all")
    
    # Changing datas to numeric
    # d_grocery = d_grocery[d_grocery["Order ID"].str[0:2] != 'Or']
    d_grocery = d_grocery[d_grocery["Order ID"].str.isnumeric()]


    d_grocery["Quantity Ordered"] = pd.to_numeric(d_grocery["Quantity Ordered"])
    d_grocery["Price Each"] = pd.to_numeric(d_grocery["Price Each"])
    d_grocery["Order ID"] = pd.to_numeric(d_grocery["Order ID"])
    
    d_grocery["Month"] = d_grocery["Order Date"].str[0:2]
    d_grocery["Time"] = d_grocery["Order Date"].str[9:14]

    d_grocery["City"] = d_grocery["Purchase Address"].apply(lambda x: f"{get_city(x)} {get_state(x)}")

    d_grocery["Hasil Perkalian"] = d_grocery["Quantity Ordered"].apply(lambda x: f"{calculate_quantity(x)}")

    d_grocery["Total"] = d_grocery["Quantity Ordered"] * d_grocery["Price Each"]


    return d_grocery

def main():
    dir_dataset = "datasets/grocery_data.csv"
    load_dataset(dir = dir_dataset)

if __name__ == "__main__":
    main()