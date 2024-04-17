# reducer.py

def reducer():
    even_count = 0
    odd_count = 0
    try:
        for line in iter(input, ''):
            category, count = line.strip().split('\t')
            count = int(count)
            if category == "even":
                even_count += count
            elif category == "odd":
                odd_count += count
    except EOFError:
        pass
    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")

if __name__ == "__main__":
    reducer()

