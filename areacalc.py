import math

def circle_area(radius):
    return math.pi * radius * radius

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return base * height / 2

stop = False
while not stop:
    u_shape = input('Pick a shape: C=circle, R=rectangle, T=triangle: ')
    if u_shape == 'C':
        u_radius = float(input('Enter the radius: '))
        print('The area of the circle is: ' + str(circle_area(u_radius)))
    elif u_shape == 'R':
        u_length = float(input('Enter the length: '))
        u_width = float(input('Enter the width: '))
        r_area = rectangle_area(u_length, u_width)
        print(f'The area of the rectangle is: {r_area}')
    elif u_shape == 'T':
        u_base = float(input('Enter the base: '))
        u_height = float(input('Enter the height: '))
        print('The area of the triangle is: ' + str(triangle_area(u_base, u_height)))
    else:
        print('Invalid input! Try again')

    yes_no = input('Do you want to quit? y/n: ')
    if yes_no == 'y':
        stop = True