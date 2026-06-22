
def portfolio_cost(filename):
    '''
    Computes the total cost of a portfolio file
    :param filename:
    :return: int: the total cost of the portfolio file
    '''
    total = 0.0
    with open(filename, 'rt') as f:
        rows = f.readlines()
        headers = rows[0].strip().split(',')
        for row in rows[1:]:
            row_data = row.strip().split(',')
            nshares = int(row_data[1])
            price = float(row_data[2])
            total += nshares * price
    return total


import sys

try:
    filename = sys.argv[1]
    cost = portfolio_cost(filename)
    print(f"The total cost of {filename} is {cost}")
except IndexError:
    print("Usage: python3 " + sys.argv[0] + " <filename>")


