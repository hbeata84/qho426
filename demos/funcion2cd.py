# definition of  a funcion - specifying  what the proceddure will repeat

def triangle_area(b,h):
    area = 0.5*h*b
    print(f"area is {area}")
# call to funcion - make program execute the funcion again.
triangle_area(10, 20)
triangle_area(5, 4)
height = float(input("Enter height: "))
base = float(input("enter base: "))
triangle_area(height, base)
