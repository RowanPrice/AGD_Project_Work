import math

def quadratic(a,b,c):
    x_1 = 0
    x_2 = 0

    if a == 0 :
        raise (ValueError)

    x_1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

    answer = str(x_1) + "," + str(x_2)

    return answer