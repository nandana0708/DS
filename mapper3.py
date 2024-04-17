# mapper.py

def mapper(line):
    fields = line.strip().split("\t")
    location = fields[2]
    cost = float(fields[4])
    return (location, cost)

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        location, cost = mapper(line)
        print(f"{location}\t{cost}")

