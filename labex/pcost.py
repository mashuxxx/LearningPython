f = open('portfolio.csv', 'rt')
headers = next(f).split(',')

all_rows = []
for line in f :
    row = line.split(',')
    all_rows.append(row)

final = 0
for g in all_rows :
    cost = int(g[1]) * float(g[2])
    final = final + cost

print(f"Total cost : {final : .6f}")