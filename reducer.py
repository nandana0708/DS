# reducer.py

from collections import defaultdict

def reducer():
    final_word_count = defaultdict(int)
    try:
        for line in iter(input, ''):
            word, count = line.strip().split('\t')
            final_word_count[word] += int(count)
    except EOFError:
        pass
    for word, count in final_word_count.items():
        print(f"{word}:{count}")

if __name__ == '__main__':
    reducer()

