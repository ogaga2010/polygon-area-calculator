class Polygon():
  def __init__(self, num_sides):
   self.num_sides = num_sides
     
class Triangle(Polygon):
            def __init__(self, base, height):
                self.base = base
                self.height = height
   
            def area(self):
                return 0.5 * self.base * self.height

class Rectangle(Polygon):
            def __init__(self, width, height):
                self.width = width
                self.height = height
   
            def area(self):
                 return self.width * self.height

class Square(Polygon):
            def __init__(self, side):
                self.side = side
   
            def area(self):
                return self.side * self.side
   
if __name__ == "__main__":
    tri = Triangle(10, 5)
    print(f"Area of triangle: {tri.area()}")

    rect = Rectangle(10, 5)
    print(f"Area of Rectangle: {rect.area()}")

    sq = Square(4)
    print(f"Area of Square: {sq.area()}")


