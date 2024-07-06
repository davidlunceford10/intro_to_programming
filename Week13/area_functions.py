import math

def compute_area_square(length):
    area = length ** 2
    return area

def compute_area_rectangle(length, width):
    area = length * width
    return area

def compute_area_circle(radius):
    area = math.pi * (radius ** 2)
    return area

continue_loop = True

while continue_loop:
    
    shape = input('What shape do you have? ').lower()
    
    if shape == 'square':
        square_side = float(input('What is the length of one side of your square? '))
        print(f'The area of your square is: {compute_area_square(square_side)}')
        
    elif shape == 'rectangle':
        rectangle_length = float(input('What is the length of your rectangle? '))
        rectangle_width = float(input('What is the width of your rectangle? '))
        print(f'The area of your rectangle is: {compute_area_rectangle(rectangle_length, rectangle_width)}')
    
    elif shape == 'circle':
        circle_radius = float(input('What is your circle radius? '))
        print(f'The area of your circle is: {compute_area_circle(circle_radius):.2f}')
        
    elif shape == 'quit':
        continue_loop = False
        
   
        
    
        
    
        