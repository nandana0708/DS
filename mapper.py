# mapper.py

from collections import defaultdict

def mapper(text):
    word_count = defaultdict(int)
    for word in text.split():
        word_count[word] += 1
    return word_count

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        text = line.strip()
        result = mapper(text)
        for word, count in result.items():
            print(f"{word}\t{count}")

