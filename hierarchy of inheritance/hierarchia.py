import abc
import math
from tkinter import *
import sys

class Colours:
    def __init__(self):
        self.colours_tab = ["black", "white", "blue", "red", "green", "yellow",
                            "silver", "gray", "pink", "brown", "orange"]

    def print_colours(self):
        print(self.colours_tab)

class ColourDescriptor:
    def __init__(self, value="black", name=""):
        self.value = value
        self.name = name
        self.colours = Colours()

    def __set__(self, instance, value):
        my_exit = 0
        while my_exit == 0:
            for x in self.colours.colours_tab:
                if value == x:
                    self.value = value
                    my_exit = 1
            if my_exit == 0:
                print("Wprowadzony " + self.name + " powinień być wybrany z poniższej listy. Spróbuj ponownie.")
                self.colours.print_colours()
                value = str(input())

    def __get__(self, instance, owner):
        return self.value

class FloatDescriptor:
    def __init__(self, side=0, name=""):
        self._side = side
        self._name = name

    def __set__(self, instance, value):
        my_exit = 0
        while my_exit == 0:
            try:
                value = float(value)
                while my_exit == 0:
                    if value > 0:
                        my_exit = 1
                        self._side = value
                    else:
                        print("Wprowadzona wartość jest mniejsza od 0. Proszę wprowadzić długość " + self._name + " ponownie")
                        value = float(input())
            except ValueError:
                print("Wartość " + self._name + " powinna być liczbą. Spróbuj ponownie.")
                value = input()

    def __get__(self, instance, owner):
        return self._side

class AngleDescriptor:
    def __init__(self, value=0):
        self._angle = value

    def __set__(self, instance, value):
        my_exit = 0
        while my_exit == 0:
            try:
                value = float(value)
                while my_exit == 0:
                    if 0 < value < 180:
                        self._angle = value
                        my_exit = 1
                    else:
                        print("Wartość kąta powinna się zawierać między 0 a 180. Spróbuj ponownie")
                        value = float(input())
            except ValueError:
                print("Kąt musi być liczbą. Spróbuj ponownie.")
                value = input()

    def __get__(self, instance, owner):
        return self._angle


class ConvexPolygon(abc.ABC):
    _fill_colour = ColourDescriptor(name="kolor wypełnienia")
    _outline_colour = ColourDescriptor(name="kolor krawędzi")
    @abc.abstractmethod
    def __init__(self, fill_colour, outline_colour):
        self._fill_colour = fill_colour
        self._outline_colour = outline_colour

    @abc.abstractmethod
    def area(self):
        raise NotImplementedError

    @abc.abstractmethod
    def perimeter(self):
        raise NotImplementedError

    @abc.abstractmethod
    def draw(self):
        raise NotImplementedError

class Triangle(ConvexPolygon): #trójkąt
    _side_a = FloatDescriptor(name="podstawy 'a'")
    _side_b = FloatDescriptor(name="boku 'b'")
    _side_c = FloatDescriptor(name="boku 'c'")

    def __init__(self, fill_colour, outline_colour, side_a, side_b, side_c):
        super(Triangle, self).__init__(fill_colour, outline_colour)
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c
        my_exit = 0
        while my_exit == 0:
            if self._side_a != self._side_b:
                if self._side_b != self._side_c:
                    if self._side_b == self._side_c:
                        if (self._side_b * 2) > self._side_a:
                            if (self._side_a + self._side_b) > self._side_b:
                                my_exit = 1
                            else:
                                print("Wprowadzone dane są nieprawidłowe, wprowadź ponownie dane.")
                                print("Wprowadź długość boku 'a':")
                                self._side_a = input()
                                print("Wprowadź długość boku 'b':")
                                self._side_b = input()
                                self._side_c = self._side_b
                        else:
                            print("Wprowadzone dane są nieprawidłowe, wprowadź ponownie dane.")
                            print("Wprowadź długość boku 'a':")
                            self._side_a = input()
                            print("Wprowadź długość boku 'b':")
                            self._side_b = input()
                            self._side_c = self._side_b
                    elif (self._side_a + self._side_b) > self._side_c:
                        if (self._side_a + self._side_c) > self._side_b:
                            if (self._side_b + self._side_c) > self._side_a:
                                my_exit = 1
                            else:
                                print("Wprowadzone dane są nieprawidłowe, wprowadź ponownie dane.")
                                print("Wprowadź długość boku 'a':")
                                self._side_a = input()
                                print("Wprowadź długość boku 'b':")
                                self._side_b = input()
                                print("Wprowadź długość boku 'c':")
                                self._side_c = input()
                        else:
                            print("Wprowadzone dane są nieprawidłowe, wprowadź ponownie dane.")
                            print("Wprowadź długość boku 'a':")
                            self._side_a = input()
                            print("Wprowadź długość boku 'b':")
                            self._side_b = input()
                            print("Wprowadź długość boku 'c':")
                            self._side_c = input()
                    else:
                        print("Wprowadzone dane są nieprawidłowe, wprowadź ponownie dane.")
                        print("Wprowadź długość boku 'a':")
                        self._side_a = input()
                        print("Wprowadź długość boku 'b':")
                        self._side_b = input()
                        print("Wprowadź długość boku 'c':")
                        self._side_c = input()
                else:
                    my_exit = 1
            else:
                my_exit = 1

    def area(self):
        a = self._side_a
        b = self._side_b
        c = self._side_c
        p = (a+b+c)/2
        area = math.sqrt(p*(p-a)*(p-b)*(p-c)) #wzór Herona
        return area

    def perimeter(self):
        return self._side_a + self._side_b + self._side_c

    def draw(self, canvas):
        h = (2 * self.area() / self._side_a)
        a = [0,0]
        b = [self._side_a, 0]
        cx = ((math.pow(self._side_b, 2) - math.pow(self._side_c, 2) + math.pow(b[0], 2)) / (2*b[0]))
        cy = (math.sqrt(math.pow(self._side_c, 2)-math.pow(cx, 2)))
        c = [cx, cy]
        a[0] = 400-(self._side_a/2)
        a[1] = 300-(h/2)
        b[0] = b[0] + 400 - (self._side_a/2)
        b[1] = b[1] + 300 - (h/2)
        c[0] = c[0] + 400 - (self._side_a/2)
        c[1] = c[1] + 300 - (h/2)
        coordinates = [a,b,c]
        canvas.create_polygon(coordinates, fill=self._fill_colour, outline=self._outline_colour)

class IsoscelesTriangle(Triangle):
    def __init__(self, fill_colour, outline_colour, side_a, side_b):
        super(IsoscelesTriangle, self).__init__(fill_colour, outline_colour, side_a, side_b, side_b)

class EquilateralTriangle(Triangle):
    def __init__(self, fill_colour, outline_colour, side_a):
        super(EquilateralTriangle, self).__init__(fill_colour, outline_colour, side_a, side_a, side_a)

class ConvexQuadrilateral(ConvexPolygon):
    _diagonal_p = FloatDescriptor(name="pierwsza przekątna")
    _diagonal_q = FloatDescriptor(name="druga przekątna")
    _diagonal_p_intersection = FloatDescriptor(name="przecięcie pierwszej przekątnej")
    _diagonal_q_intersection = FloatDescriptor(name="przecięcie drugiej przekątnej")
    _angle = AngleDescriptor()

    def __init__(self, fill_colour, outline_colour, diagonal_p, diagonal_q, intersection_p, intersection_q, angle):
        super(ConvexQuadrilateral, self).__init__(fill_colour, outline_colour)
        self._diagonal_p = diagonal_p
        self._diagonal_q = diagonal_q
        self._diagonal_p_intersection = intersection_p
        self._diagonal_q_intersection = intersection_q
        self._angle = angle
        self._angle = math.radians(self._angle)

        my_exit = 0
        while my_exit == 0:
            if self._diagonal_p > self._diagonal_p_intersection:
                if self._diagonal_q > self._diagonal_q_intersection:
                    my_exit = 1
                else:
                    print("Wartość przecięcia drugiej przekątnej jest większa niż długośc drugiej przekątnej. "
                          "Wpisz ponownie wartości")
                    print("Podaj długość drugiej przekątnej:")
                    self._diagonal_q = input()
                    print("Podał długość przecięcia drugiej przekątnej:")
                    self._diagonal_q_intersection = input()
            else:
                print("Wartość przecięcia pierwszej przekątnej jest większa niż długośc pierwszej przekątnej. "
                      "Wpisz ponownie wartości")
                print("Podaj długość pierwszej przekątnej:")
                self._diagonal_p = input()
                print("Podał dłogość przecięcia pierwszej przekątnej:")
                self._diagonal_p_intersection = input()

        self._side_a = math.sqrt(math.pow(self._diagonal_p_intersection, 2) + math.pow(self._diagonal_q -
                        self._diagonal_q_intersection, 2) - (2 * (self._diagonal_p_intersection * (self._diagonal_q -
                        self._diagonal_q_intersection)) * math.cos(self._angle)))

        self._side_b = math.sqrt(math.pow(self._diagonal_p_intersection, 2) + math.pow(self._diagonal_q_intersection, 2)
                        - 2 * (self._diagonal_p_intersection * self._diagonal_q_intersection *
                        math.cos(math.radians(180) - self._angle)))

        self._side_c = math.sqrt(math.pow(self._diagonal_q_intersection, 2) + math.pow(self._diagonal_p -
                        self._diagonal_p_intersection, 2) - (2 * (self._diagonal_q_intersection * (self._diagonal_p -
                        self._diagonal_q_intersection)) * math.cos(self._angle)))

        self._side_d = math.sqrt(math.pow(self._diagonal_q - self._diagonal_q_intersection, 2) +
                        math.pow(self._diagonal_p - self._diagonal_p_intersection, 2)
                        - (2 * (self._diagonal_q - self._diagonal_q_intersection) *
                        (self._diagonal_p - self._diagonal_p_intersection) * math.cos(math.radians(180)
                        - self._angle)))

    def area(self):
        return (1/2) * (self._diagonal_p * self._diagonal_q * math.sin(self._angle))

    def perimeter(self):
        return self._side_a + self._side_b + self._side_c + self._side_d

    def draw(self, canvas):
        b = [-self._diagonal_p_intersection, 0]
        cx = ((math.pow(self._diagonal_q - self._diagonal_q_intersection, 2) - math.pow(self._side_a, 2) +
               math.pow(b[0], 2))/(2*b[0]))
        cy = math.sqrt((math.pow(self._diagonal_q - self._diagonal_q_intersection, 2) - math.pow(cx, 2)))
        c = [cx, cy]
        d = [self._diagonal_p - self._diagonal_p_intersection, 0]
        ex = ((math.pow(self._diagonal_q_intersection, 2) - math.pow(self._side_b, 2) + math.pow(b[0], 2)) / (2*b[0]))
        ey = -(math.sqrt(math.pow(self._diagonal_q_intersection, 2) - math.pow(ex, 2)))
        e = [ex, ey]
        b[0] += 400 + self._diagonal_p_intersection - (self._diagonal_p/2)
        b[1] += 300
        c[0] += 400 + self._diagonal_p_intersection - (self._diagonal_p/2)
        c[1] += 300
        d[0] += 400 + self._diagonal_p_intersection - (self._diagonal_p/2)
        d[1] += 300
        e[0] += 400 + self._diagonal_p_intersection - (self._diagonal_p/2)
        e[1] += 300
        coordinates = [b,c,d,e]
        canvas.create_polygon(coordinates, fill=self._fill_colour, outline=self._outline_colour)

class Parallelogram(ConvexQuadrilateral):
    _diagonal_p = FloatDescriptor(name="pierwsza przekątna")
    _diagonal_q = FloatDescriptor(name="druga przekątna")

    def __init__(self, fill_colour, outline_colour, diagonal_p, diagonal_q, angle):
        self._diagonal_p = diagonal_p
        self._diagonal_q = diagonal_q
        super(Parallelogram, self).__init__(fill_colour, outline_colour, self._diagonal_p, self._diagonal_q,
                                            self._diagonal_p/2, self._diagonal_q/2, angle)

class Kite(ConvexQuadrilateral):
    _second_diagonal = FloatDescriptor(name="druga przekątna")

    def __init__(self, fill_colour, outline_colour, diagonal_p, diagonal_q, diagonal_p_intersection):
        self._second_diagonal = diagonal_q
        super(Kite, self).__init__(fill_colour, outline_colour, diagonal_p, self._second_diagonal,
                                   diagonal_p_intersection, self._second_diagonal/2, 90)

class Rhombus(Parallelogram):
    def __init__(self, fill_colour, outline_colour, diagonal_p, diagonal_q):
        super(Rhombus, self).__init__(fill_colour, outline_colour, diagonal_p, diagonal_q, 90)

class Square(Rhombus):
    def __init__(self, fill_colour, outline_colour, diagonal):
        super(Square, self).__init__(fill_colour, outline_colour, diagonal, diagonal)

class RegularPentagon(ConvexPolygon):
    _side = FloatDescriptor(name="bok")

    def __init__(self, fill_colour, outline_colour, side):
        super(RegularPentagon, self).__init__(fill_colour, outline_colour)
        self._side = side

    def area(self):
        return math.pow(self._side, 2) * (math.sqrt(25 + (10 * math.sqrt(5))))/4

    def perimeter(self):
        return 5*self._side

    def draw(self, canvas):
        angle = 0 - (math.pi / 5)
        radius = self._side / (2 * (math.tan(math.pi / 5)))
        coordinates = [[400 + radius * math.sin((2 * math.pi / 5) * i - angle),
                        300 + radius * math.cos((2 * math.pi / 5) * i - angle)] for i in range(5)]
        canvas.create_polygon(coordinates, fill=self._fill_colour, outline=self._outline_colour)

class RegularHexagon(ConvexPolygon):
    _side = FloatDescriptor(name="bok")

    def __init__(self, fill_colour, outline_colour, side):
        super(RegularHexagon, self).__init__(fill_colour, outline_colour)
        self._side = side
        self._radius = self._side * (math.sqrt(3)/2)

    def area(self):
        return 2*(math.sqrt(3) * math.pow(self._radius, 2))

    def perimeter(self):
        return 6*self._side

    def draw(self, canvas):
        angle = 0 - (math.pi / 6)
        radius = self._radius
        coordinates = [[400 + radius * math.sin((2 * math.pi / 6) * i - angle),
                        300 + radius * math.cos((2 * math.pi / 6) * i - angle)] for i in range(6)]
        canvas.create_polygon(coordinates, fill=self._fill_colour, outline=self._outline_colour)


class RegularOctagon(ConvexPolygon):
    _side = FloatDescriptor(name="bok")

    def __init__(self, fill_colour, outline_colour, side):
        super(RegularOctagon, self).__init__(fill_colour, outline_colour)
        self._side = side
        self._radius = self._side * ((1 + math.sqrt(2))/2)

    def area(self):
        return 2*((1 + math.sqrt(2)) * math.pow(self._side, 2))

    def perimeter(self):
        return 8*self._side

    def draw(self, canvas):
        angle = 0 - (math.pi / 8)
        radius = self._radius
        coordinates = [[400 + radius * math.sin((2 * math.pi / 8) * i - angle),
                        300 + radius * math.cos((2 * math.pi / 8) * i - angle)] for i in range(8)]
        canvas.create_polygon(coordinates, fill=self._fill_colour, outline=self._outline_colour)



ColourList = Colours()
print("------PROGRAM DO LICZENIA PÓL FIGUR GEOMETRYCZNYCH------")
print("Witaj, z poniższej listy wybierz interesującą Cię figurę:")
print("1. Trójkąt")
print("2. Trójkąt równoramienny")
print("3. Trójkąt równoboczny")
print("4. Czworokąt wypukły")
print("5. Równoległobok")
print("6. Deltoid")
print("7. Romb")
print("8. Kwadrat")
print("9. Pięciokąt regularny")
print("10. Sześciokąt regularny")
print("11. Ośmiokąt regularny")
print("Aby wyjść, wciśnij inny klawisz.")

select = str(input())

if select == "1":
    print("Wybierz kolor wypełnienia trójkąta. Możesz wybrać kolor z poniższej listy.")
    ColourList.print_colours()
    input_fill = str(input())
    print("Wybierz kolor krawędzi.")
    input_outline = str(input())
    print("Podaj długość podstawy 'a':")
    input_side_a = input()
    print("Podaj długość boku 'b':")
    input_side_b = input()
    print("Podaj długość boku 'c':")
    input_side_c = input()
    convex_polygon = Triangle(input_fill, input_outline, input_side_a, input_side_b, input_side_c)
elif select == "2":
    print("Wybierz kolor wypełnienia trójkąta. Możesz wybrać kolor z poniższej listy.")
    ColourList.print_colours()
    input_fill = str(input())
    print("Wybierz kolor krawędzi.")
    input_outline = str(input())
    print("Podaj długość podstawy 'a':")
    input_side_a = input()
    print("Podaj długość boku 'b':")
    input_side_b = input()
    convex_polygon = IsoscelesTriangle(input_fill, input_outline, input_side_a, input_side_b)
elif select == "3":
    print("Wybierz kolor wypełnienia trójkąta. Możesz wybrać kolor z poniższej listy.")
    ColourList.print_colours()
    input_fill = str(input())
    print("Wybierz kolor krawędzi.")
    input_outline = str(input())
    print("Podaj długość podstawy 'a':")
    input_side_a = input()
    convex_polygon = EquilateralTriangle(input_fill, input_outline, input_side_a)
elif select == "4":
    print("Wybierz kolor wypełnienia czworokąta. Możesz wybrać kolor z poniższej listy. ")
    ColourList.print_colours()
    input_fill = str(input())
    print("Wybierz kolor krawędzi czworokąta: ")
    input_outline = str(input())
    print("Podaj długośc pierwszej przekątnej: ")
    input_diagonal_p = input()
    print("Podaj długość przecięcia pierwszej przekątnej: ")
    input_diagonal_p_intersection = input()
    print("Podaj długośc drugiej przekątnej: ")
    input_diagonal_q = input()
    print("Podaj długość przecięcia drugiej przekątnej: ")
    input_diagonal_q_intersection = input()
    print("Podaj wartość kątą zawartego między przekątnymi: ")
    input_angle = input()
    convex_polygon = ConvexQuadrilateral(input_fill, input_outline, input_diagonal_p, input_diagonal_q,
                                         input_diagonal_p_intersection, input_diagonal_q_intersection, input_angle)
elif select == "5":
    print("Wybierz kolor wypełnienia równoległoboku. Możesz wybrać kolor z poniższej listy. ")
    ColourList.print_colours()
    input_fill = str(input())
    print("Wybierz kolor krawędzi równoległoboku: ")
    input_outline = str(input())
    print("Podaj długośc pierwszej przekątnej: ")
    input_diagonal_p = input()
    print("Podaj długośc drugiej przekątnej: ")
    input_diagonal_q = input()
    print("Podaj wartość kątą zawartego między przekątnymi: ")
    input_angle = input()
    convex_polygon = Parallelogram(input_fill, input_outline, input_diagonal_p, input_diagonal_q, input_angle)
elif select == "6":
    print("Wybierz kolor wypełnienia deltoidu. Możesz wybrać kolor z poniższej listy. ")
    ColourList.print_colours()
    input_fill = str(input())
    print("Wybierz kolor krawędzi deltoidu: ")
    input_outline = str(input())
    print("Podaj długośc pierwszej przekątnej: ")
    input_diagonal_p = input()
    print("Podaj długość przecięcia pierwszej przekątnej: ")
    input_diagonal_p_intersection = input()
    print("Podaj długośc drugiej przekątnej: ")
    input_diagonal_q = input()
    convex_polygon = Kite(input_fill, input_outline, input_diagonal_p, input_diagonal_q, input_diagonal_p_intersection)
elif select == "7":
    print("Wybierz kolor wypełnienia rombu. Możesz wybrać kolor z poniższej listy. ")
    ColourList.print_colours()
    input_fill = str(input())
    print("Wybierz kolor krawędzi rombu: ")
    input_outline = str(input())
    print("Podaj długośc pierwszej przekątnej: ")
    input_diagonal_p = input()
    print("Podaj długośc drugiej przekątnej: ")
    input_diagonal_q = input()
    convex_polygon = Rhombus(input_fill, input_outline, input_diagonal_p, input_diagonal_q)
elif select == "8":
    print("Wybierz kolor wypełnienia kwadratu. Możesz wybrać kolor z poniższej listy. ")
    ColourList.print_colours()
    input_fill = str(input())
    print("Wybierz kolor krawędzi kwadratu: ")
    input_outline = str(input())
    print("Podaj długośc przekątnej: ")
    input_diagonal = input()
    convex_polygon = Square(input_fill, input_outline, input_diagonal)
elif select == "9":
    print("Wybierz kolor wypełnienia pięciokąta. Możesz wybrać kolor z poniższej listy. ")
    ColourList.print_colours()
    input_fill = str(input())
    print("Wybierz kolor krawędzi pięciokąta: ")
    input_outline = str(input())
    print("Podaj długośc boku: ")
    input_side = input()
    convex_polygon = RegularPentagon(input_fill, input_outline, input_side)
elif select == "10":
    print("Wybierz kolor wypełnienia sześciokąta. Możesz wybrać kolor z poniższej listy. ")
    ColourList.print_colours()
    input_fill = str(input())
    print("Wybierz kolor krawędzi sześciokąta: ")
    input_outline = str(input())
    print("Podaj długośc boku: ")
    input_side = input()
    convex_polygon = RegularHexagon(input_fill, input_outline, input_side)
elif select == "11":
    print("Wybierz kolor wypełnienia ośmiokąta. Możesz wybrać kolor z poniższej listy. ")
    ColourList.print_colours()
    input_fill = str(input())
    print("Wybierz kolor krawędzi ośmiokąta: ")
    input_outline = str(input())
    print("Podaj długośc boku: ")
    input_side = input()
    convex_polygon = RegularOctagon(input_fill, input_outline, input_side)
else:
    print("Miłego dnia!")
    sys.exit()

print("Pole powierzchni wybranej figury jest równe: ")
print(convex_polygon.area())
print("Obwód wybranej figury jest równy: ")
print(convex_polygon.perimeter())

root = Tk()
root.geometry('800x600')

canv = Canvas(root, width=800, height=600, bg="white")
convex_polygon.draw(canv)
canv.pack()
root.mainloop()