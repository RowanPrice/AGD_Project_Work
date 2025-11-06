def calc_grade(p_mark):
    p_grade = ""
    if isinstance(p_mark,str):
        raise TypeError("The input has to be an integer")
    elif isinstance(p_mark,float):
        raise TypeError("The input has to be an integer")
    elif p_mark >= 351 or p_mark <= -1:
        raise ValueError("The input has to be inbetween 350 and 0 inclusive")
    elif int(p_mark) <= 60:
        p_grade = "U"
    elif int(p_mark) <= 104:
        p_grade = "E"
    elif int(p_mark) <= 149:
        p_grade = "D"
    elif int(p_mark) <= 194:
        p_grade = "C"
    elif int(p_mark) <= 239:
        p_grade = "B"
    elif int(p_mark) <= 298:
        p_grade = "A"
    elif int(p_mark) <= 350:
        p_grade = "A*"
    return p_grade

if __name__ == '__main__':
    mark = int(input("What mark did you get? "))
    grade = calc_grade(mark)
    print(calc_grade(mark))