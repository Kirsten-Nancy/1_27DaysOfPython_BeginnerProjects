from turtle import Turtle, Screen
from prettytable import PrettyTable, ALL


my_pet = Turtle()
print(my_pet)
my_pet.shape('turtle')
my_pet.color('cyan4')
print(my_pet.position())
my_pet.forward(100.0)
my_pet.right(90.0)
my_pet.forward(100.0)
my_pet.right(90.0)
my_pet.forward(100.0)

my_screen = Screen()
print(my_screen)
print(my_screen.canvheight)
my_screen.bgcolor('plum4')
my_screen.exitonclick()

table = PrettyTable(hrules=ALL)

# table.add_column("Pokemon name", ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column("Type", ['Electric', 'Water', 'Fire'])
# table.align = 'l'
table.add_row([" ", "mid", " "])
table.add_row([" ", " ", " "])
table.add_row([" ", "X", " "])


print(table)
