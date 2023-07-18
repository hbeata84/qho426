def generate():
    name = input(" enter name:")
    mrk = float(input("enter the mark: "))
    return name, mrk

#print(generate())
#x = generate()
#print(x)
#print(type(x))

def list_of_students(n):
    stud_list = []
    for i in range(n):
        stud_list.append(generate())
    return stud_list

#print(list_of_students(3))

def average(lista = []):
    total = 0
    for tup in lista:
        total += tup[1]
    avg = total/len(lista)
    return  avg

#print(average(list_of_students(5)))
def run():
    s_list = []
    while True:
        opt = int(input("menu:\n\n1-populate list of students\n2-calculate average mark\n3-change mark of one student\n4-exit\nChoice: "))
        if opt == 4:
            break
        elif opt == 1:
            num = int(input("how many student would you like to add? "))
            s_list.extend(list_of_students(num))
        elif opt ==2:
            print(f"Average mark is {average(s_list):.2f}")
        elif opt == 3:
            name = input("whose mark is to be changed ?")
            for student in s_list:
                if name == student[0]:
                    n_mrk = float(input("enter new mark: "))
                    s_list.remove(student)
                    s_list.append((name, n_mrk))
        else:
            print(" No such option, try again . FOOL")

run()



