def adding(lista = []):
    new_member = input("Enter name of new avenger: ")
    lista.append(new_member)

#h = []
# for i in range(3):
 #  adding(h)
#print(h)

def remove(lista=[]):
    rejected = input("enter name of avenger to be removed: ")
    if rejected in lista:
        lista.remove(rejected)

#a = ["fred", "george","harry", "anna"]
#remove(a)
#print(a)

def printing (lista= []):
    for hero in lista:
        print(f"the might {hero} is part of the avengers!")
#x = ["kelly", "Jerzy", "Viktorija", "Marius"]
#priting(x)

def run():
    avengers = []
    while True:
        opt = int(input("Avengers, Assemble!\n\n1-Add an Avenger\n2- Remove an Avenger \n3- check on the team \n4 - EXIT"))
        if opt == 1:
            adding(avengers)
        elif opt ==2:
            remove(avengers)
        elif opt == 3:
            printing(avengers)
        elif opt ==4:
            break
        else:
            print("No such option. Go to specsavers!")

run()

