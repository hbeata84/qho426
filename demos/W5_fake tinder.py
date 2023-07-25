def interests():
    print("enter all interests, one after the other or \"stop\" to stop ")
    s1 = set()
    interests = ""
    while True:
        interests = input()
        if interests.lower() == "stop":
            break
        s1.add(interests)
    return s1


#print(interests())
def run():
       print("First person: ")
       p1 = interests()
       print("secound person")
       p2 = interests()
       common = p1.intersection(p2)
       if len(common) >= 3:
         print(f"you are a match made in heaven! you have {len(common)}hobbies in common ")
       else:
         print("oh no, it wont work, find other human")

run()