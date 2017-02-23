from pizza import Pizza

# pizza = Pizza()
# pizza.read('small')
# pizza.slice((0, 0), (0, 2))
# pizza.slice((0, 0), (3, 6))
#
# for i in range(1, 7):
#     pizza.slice((1, 5), (i, i))
#
# pizza.parse_to_file()

pizza = Pizza()
pizza.read('medium')

for r in range(0, len(pizza._grid), 1):
    for c in range(0, len(pizza._grid), 12):
        pizza.slice((r, (r)), (c, (c + 11)))

print(pizza.is_valid_pizza())
