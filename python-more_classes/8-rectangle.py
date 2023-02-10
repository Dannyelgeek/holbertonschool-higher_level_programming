#!/usr/bin/python3
'''creating a Rectangle.'''


class Rectangle:
    '''width will be a private attribute'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Width attribute privacy.'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''Set width value.'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height attribute privacy'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''Set height value.'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Rectangle area.'''
        area_w = self.__width
        area_h = self.__height
        return (area_w * area_h)

    def perimeter(self):
        '''Rectangle perimeter'''
        per_w = self.__width
        per_h = self.__height
        if per_h == 0 or per_w == 0:
            return 0
        else:
            return (2 * (per_w + per_h))

    def bigger_or_equal(rect_1, rect_2):
        '''Returns the biggest rectangle based on the area.'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    def __str__(self):
        '''print a rectangle'''
        new_line = ""
        rect_w = self.__width
        rect_h = self.__height
        if rect_w == 0 or rect_h == 0:
            return (new_line)
        else:
            for ind in range(rect_h):
                for ind_2 in range(rect_w):
                    new_line += str(self.print_symbol)
                if ind != rect_h - 1:
                    new_line += "\n"
            return (new_line)

    def __repr__(self):
        '''Return a representation of the rectangle'''
        w = str(self.__width)
        h = str(self.__height)
        repr = "Rectangle(" + w + ", " + h + ")"
        return (repr)

    def __del__(self):
        '''Prints a del message'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
