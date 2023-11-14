x = str(input("Start: "))
y = str(input("Finish: "))

x = x.split(',')
y = y.split(',')

start = [int(i) for i in x]
finish = [int(i) for i in y]

print(start)