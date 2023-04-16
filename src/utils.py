import os
from collections import namedtuple
from typing import Dict, Literal

import pandas as pd

_train_instances = None
_variables_names = ("id", "subject", "ts", "condition", "class")
_columns_names = None
_n_columns = None
_ts_length = None


def get_ts_from_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot(index="sample num", columns="sensor position", values="sensor value")


def _read_one(file: str = "Data1.csv", dataset: Literal["train", "test"] = "train", data_dir: str = "./data"
              ) -> pd.DataFrame:
    return pd.read_csv(os.path.join(data_dir, dataset, file))


def read_data(dataset: Literal["train", "test"] = "train", data_dir: str = "./data"
              ) -> Dict[str, str | int | pd.DataFrame]:
    files = os.listdir(os.path.join(data_dir, dataset))
    data = dict()
    for f in files:
        raw_df = _read_one(f, dataset)
        data[f] = {
            "id": int(raw_df["trial number"].unique()[0]),
            "subject": raw_df["name"].unique()[0],
            "ts": get_ts_from_df(raw_df),
            "condition": raw_df["matching condition"].unique()[0].rstrip(","),
            "class": raw_df["subject identifier"].unique()[0],
        }
    return data


def _get_train_instances() -> int:
    global _train_instances
    if not _train_instances:
        _train_instances = len(read_data())
    return _train_instances


def _get_n_columns() -> int:
    global _n_columns
    if not _n_columns:
        raw_df = _read_one()
        _n_columns = get_ts_from_df(raw_df).shape[1]
    return _n_columns


def _get_columns_names() -> int:
    global _columns_names
    if not _columns_names:
        raw_df = _read_one()
        _columns_names = get_ts_from_df(raw_df).columns.to_list()
    return _columns_names


def _get_ts_length() -> int:
    global _ts_length
    if not _ts_length:
        raw_df = _read_one()
        _ts_length = get_ts_from_df(raw_df).shape[1]
    return _ts_length


_Meta = namedtuple("Meta", "train_instances variable_names column_names n_columns ts_length")
meta = _Meta(_get_train_instances(), _variables_names, _get_columns_names(), _get_n_columns(), _get_ts_length())
