import pandas as pd


def get_ts_from_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot(index="sample num", columns="sensor position", values="sensor value")
