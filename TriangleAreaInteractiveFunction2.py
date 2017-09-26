def triangle_area():
    triangle_height = input('What is the height?: ')
    if str.isdigit(triangle_height):
        triangle_height = int(triangle_height)
    else:
        print('Pleae enter a value')
       
    triangle_base = input('What is the base?: ')
    if str.isdigit(triangle_base):
        triangle_base = int(triangle_base)
    else:
        print('Pleae enter a value')
    
    the_area = (triangle_base/2) * triangle_height
    return the_area

print(triangle_area())
