from prettytable import PrettyTable

table = PrettyTable()

# table.field_names = ["Item","Profit","Weight (in kg)", "P / W"]

table.add_column("Item",[1,2,3,4,5,6,7,8])
table.add_column("Profit",[10,20,15,35,5,10,25,15])
table.add_column("Weight (in kg)",[10,5,3,1,2,4,6,5])
table.add_column("P / W",[1,4,5,35,2.5,2.5,4.166,3])

print(table)