import pandas as pd

train_in_path = "/Users/peterrodnick/git/INL/data/train/in.tsv"
train_expected_path = "/Users/peterrodnick/git/INL/data/train/expected.tsv"


def get_df_train_in() -> pd.DataFrame:
    return pd.read_csv(train_in_path, sep='\t', header=None, names=["id", "without"])


def get_df_train_expected() -> pd.DataFrame:
    return pd.read_csv(train_expected_path, sep='\t', header=None, names=["with"])


def get_train_df() -> pd.DataFrame:
    return pd.concat([get_df_train_in(), get_df_train_expected()], axis=1)
