from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtal", "Bulbasuar"])
table.add_column("Type", ["Electric", "Fire", "Water", "Grass"])

print(table)
#https://pypi.org/project/prettytable/