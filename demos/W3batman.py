from random import randint

def batman_punch(str = 5, technique = 0):
    punch_power = 0.4 * str + 0.6*technique
    return punch_power
print (f"batman's punch is {batman_punch()}")

def fight_scene (n=2, enemy_str=3):
    total_str = n * enemy_str
    bat_str = batman_punch(randint(0,10))
    if bat_str >= total_str:
        return "batman wins"
    else:
        return "batman looses"

print(fight_scene())
def roberry_escape(n_of_cars):
     if n_of_cars > 5:
         return "batman is caught"
     else:
         return "batman escape"

def run():
    scene = fight_scene(randint(1, 10))
    escape = roberry_escape(randint(2,12))
    print(f"after a long fight {scene} afterwards police chase him  and {escape}")
    run()