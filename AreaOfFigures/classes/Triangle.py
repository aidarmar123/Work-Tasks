class Triangle:
    sides = []
    def __init__(self, sides:list):
        self.sides = sides

    def area(self):
        semi_perimetr = (self.sides[0]+self.sides[1]+self.sides[2])/2 # Полупериметр
        area = semi_perimetr
        for side in self.sides:
            area = area*(semi_perimetr-side)
        #Вычесление площади по формуле Герона
        return round(area**(1/2),2)

    def is_rectangle(self):
        hypotenuse = max(self.sides) #Гипотенуза

        legs = self.sides
        legs.remove(hypotenuse)  #Катеты

        if hypotenuse**2 == legs[0]**2+legs[1]**2:
        #Проверка по теореме Пифагора
            return True
        else:
            return False


