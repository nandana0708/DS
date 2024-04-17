# reducer.py

from collections import defaultdict

def reducer():
    max_cost_per_location = defaultdict(float)
    try:
        for line in iter(input, ''):
            location, cost = line.strip().split('\t')
            cost = float(cost)
            if cost > max_cost_per_location[location]:
                max_cost_per_location[location] = cost
    except EOFError:
        pass
    for location, max_cost in max_cost_per_location.items():
        print(f"{location}: {max_cost}")

if __name__ == "__main__":
    reducer()

