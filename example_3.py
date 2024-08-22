#Write a Python generator function that yields the squares of numbers from 1 to 3.
def square_generator():
    for i in range(1, 4):
        yield i * i

# Using the generator
for square in square_generator():
    print(square )