import pandas as pd
import numpy as np

def random_sample(data, n: int, seed: int):
    return data.sample(n = n, random_state = seed)

if __name__ == '__main__':
    census = pd.read_csv('../datasets/census.csv')
    amostra_randomica = random_sample(data=census, n = 100, seed = 99)
    print(amostra_randomica.shape)