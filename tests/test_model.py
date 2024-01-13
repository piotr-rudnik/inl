import pandas as pd
import pytest

from model import count_punctuation_around_words_for_chars, count_punctuation_around_words


@pytest.fixture
def sample_df():
    data = {'text': ['Hello, world!']}
    return pd.DataFrame(data)

def test_count_punctuation_around_words(sample_df):
    result = count_punctuation_around_words(sample_df, 'text', ',')
    assert result['Hello']['before'] == 0
    assert result['Hello']['after'] == 1
    assert result['Hello']['neither'] == 0
    assert result['world']['before'] == 0
    assert result['world']['after'] == 0
    assert result['world']['neither'] == 1



def test_count_punctuation_around_words_for_chars(sample_df):
    chars = [',', "!"]
    result = count_punctuation_around_words_for_chars(sample_df, 'text', chars)

    # Test for comma
    assert result[',']['Hello']['before'] == 0
    assert result[',']['Hello']['after'] == 1
    assert result[',']['Hello']['neither'] == 0

    assert result[',']['world']['before'] == 1

    # Test for exclamation mark
    assert result['!']['world']['after'] == 1

