import re

from base import CHARS
from datasets import get_train_df

def count_chars(df, chars=CHARS):
    counts = {char: df["with"].str.count(re.escape(char)).sum() for char in chars}
    return counts

# ok
def exploration(df):
    print(df.head())
    print(count_chars(df))


if __name__ == '__main__':
    df = get_train_df()
    exploration(df)