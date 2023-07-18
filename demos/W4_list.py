# declare empty list
bleh = []
meh = list ()
 #declare no empty list
yummy = ["chocolate", "pizza", "doughnuts", "subway"]
 # print entire list
print(yummy)
 #print  a single item
print(yummy[-4])
 # print some items off the list
print(yummy[0:4:2])
 #add elements to our list (expand it)- the end of the list
print(bleh)
bleh.append ("spinach")
bleh.append("brocoli")
bleh.append("aubergine")
bleh.append("pesto")
print(bleh)
 #add items to a list (multiple items)
bleh.extend(["liver", "bigos", "tomatoes"])
print(bleh)
 #remove item from a list
if "hot dog" in bleh:
     bleh.remove("hot dog")
print(bleh)
 #insert items specific position
bleh.insert(1, "carrot")
print(bleh)
bleh.insert(4, "cabbage")
print(bleh)
 #remove items by index
x = bleh.pop(3)
bleh.pop(5)
print(bleh)
print(x)
 #mutate your list
print(yummy)
yummy[2] = "pancakes"
print(yummy)
 #check a list for particular data type/ traverse list
lista = ["Fred", 56, True, 99.4, "Potato", False, 82]
sum = 0
for item in lista:
     if isinstance(item, int):
         sum+= item
print(sum)