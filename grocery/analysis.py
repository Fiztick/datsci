import os
import pandas as pd
import matplotlib.pyplot as plt

import chart_studio.plotly as py
import plotly.offline as pyoff
import plotly.graph_objs as go

def load_data(dir: str):
    # Load CSV File
    d_grocery = pd.read_csv(dir)
    # Grab only NAN row
    d_nan = d_grocery[d_grocery.isna().any(axis=1)]

    # Remove NAN from datasets
    d_grocery = d_grocery.dropna(how="all")

    # In column Order Date remove Cell that have string instead of datetime
    d_grocery = d_grocery[d_grocery['Order Date'].str[0:2] != 'Or']
    
    # Convert and Corecting All Item in Column Quantity Ordered and Price Each to Integer
    d_grocery["Quantity Ordered"] = pd.to_numeric(d_grocery["Quantity Ordered"])
    d_grocery["Price Each"] = pd.to_numeric(d_grocery["Price Each"])

    # Get Date Item (Month Only) In cell : 2 Ways

    # 1 Way, Slice String in Cell Order Date in order to get only month
    d_grocery["Month"] = d_grocery["Order Date"].str[0:2]
    # Change Data Type from String to Integer
    d_grocery["Month"] = d_grocery["Month"].astype('int32')


    # 2 Way, With DateTime Function
    d_grocery["Month"] = pd.to_datetime(d_grocery["Order Date"]).dt.month
    
    return d_grocery


def get_city(address):
    return address.split(",")[1].strip(" ")

def get_state(address):
    return address.split(",")[2].split(" ")[1]


def explore_sales_monthly(data):
    monthly_sales = data.groupby(["Month"]).sum()
    return monthly_sales

def explore_sales_by_city(data):
    monthly_sales = data.groupby(["City"]).sum()
    return monthly_sales

def explore_sales_by_product(data):
    product_sales = data.groupby(["Product"]).sum()
    product_sales = product_sales[["Quantity Ordered", "Sales"]]
    existing_item = product_sales.index.tolist()
    return product_sales, existing_item

def explore_sales_by_month_product(data, month = 1):
    pro_m_data = data[data["Month"] == month]
    pro_m_data = pro_m_data.groupby(["Product"]).sum()
    return pro_m_data
    

def explore_sales_by_product_month(data, product = "Macbook Pro Laptop"):
    m_pro_data = data[data["Product"] == product]
    m_pro_data = m_pro_data.groupby(["Month"]).sum()
    m_pro_data = m_pro_data[["Quantity Ordered", "Sales"]]
    print(m_pro_data)

# Berdasarkan Kota, Total Sales, Sales Per Bulan Pada Kota Tertentu, Sales Sebuah Barang Pada Suatu Kota
    

def main():
    dir = "datasets/grocery_data.csv"

    d_grocery = load_data(dir)

    # Apply Function to Column in Dataframe and Add to New Column
    d_grocery["City"] = d_grocery["Purchase Address"].apply(lambda x: f"{get_city(x)} {get_state(x)}")

    # Calculate Sales which quantity * price each
    d_grocery["Sales"] = d_grocery["Quantity Ordered"].astype("int") * d_grocery["Price Each"].astype("float")

    bycity = explore_sales_by_city(d_grocery)
    bycity = bycity[["Quantity Ordered", "Sales"]]

    plot_data = [
    
        go.Scatter(
            x = bycity.index,
            y = bycity[["Sales"]]
        )
    ]

    plot_layout = go.Layout(
        xaxis={"type": "category"},
        title="Monthly Sales"
    )

    fig = go.Figure(data = plot_data, layout = plot_layout)
    pyoff.iplot(fig)
    
    # Display Info
    # key_bycity = [ cty for cty in bycity.index]
    # print(key_bycity)

    # plt.figure(figsize=(5, 6))
    # plt.tight_layout()
    # plt.bar(key_bycity, bycity["Sales"])
    # plt.ylabel("Sales in USD ($)")
    # plt.xlabel("City")
    # plt.set_yticks(key_bycity, rotation='vertical')

    # plt.savefig("graph/city.png", pad_inches=0.05)

if __name__ == "__main__":
    main()