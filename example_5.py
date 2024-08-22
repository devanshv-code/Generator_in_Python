# Write a Python generator function that yields the first 5 natural numbers.
def simple_generator():
    for i in range(1, 6):
        yield i
# Using the generator
for number in simple_generator():
    print(number)