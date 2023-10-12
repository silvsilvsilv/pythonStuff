from prettytable import PrettyTable

table = PrettyTable()

field_names = ["Item","Profit","Weight (in kg)", "P / W"]

table.add_column(field_names[0],[1,2,3,4,5,6,7,8])
table.add_column(field_names[1],[10,20,15,35,5,10,25,15])
table.add_column(field_names[2],[10,5,3,1,2,4,6,5])
table.add_column(field_names[3],[1,4,5,35,2.5,2.5,4.166,3])
# table.add_column(table.field_names[0],[1,2,3,4])

print(table)