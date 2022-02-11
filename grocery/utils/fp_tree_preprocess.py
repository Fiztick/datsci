import pandas as pd

def fp_tree_preprocess(file_dir):
    data = pd.read_csv(file_dir)
    d_grocery = data.groupby(["Order ID"])

if __name__ == '__main__':
    fp_tree_preprocess(file_dir = "../datasets/grocery_data.csv")

