import re
from collections import Counter
from pathlib import Path

def word_count(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    freq = Counter(words)
    total_words = len(words)
    top10 = freq.most_common(10)
    print("Total words:", total_words)
    print("Top 10 words:")
    for word, count in top10:
        print(word, ":", count)

filename = Path(__file__).with_name("sample.txt")
word_count(filename)