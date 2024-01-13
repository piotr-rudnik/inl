import re
from collections import defaultdict

from base import CHARS

def count_punctuation_around_words(df, column_name, punctuation):
    a = defaultdict(lambda: {'before': 0, 'after': 0, 'neither': 0, 'total': 0, 'before_chance': 0.0, 'after_chance': 0.0})
    for text in df[column_name].astype(str):
        # Patterns for before and after punctuation
        pattern_before = fr'{re.escape(punctuation)}\s*\b(\w+)'
        pattern_after = fr'\b(\w+)\s*{re.escape(punctuation)}'

        matches_before = re.findall(pattern_before, text)
        matches_after = re.findall(pattern_after, text)

        all_words = set(re.findall(r'\b\w+\b', text))

        for word in all_words:
            a[word]['total'] += text.count(word)
            if word in matches_before:
                a[word]['before'] += text.count(word)
            if word in matches_after:
                a[word]['after'] += text.count(word)
            if word not in matches_before and word not in matches_after:
                a[word]['neither'] += text.count(word)

    # Calculating chances
    for word, counts in a.items():
        if counts['total'] > 0:
            counts['before_chance'] = counts['before'] / counts['total']
            counts['after_chance'] = counts['after'] / counts['total']

    return dict(a)
def count_punctuation_around_words_for_chars(df, column_name, chars=CHARS) -> dict:
    counts = {}
    for char in chars:
        counts[char] = count_punctuation_around_words(df, column_name, char)
    return counts


def calculate_average_word_gap(df, column_name, punctuation):
    total_punctuation_count = df[column_name].str.count(re.escape(punctuation)).sum()
    total_word_count = df[column_name].str.split().apply(len).sum()
    average_gap = total_word_count / total_punctuation_count if total_punctuation_count > 0 else float('inf')
    return average_gap