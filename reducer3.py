# reducer.py

def reducer():
    total_lines = 0
    total_cost = 0.0
    try:
        for line in iter(input, ''):
            location, cost = line.strip().split('\t')
            total_lines += 1
            total_cost += float(cost)
    except EOFError:
        pass
    print(f"Total lines: {total_lines}")
    print(f"Total cost: {total_cost}")

if __name__ == "__main__":
    reducer()

