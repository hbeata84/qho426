import json
import matplotlib.pyplot as plt

def save(dictio = {}):
    with open("data.jason", "w") as f:
        json.dump(dictio, f)

#d = {"cat":50, "dog":100}
#save(d)
def load():
    with open("data.jason") as f:
        d = json.load(f)
    return d

def survey(n=3):
    s = {}
    for i in range(n):
        resp = ""
        while resp not in ("me", "partner", "pet", "child"):
            resp = input("Who rules in your house? Me, partner, child, pet").lower()
        s[resp] = s.get(resp, 0) + 1
    return s
#print(survey(5))

def run():
    data = {}
    while True:
        print("Menu:\n1-NewSurvey\n2-Load last survey\n3-Save results\n4-Visualise\n5-Exit\n")
        opt = input("Enter your choice: ")
        if opt == "1":
            n = int(input("Number of respondents"))
            data = survey(n)
        elif opt == "2":
            data = load()
        elif opt == "3":
            save(data)
        elif opt == "4":
            print("Choose type:\na-Point graph\nb-Bar Chart\nc-Pie chart")
            opt2 = input("Your choice: ").lower()
            if opt2 == "a":
                plt.plot(data.keys(), data.values(), "y^-")
                plt.xlabel("Emperor")
                plt.ylabel("Frequency")

            elif opt2 == "b":
                plt.bar(data.keys(), data.values(), color = "#A512B1")
                plt.xlabel("Emperor")
                plt.ylabel("Frequency")

            elif opt2 == "c":
                plt.pie(data.values(), labels=data.keys(), autopct= "%.0f")
            else:
                print("No such option. Try again")
            plt.title("Power struggle in students houses")
            plt.show()
        elif opt == "5":
            break
run()