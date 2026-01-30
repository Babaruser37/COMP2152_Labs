inventory = {"Laptop": (999.99,5),
             "Mouse":(29.99,15),
             "Keyboard":(79.99,10),
             "Monitor":(299.99,8)
             }
prices = []
for key in inventory:
    print(f"{key} - Price: ${inventory[key][0]}, Quantity: {inventory[key][1]}")
    prices.append(inventory[key][1])
print(" ")

electronics = {"Laptop","Monitor"}
accessories = {"Mouse","Keyboard"}

print(f"All products: {electronics.union(accessories)}")
print(" ")

print(f"Price list: {prices}")
prices.sort()
print(f"Sorted prices: {prices}")
print(f"Lowest Price: ${prices[0]}")
print(f"Highest Price: ${prices[-1]}")

inventory["Headphones"] = (49.99,20)
inventory["Mouse"] = (29.99,12)
del(inventory["Monitor"])
print(" ")


print("=== Final Inventory ===")

for key in inventory:
    print(f"{key} - Price: ${inventory[key][0]}, Quantity: {inventory[key][1]}")

