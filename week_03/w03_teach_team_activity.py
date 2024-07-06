square_side_length = float(input('What is the length of a side of the square? '))
square_area = square_side_length ** 2
square_area_to_hundredths_place = round(square_area, 2)
print(f"The area of the square is: {square_area_to_hundredths_place}")

rectangle_length = float(input('What is the length of the rectangle? '))
rectangle_width = float(input('What is the width of the rectangle? '))
rectangle_area = rectangle_length * rectangle_width
rectangle_area_rounded_to_hundredths_place = round(rectangle_area, 2)
print(f"The area of the rectangle is: {rectangle_area_rounded_to_hundredths_place}")

circle_radius = float(input('What is the radius of the circle? '))
circle_area = 3.14 * circle_radius**2
circle_area_rounded_to_hundredths_place = round(circle_area, 2)
print(f'The area of the circle is: {circle_area_rounded_to_hundredths_place}')