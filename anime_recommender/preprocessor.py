import re
import math
import sys
import pickle

import pandas as pd
from tqdm import tqdm

def load_data(dir: str):
    data = pd.read_csv(dir)
    return data

def preprocessor_name_genre(data):
    datas = data[["title", "genre"]]
    genre = data[["genre"]]
    return datas, genre

def clean_str(string):
        string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
        return string.strip()

def existing_genre(lbl_data):
    genres = lbl_data.values.tolist()
    labels = []

    for genre in tqdm(genres):        
        if not isinstance(genre[0], float):
            g = genre[0].split(",")
            for item in g:
                item = clean_str(item)
                if item not in labels:
                    labels.append(item)
    
    genre2id = dict()
    id2genre = dict()

    for i, ge in enumerate(labels):
        genre2id[ge] = i
        id2genre[i] = ge
    
    return genre2id, id2genre
    
    
def preprocessor(dir: str):
    animedb = load_data(dir)
    datas, genre = preprocessor_name_genre(animedb)
    
    print("liat genre")
    print(genre.describe())

    genre2id, id2genre = existing_genre(genre)
    lbl_len = len(genre2id)
    
    dataset = datas.values.tolist()
    overall_dataset = []

    print(genre2id)

    for d in tqdm(dataset, desc="Pair Title with Genre"):
        x_raw = clean_str(d[0])
        if not isinstance(d[1], float):
            y_raw = d[1].split(",")
            
            for yr in y_raw:
                y_d = genre2id[clean_str(yr)]
                y = [0] * lbl_len

                y[y_d] = 1
                
                overall_dataset.append([x_raw, y])
            

    with open("datasets/preprocessed/dataset.pkl", "wb") as f:
        pickle.dump(overall_dataset, f)