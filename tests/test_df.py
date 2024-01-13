from datasets import get_train_df


def test_can_get_train_df():
    df = get_train_df()
    assert df is not None
    assert "id" in df.columns
    assert "with" in df.columns
    assert "without" in df.columns
