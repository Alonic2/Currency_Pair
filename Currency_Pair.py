from forex_python.converter import get_rates
import fire
import pandas as pd

def Pair(name):

    DataT = pd.Series(get_rates(str(name)))
    DataT.to_csv(f"{name}.csv")

if __name__ == '__main__':
    fire.Fire()
