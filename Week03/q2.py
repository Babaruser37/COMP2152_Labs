cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

print(f"Number of apples: {cart.count('apple')}")
print(f"Position of milk: {cart.index('milk')}")

cart.remove("eggs")
print(f"Removed item using pop: {cart.pop()}")

if "banana" in cart:
    print("Is banana in cart: True")
else:
    print("Is banana in cart: False")

print(f"Final Cart: {cart}")
