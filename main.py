import itertools
import operator

# Use count to index my data
my_data = [100, 200, 300, 400, 500, 600]

my_data = list(zip(my_data, itertools.count()))

# print(my_data)

# Use Cycle to cycle through values of collection

cycle_data = itertools.cycle(my_data)

print(next(cycle_data))
print(next(cycle_data))
print(next(cycle_data))
print(next(cycle_data))
print(next(cycle_data))
print(next(cycle_data))
print(next(cycle_data))

# Use repeat to iterate through range and get power of 2 of each num in range
# Easier to use than for loops
my_repeat = map(pow, range(10), itertools.repeat(2))
print(list(my_repeat))

