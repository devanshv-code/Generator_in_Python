# generator expression
#Create a generator expression to yield numbers from 1 to 3.
gen_expr = (x for x in range(1, 4))

# Using the generator  expression
for number in gen_expr:
    print(number)

