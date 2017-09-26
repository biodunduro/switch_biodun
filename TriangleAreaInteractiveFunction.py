def triangle_area():
    triangle_height = int(input('What is the height?: '))
    triangle_base = int(input('What is the base?: '))
    the_area = (triangle_base/2) * triangle_height
    return the_area

print(triangle_area())

