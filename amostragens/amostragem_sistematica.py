import pandas as pd
import numpy  as np
import random


def amostragem_sistematica(data, n_samples: int, seed: int):
    random.seed(seed)
    inicio = random.randint(0, n_samples)
    step = data.shape[0] // n_samples
    index = np.arange(inicio, data.shape[0], step = step)
    return data.iloc[index, :]

if __name__ == '__main__':
    census = pd.read_csv('../datasets/census.csv')
    sis_sample = amostragem_sistematica(data=census, n_samples=300, seed=99)
    print(sis_sample.shape)