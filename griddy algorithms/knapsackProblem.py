#Knapsack Problem
from prettytable import PrettyTable

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
 
# Main greedy function to solve problem
def fractionalKnapsack(W, arr):
    
    t = PrettyTable()

    t.add_column("Item", ["Profit", "Weight (kg)", "P / W"])
    for i in range(len(arr)):
        t.add_column(str(i+1),[arr[i].profit,arr[i].weight,(arr[i].profit / arr[i].weight)])
    
    print(t)
    
    # Sorting Item on basis of ratio
    arr.sort(key = lambda x: (x.profit/x.weight), reverse = True)  
    
    # Result(value in Knapsack)
    finalvalue = 0.0
    
    values = []
    weights = []
    wt = W
    # Looping through all Items
    for item in arr:
 
        # If adding Item won't overflow, 
        # add it completely
        if item.weight <= W:
            weights.append(item.weight)
            W -= item.weight
            finalvalue += item.profit
            values.append(item.profit)
 
        # If we can't add current Item, 
        # add fractional part of it
        else:
            finalvalue += item.profit * W / item.weight
            values.append(item.profit * W / item.weight)
            break
     
    print(f"Summation of Weights: ")
    
    for i in range(len(weights)):
        print(f"{weights[i]} {'+ ' if i != len(weights) - 1 else ''}", end="")

    print(f"= {wt}")    

    # Returning final value
    print(f"Summation of Profit: ")

    for i in range(len(values)):
        print(f"{values[i]} {'+ ' if i != len(values) - 1 else ''}", end="")
    
    print(f"= {finalvalue}")
 
 
# Driver Code
if __name__ == "__main__":
    W = 18
    arr = [Item(10,10), Item(20,5), Item(15,3), Item(35,1), Item(5,2), Item(10,4), Item(25,6), Item(15,3)]
 
    # Function call
    fractionalKnapsack(W, arr)
 