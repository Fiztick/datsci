import argparse

from preprocessor import preprocessor

def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', help="Path to dataset", required=True, default="dataset/anime.csv")

    args = parser.parse_args()
    return args

def train(args):
    preprocessor(args.data_dir)    
    # print(data)

if __name__ == '__main__':
    args = argument_parser()
    train(args)