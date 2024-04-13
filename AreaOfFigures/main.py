from classes.Circle import Circle
from classes.Triangle import Triangle

figures={"Circle":Circle,
         "Triangle":Triangle}



print(f"List figures: {", ".join(figures.keys())}")
figure_name = input("Enter figure name: ")

while figure_name in figures.keys():
    parameter = input("Enter parameter: ")

    if figure_name == "Circle":
        if not parameter.strip().isdigit():
            print("Please enter a one number")
            continue
        parameter = int(parameter)
    elif figure_name == "Triangle":
        parameter = parameter.split()
        parameter = [int(i) for i in parameter if i.isdigit()]
        if len(parameter) != 3:
            print("Please enter three numbers")
            continue

    print(f"The area of the {figure_name} is equal to {figures[figure_name](parameter).area()}")
    break
if figure_name not in figures.keys():
    print("Please enter a valid figure name")