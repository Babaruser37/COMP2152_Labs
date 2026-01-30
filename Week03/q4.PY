monday = {"Alice", "Bob", "Charlie", "Diana"}
wednesday = {"Bob", "Diana", "Eve", "Frank"}

monday.add("Grace")



print(f"Monday's class: {monday}")
print(f"Wednesday's class: {wednesday}")

print(f"Attended both classes: {monday.intersection(wednesday)}")
print(f"Attended either classes: {monday.union(wednesday)}")
print(f"Attended only Monday class: {monday.difference(wednesday)}")
print(f"Attended only one class: {monday.symmetric_difference(wednesday)}")

print(f"Is Monday subset of all students? {monday.issubset(monday.union(wednesday))}")


