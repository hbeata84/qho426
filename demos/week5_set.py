#insasalising empty set
s = set()
#initalising no empty set
sl1 = {1, 2, 3, 4 }
col = {"blue" "green", "red", "yellow", "black""red", "blue"}
print(col)
#adding items to the set
col.add("purple")
col.add("orange")
print(col)

#adding more items at once
col = col.union({"white", "brown", "crimson", "magenta"})
print(col)

#remove item from set
if"yellow" in col:
        col.remove("yellow")
print(col)

#set are heterog data structure
col.add(99)
col.add(False)
col.add(76.8)
print(col)
print("-"*20)
c = {"brown", "turquoise", "pink", "red", "cyan", "green"}

#union = join 2 sets togheter, not keeping duplicates
c2 = col.union(c)
print(f"col is {col}")
print(f"c2 is {c2}")

#intersection- looking at common values in the sets
c3 = col.intersection(c)
print(f"c3 is {c3}")

#diffrence - keep elements of one set that not part of other
c4 = c.difference(col)
c5 = col.difference(c)
print(f"c4 is {c4}")
print(f"c5 is {c5}")
