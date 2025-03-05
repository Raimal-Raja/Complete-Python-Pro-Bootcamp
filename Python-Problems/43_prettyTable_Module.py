from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Name', ['Raimal', 'Raja'])
table.add_column('Language', ['Python', 'Java'])
table.align = "l"
print(table)
