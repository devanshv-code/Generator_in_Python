# Generator_in_Python

A generator in Python is a function that uses the yield keyword to produce a sequence of values one at a time, pausing between each. It is memory-efficient because it generates items on the fly, rather than storing the entire sequence in memory.
## Primarily types of generators
Generator Functions


Generator Expressions

## Key Points:
Function with yield: A generator is created using a function with the yield keyword. When yield is used, the function pauses and saves its state, returning the yielded value to the caller. The next time the function is called, it resumes from where it left off.

Memory Efficient: Generators are useful because they generate items one at a time, which is much more memory-efficient than creating a list of all items at once, especially for large sequences.

Iterative Processing: They are perfect for tasks where you only need to process one item at a time, like reading lines from a file or generating an infinite series of numbers.
## Why is it useful?
Saves Memory: Generators don’t store all values in memory. They are created on the fly and are great for handling large data streams or infinite sequences.

Lazy Evaluation: They generate values only when requested, which can make programs faster and more responsive.

So, generators help in writing efficient code that’s both memory and performance-friendly.
