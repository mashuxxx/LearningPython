##A rubber ball is dropped from a height of 100 meters
# and each time it hits the ground,
# it bounces back up to 3/5 the height it fell.
# Write a program bounce.py that prints a table showing
# the height of the first 10 bounces.

height = 100
for bounce in range (1, 11, 1):
    height = height * 3/5
    print(f'{bounce:4d}: {height:.4f}')

