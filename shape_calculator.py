class Rectangle:
  # setting the dimensions that will be used
  def __init__(self, width, height):
    self.width = width
    self.height = height

  # defining the width and height
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  # Calculating the area of the shape
  def get_area(self):
    return self.width * self.height

  # finding the perimeter of teh shape
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  # finding the diagonal of the shape
  def get_diagonal(self):
    return (self.width**2 + self.height**2)**.5

  # Generating the image of the shape
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        picture += "*" * self.width + "\n"
      return picture

  # Finding the amount inside
  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())

  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)


# Making a child class to inherit from the parent Rectangle class
class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return "Square(side={})".format(self.width)
