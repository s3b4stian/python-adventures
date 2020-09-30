#########
# classes
#########

class Rectangle:
    ## dunder init method
    ## run once the object is created
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    ## dunder to string method called when cast to string
    ## triggered with ex print(str(r1))
    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"

    ## dunder representation method, show how the object is built
    ## triggered with ex print(r1)
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
    ## dunder equal method, called when comparing objects using ==
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    ## dunder less than method, called when comparing objects using <
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
print(r1.width)
print(r1.height)
print(r1.area())
print(r1.perimeter())

## address of the object
print(hex(id(r1)))

## to string
print(str(r1))

## representation
print(r1)

## equality
r2 = Rectangle(10, 20)
print(r1 is not r2)
print(r1 == r2)
print(r1 == 100)

## less than
r1 = Rectangle(10, 20)
r2 = Rectangle(20, 20)
print(r1 < r2)

### this also works well
### despite __gt__ method not implemented python flip the instruction and use __lt__ method
print(r2 > r1)

###################
# getter and setter
###################

class OtherRectangle:
    def __init__(self, width, height):
        ## calling setter inside th initializer
        self.width = width
        self.height = height

    ## define the getter for _width
    @property
    def width(self):
        print("getting width")
        return self._width

    ## define the setter for _width
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width

    ## define the getter for _height
    @property
    def height(self):
        print("Getting height")
        return self._height

    ## define the setter for _height
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Height must be positive")
        else:
            self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

r1 = OtherRectangle(10, 20)
print(r1.width)
print(r1.height)

try:
    r1.width = 0
except ValueError:
    print("Width to 0 or less")

try:
    r1.height = 0
except ValueError:
    print("Width to 0 or less")

try:
    r2 = OtherRectangle(-10, 20)
except ValueError:
    print("Initialization with 0 or less")