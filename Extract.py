import pandas as pd

def ExtractData(url, path):
    df=pd.read_csv(url)
    if df is not None:
        return df.to_csv(path)
    else:
        return df
    return df