#IT 412 - Eric Lovell - Problem 4#

from classes.shirt import ShirtInherit

my_new_shirts = ShirtInherit("small", "light blue", "short sleeve", "this shirt rules.")
my_new_shirts.increase_quantity(100)
print("New shirt inventory: " + str(my_new_shirts.quantity))
#Call method print message on shirt
print("Shirt Message: " + my_new_shirts.message.title())